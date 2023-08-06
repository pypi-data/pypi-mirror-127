import logging
import os
from pathlib import Path
import time

import cgmml.models.HRNET.code.models.pose_hrnet  # noqa
import cv2
import glob2 as glob
import pandas as pd
import torch
import torch.backends.cudnn as cudnn
import torch.nn.parallel
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import torchvision
from cgmml.models.HRNET.code.config import cfg, update_config
from cgmml.models.HRNET.code.config.constants import (COCO_KEYPOINT_INDEXES, NUM_KPTS)
from cgmml.models.HRNET.code.models.pose_hrnet import get_pose_net
from cgmml.models.HRNET.code.utils.google_drive_utils import download_file_from_google_drive
from cgmml.models.HRNET.code.utils.utils import (box_to_center_scale, calculate_pose_score, draw_pose,
                                                 get_person_detection_boxes, get_pose_estimation_prediction, rot)


logging.basicConfig(level=logging.INFO, filename='pose_prediction.log',
                    format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', filemode='w')


REPO_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_DIR / 'data'
CONFIG_PATH_W32 = REPO_DIR / 'cgmml/models/HRNET/inference-config-hrnet_w32.yaml'
CONFIG_PATH_W48 = REPO_DIR / 'cgmml/models/HRNET/inference-config-hrnet_w48.yaml'
MODEL_FILE_W32 = DATA_DIR / 'pose_models' / 'pose_hrnet_w32_384x288.pth'
MODEL_FILE_W48 = DATA_DIR / 'pose_models' / 'pose_hrnet_w48_384x288.pth'
MODEL_ID_W32 = '1fGN2P81JEgzjLxCn5_PaOwaoUwT0Ybc3'
MODEL_ID_W48 = '1UoJhTtjHNByZSm96W3yFTfU5upJnsKiS'

CONFIG_PATH = CONFIG_PATH_W48
MODEL_FILE = MODEL_FILE_W48
MODEL_ID = MODEL_ID_W48
MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)


class PosePrediction:
    def __init__(self, ctx):
        self.ctx = ctx

    def load_box_model(self):
        self.box_model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
            pretrained=True)
        self.box_model.to(self.ctx)
        self.box_model.eval()

    def load_pose_model(self):
        self.pose_model = get_pose_net(cfg)
        self.pose_model.load_state_dict(torch.load(
            MODEL_FILE, map_location=torch.device('cpu')), strict=False)
        self.pose_model = torch.nn.DataParallel(self.pose_model, device_ids=cfg.GPUS)
        self.pose_model.to(self.ctx)
        self.pose_model.eval()

    def read_image(self, image_path):
        image_bgr = cv2.imread(str(image_path))
        return image_bgr, image_bgr.shape

    def orient_image_using_scan_type(self, original_image, scan_type):
        if scan_type in ['100', '101', '102', 'standing']:
            rotated_image = cv2.rotate(original_image, cv2.ROTATE_90_CLOCKWISE)  # Standing
        elif scan_type in ['200', '201', '202', 'laying']:
            rotated_image = cv2.rotate(original_image, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Laying
        else:
            logging.info("%s %s %s", "Provided scan type", scan_type, "not supported")
            logging.info("Keeping the image in the same orientation as provided")
            rotated_image = original_image
        return rotated_image

    def orient_cordinate_using_scan_type(self, pose_keypoints, scan_type, height, width):
        if scan_type in ['100', '101', '102', 'standing']:
            pose_keypoints = rot(pose_keypoints, 'ROTATE_90_COUNTERCLOCKWISE', height, width)
        elif scan_type in ['200', '201', '202', 'laying']:
            pose_keypoints = rot(pose_keypoints, 'ROTATE_90_CLOCKWISE', height, width)
        else:
            logging.info("%s %s %s", "Provided scan type", scan_type, "not supported")
            logging.info("Keeping the co-ordinate in the same orientation as provided")
        return pose_keypoints

    def preprocess_image(self, rotated_image):
        box_model_input = []
        rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
        img_tensor = torch.from_numpy(rotated_image_rgb / 255.).permute(2, 0, 1).float().to(self.ctx)
        box_model_input.append(img_tensor)
        return box_model_input, rotated_image_rgb

    def perform_box_on_image(self, box_model_input):
        pred_boxes, pred_score = get_person_detection_boxes(
            self.box_model, box_model_input, threshold=cfg.BOX_MODEL.THRESHOLD)
        return pred_boxes, pred_score

    def perform_pose_on_image(self, pose_bbox, rotated_image_rgb):
        center, scale = box_to_center_scale(pose_bbox, cfg.MODEL.IMAGE_SIZE[0], cfg.MODEL.IMAGE_SIZE[1])
        pose_preds, pose_score = get_pose_estimation_prediction(self.pose_model, rotated_image_rgb, center, scale)
        return pose_preds, pose_score

    def pose_draw_on_image(self, rotated_pose_preds, original_image):
        if len(rotated_pose_preds) >= 1:
            for kpt in rotated_pose_preds:
                draw_pose(kpt, original_image)  # draw the poses

    def save_final_image(self, final_image_name, original_image):
        cv2.imwrite('outputs/' + final_image_name, original_image)


class ResultGeneration:
    def __init__(self, pose_prediction, save_pose_overlay):
        self.pose_prediction = pose_prediction
        self.save_pose_overlay = save_pose_overlay

    def result_on_artifact_level(self, jpg_path, scan_type):
        jpg_path = str(jpg_path)
        image = self.pose_prediction.read_image(jpg_path)
        return self.result_on_artifact_level_from_image(image, jpg_path, scan_type)

    def result_on_artifact_level_from_image(self, image, jpg_path, scan_type):
        """Detects persons in image and provide coordinates in pixels

        Args:
            image (object): Image data in OpenCV format
            jpg_path (str): Path to the RGB file in JPG format (only for writing purpose)
            scan_type (str): Type of the scan '100', '101', '102', '200', '201', '202'

        Returns:
            dict: JSON structure containing amount of detected persons, skeleton coordinates
        """
        start_time = time.time()

        jpg_path = str(jpg_path)
        shape = image.shape
        rotated_image = self.pose_prediction.orient_image_using_scan_type(image, scan_type)
        box_model_input, rotated_image_rgb = self.pose_prediction.preprocess_image(rotated_image)

        pred_boxes, pred_score = self.pose_prediction.perform_box_on_image(box_model_input)

        pose_result = []

        # Get Height,Width,color from Image
        (height, width, color) = shape
        # one box ==> one pose pose[0]

        for idx, pose_bbox in enumerate(pred_boxes):
            single_body_pose_result = {}
            key_points_coordinate_list = []
            key_points_prob_list = []

            pose_preds, pose_score = self.pose_prediction.perform_pose_on_image(pose_bbox, rotated_image_rgb)
            pose_preds[0] = self.pose_prediction.orient_cordinate_using_scan_type(
                pose_preds[0], scan_type, height, width)

            if self.save_pose_overlay:
                self.pose_prediction.pose_draw_on_image(pose_preds, image)
                if idx == len(pred_boxes) - 1:
                    self.pose_prediction.save_final_image(jpg_path.split('/')[-1], image)

            for i in range(0, NUM_KPTS):
                key_points_coordinate_list.append(
                    {COCO_KEYPOINT_INDEXES[i]: {'x': pose_preds[0][i][0], 'y': pose_preds[0][i][1]}})
                key_points_prob_list.append({COCO_KEYPOINT_INDEXES[i]: {'score': pose_score[0][i][0]}})
            body_pose_score = calculate_pose_score(pose_score)

            single_body_pose_result = {
                'bbox_coordinates': pose_bbox,
                'bbox_confidence_score': pred_score,
                'key_points_coordinate': key_points_coordinate_list,
                'key_points_prob': key_points_prob_list,
                'body_pose_score': body_pose_score
            }
            pose_result.append(single_body_pose_result)

        end_time = time.time()
        pose_result_of_artifact = {'no_of_body_pose_detected': len(pred_boxes),
                                   'pose_result': pose_result,
                                   'time': end_time - start_time
                                   }
        return pose_result_of_artifact

    def result_on_scan_level(self, scan_parent):
        self.qr_code = []
        self.scan_step = []
        self.artifact_id = []
        self.no_of_body_pose_detected = []
        self.pose_result = []
        self.time = []
        # self.artifact_pose_result = []
        logging.info("Extracting artifacts from scans")

        artifact_paths = glob.glob(os.path.join(scan_parent, "**/**/*.jpg"))

        logging.info("Result Generation Started")
        for jpg_path in artifact_paths:
            jpg_path = jpg_path.replace("\\", "/")
            split_path = jpg_path.split('/')

            qr_code, scan_step, artifact_id = split_path[3], split_path[4], split_path[5]
            pose_result_of_artifact = self.result_on_artifact_level(jpg_path, scan_step)

            self.qr_code.append(qr_code)
            self.scan_step.append(scan_step)
            self.artifact_id.append(artifact_id)
            self.no_of_body_pose_detected.append(pose_result_of_artifact['no_of_body_pose_detected'])
            self.pose_result.append(pose_result_of_artifact['pose_result'])
            self.time.append(pose_result_of_artifact['time'])
            # self.artifact_pose_result.append(pose_result_of_artifact)

    def store_result_in_dataframe(self):
        self.df = pd.DataFrame({
            'scan_id': self.qr_code,
            'scan_step': self.scan_step,
            'artifact_id': self.artifact_id,
            'no_of_body_pose_detected': self.no_of_body_pose_detected,
            'pose_result': self.pose_result,
            'processing_time': self.time
        })

    def save_to_csv(self, file_path):
        self.df.to_csv(file_path, index=False)


def get_hrnet_model() -> ResultGeneration:
    if not os.path.isfile(MODEL_FILE):
        download_file_from_google_drive(MODEL_ID, MODEL_FILE)
    ctx = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    # cudnn related setting
    cudnn.benchmark = cfg.CUDNN.BENCHMARK
    torch.backends.cudnn.deterministic = cfg.CUDNN.DETERMINISTIC
    torch.backends.cudnn.enabled = cfg.CUDNN.ENABLED
    update_config(cfg, str(CONFIG_PATH))

    pose_prediction = PosePrediction(ctx)
    pose_prediction.load_box_model()
    pose_prediction.load_pose_model()

    return ResultGeneration(pose_prediction, cfg.TEST.POSE_DRAW)


def main():
    result_generation = get_hrnet_model()
    result_generation.result_on_scan_level(cfg.TEST.DATA_PATH)

    logging.info("Result Generation done")

    result_generation.store_result_in_dataframe()
    result_generation.save_to_csv(cfg.MODEL.NAME + '.csv')


if __name__ == '__main__':
    main()
