from typing import Tuple

import numpy as np

from cgmml.common.depthmap_toolkit.depthmap import is_google_tango_resolution
from cgmml.models.HRNET.body_pose import BodyPose

PREDICTION_OFFSET_IN_CM = 11.0
PREDICTION_SCALE_FACTOR = 1.01


def predict_height(depthmap_file: str, rgb_file: str, calibration_file: str) -> Tuple[float, float]:

    # Check if it is captured by a new device
    body = BodyPose.create_from_rgbd(depthmap_file, rgb_file, calibration_file)
    angle = body.dmap.get_angle_between_camera_and_floor()
    if is_google_tango_resolution(body.dmap.width, body.dmap.height):
        raise Exception('Skipping because it is not a new device data')

    # Check how many persons were detected
    person_count = body.get_person_count()
    if person_count < 1:
        raise Exception('Skipping because there is no child detected')
    if person_count > 1:
        raise Exception('Skipping because there are more persons detected')

    # Check if child is lying down
    if body.is_standing():
        raise Exception('Skipping because the child is standing')

    # Return result
    height_in_cm = body.get_person_length() * 100.0 * PREDICTION_SCALE_FACTOR + PREDICTION_OFFSET_IN_CM
    return height_in_cm, angle


def render_prediction_plots(depthmap_file: str, rgb_file: str, calibration_file: str) -> np.array:
    body = BodyPose.create_from_rgbd(depthmap_file, rgb_file, calibration_file)
    return body.debug_render()
