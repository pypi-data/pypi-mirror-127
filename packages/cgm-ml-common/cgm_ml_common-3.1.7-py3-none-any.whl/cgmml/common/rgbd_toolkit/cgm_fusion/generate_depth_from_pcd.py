import logging

from cgmml.common.rgbd_toolkit.cgm_fusion import utility

# flake8: noqa: E501

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s: line %(lineno)d'))
logger.addHandler(handler)

#from cgm_fusion import calibration


# import glob, os
# os.chdir("/localssd/qrcode/")
# for file in glob.glob("*.ply"):
#     logger.info(file)

# import dbutils
# import config


# # get the number of rgb artifacts
# select_sql_statement = "SELECT path FROM artifact WHERE type='pcd';"
# pcd_paths = db_connector.execute(select_sql_statement, fetch_all=True)[0][0]
# logger.info(pcd_paths)

# fusion.get_depth_image_from_point_cloud(calibration_file="dummy", pcd_file="/tmp/cloud_debug.ply", output_file="dummy")
# utility.get_depth_channel(ply_path="/tmp/cloud_debug.ply", output_path_np = "/tmp/output.npy", output_path_png="/tmp/output.png")
# utility.get_rgbd_channel(ply_path="/tmp/cloud_debug.ply", output_path_np = "/tmp/output.npy")

utility.get_all_channel(ply_path="/tmp/cloud_debug.ply",
                        output_path_np="/tmp/output.npy")

# utility.get_viz_channel(ply_path="/tmp/cloud_debug.ply",  channel=4, output_path="/tmp/red.png")
