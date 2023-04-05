"""
@RW
"""

import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
dir_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(dir_path, "../log/error.log")
fh = logging.FileHandler(log_path)
fh.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
