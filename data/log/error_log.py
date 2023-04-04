"""
@RW
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
fh = logging.FileHandler('error.log')
fh.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
