"""
@RW
"""

import logging
import os

from data.clear import clear_file

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
dir_path = os.path.dirname(os.path.abspath(__file__))
error_log_path = os.path.join(dir_path, "../log/error.log")
fh = logging.FileHandler(error_log_path)
fh.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def clear_error_log():
    clear_file(error_log_path)
