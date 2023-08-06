import pickle
from typing import List, Tuple, Union
import logging

import numpy as np
import tensorflow as tf

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s: line %(lineno)d'))
logger.addHandler(handler)


def create_multiartifact_sample(artifacts: List[str],
                                normalization_value: float,
                                image_target_height: int,
                                image_target_width: int,
                                target_names: tf.Tensor,
                                n_artifacts: int,
                                ) -> Tuple[tf.Tensor, tf.Tensor]:
    """Open pickle files and load data.

    Args:
        artifacts: List of file paths to pickle files

    Returns:
        depthmaps of shape (IMAGE_TARGET_HEIGHT, IMAGE_TARGET_WIDTH, n_artifacts)
        targets of shape (1, )
    """
    targets_list = []
    depthmaps = np.zeros((image_target_height, image_target_width, n_artifacts))

    for i, artifact_path in enumerate(artifacts):
        depthmap, targets = _py_load_pickle(artifact_path, normalization_value,
                                            image_target_height, image_target_width, target_names)
        depthmap.set_shape((image_target_height, image_target_width, 1))
        depthmaps[:, :, i] = tf.squeeze(depthmap, axis=2)
        targets_list.append(targets)
    targets = targets_list[0]
    if not np.all(targets_list == targets):
        logger.info('Warning: Not all targets are the same!! \n target_list: %s \n artifacts: %s: ',
                    targets_list, artifacts)
    return depthmaps, targets


def _py_load_pickle(path: Union[tf.Tensor, str],
                    normalization_value: float,
                    image_target_height: int,
                    image_target_width: int,
                    target_names: tf.Tensor,
                    ) -> Tuple[Union[tf.Tensor, np.array], Union[tf.Tensor, np.array]]:
    path_ = path if isinstance(path, str) else path.numpy()
    try:
        depthmap, targets = pickle.load(open(path_, "rb"))
    except OSError as e:
        print(f"path: {path}, type(path) {str(type(path))}")
        print(e)
        raise e
    depthmap = _preprocess_depthmap(depthmap)
    depthmap = depthmap / normalization_value
    depthmap = tf.image.resize(depthmap, (image_target_height, image_target_width))
    targets = _preprocess_targets(targets, target_names)
    return depthmap, targets


def _preprocess_depthmap(depthmap: Union[tf.Tensor, np.array]) -> Union[tf.Tensor, np.array]:
    return depthmap.astype("float32")


def _preprocess_targets(targets: Union[tf.Tensor, np.array],
                        target_names_: tf.Tensor,
                        ) -> Union[tf.Tensor, np.array]:
    target_names = target_names_.numpy().tolist()
    targets = [targets[target_name.decode() if isinstance(target_name, bytes) else target_name]
               for target_name in target_names]
    return np.array(targets).astype("float32")
