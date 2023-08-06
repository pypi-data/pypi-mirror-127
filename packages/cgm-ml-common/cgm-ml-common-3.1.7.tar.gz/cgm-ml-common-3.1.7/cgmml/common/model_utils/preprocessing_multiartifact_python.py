import os
import re
import logging
from functools import partial
from itertools import islice
from typing import Iterator, List

from bunch import Bunch
import glob2 as glob

from cgmml.common.model_utils.model_utils_constants import SAMPLING_STRATEGY_SYSTEMATIC, SAMPLING_STRATEGY_WINDOW

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s: line %(lineno)d'))
logger.addHandler(handler)

REGEX_PICKLE = re.compile(
    r"pc_(?P<person_id>[a-zA-Z0-9-]+)_(?P<timestamp>[\d-]+)_(?P<code>\d{3})_(?P<idx>\d\.\d).p$"
)


def create_multiartifact_paths_for_qrcodes(qrcode_paths: List[str], data_config: Bunch) -> List[List[str]]:
    samples = []
    for qrcode_path in sorted(qrcode_paths):
        for code in data_config.CODES:
            p = os.path.join(qrcode_path, code)
            new_samples = _create_multiartifact_paths(p, data_config.N_ARTIFACTS, data_config)
            samples.extend(new_samples)
    return samples


def _create_multiartifact_paths(qrcode_path: str, n_artifacts: int, data_config: Bunch) -> List[List[str]]:
    """Look at files for 1 qrcode and divide into samples.

    Args:
        qrcode_path: File path of 1 qrcode, e.g. "dataset/scans/1583462470-16tvfmb1d0/100"
        n_artifacts: Desired number of artifacts in one sample

    Returns:
        List of samples, where each sample consists of muliple file paths
    """
    path_with_wildcard = os.path.join(qrcode_path, "*.p")
    list_of_pickle_file_paths = sorted(glob.glob(path_with_wildcard))

    # Split if there are multiple scans on different days TODO
    scans = [list_of_pickle_file_paths]

    # Filter to keep scans with enough artifacts
    scans = list(filter(lambda x: len(x) >= n_artifacts, scans))

    # Sample artifacts
    if data_config.SAMPLING_STRATEGY == SAMPLING_STRATEGY_SYSTEMATIC:
        samples = list(map(partial(sample_systematic_from_artifacts, n_artifacts=n_artifacts), scans))

    if data_config.SAMPLING_STRATEGY == SAMPLING_STRATEGY_WINDOW:
        samples = []
        for scan in scans:
            some_samples = list(sample_windows_from_artifacts(scan, n_artifacts=n_artifacts))
            assert len(scan) - n_artifacts + 1 == len(some_samples)
            samples.extend(some_samples)

    return samples


def sample_windows_from_artifacts(artifacts: list, n_artifacts: int) -> Iterator[list]:
    """Sample multiple windows (of length n_artifacts) from list of artifacts

    Args:
        artifacts: e.g. ['001.p', '002.p', '003.p', '004.p', '005.p', '006.p']
        n_artifacts: Desired number of artifacts in one sample

    Returns:
        samples: e.g. [
            ['001.p', '002.p', '003.p', '004.p', '005.p'],
            ['002.p', '003.p', '004.p', '005.p', '006.p'],
        ]
    """
    it = iter(artifacts)
    result = list(islice(it, n_artifacts))
    if len(result) == n_artifacts:
        yield result
    for elem in it:
        result = result[1:] + [elem]
        yield result


def sample_systematic_from_artifacts(artifacts: list, n_artifacts: int) -> list:
    n_artifacts_total = len(artifacts)
    n_skip = n_artifacts_total // n_artifacts  # 20 / 5 = 4
    indexes_to_select = list(range(n_skip // 2, n_artifacts_total, n_skip))[:n_artifacts]
    selected_artifacts = [artifacts[i] for i in indexes_to_select]
    assert len(selected_artifacts) == n_artifacts, str(artifacts)
    return selected_artifacts


def _get_epoch(fname: str) -> str:
    match_result = REGEX_PICKLE.search(fname)
    if match_result:
        return match_result.group("timestamp")
    else:
        logger.info("%s doesn't match REGEX_PICKLE", fname)
