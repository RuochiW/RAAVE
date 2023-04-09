"""
Author: Ruochi Wang
Date: April 8, 2023
Purpose: A script that logging the error
License: MIT License
Dependencies: logging, os

To install the required dependencies, run the following command:

pip install logging, os

"""

# Import the logging module for logging error
import logging

# Import the os module for get dir and file path
import os

# Import the clear_file function from the data.clear module
from data.clear import clear_file

# Get the logger instance for the current module
logger = logging.getLogger(__name__)

# Set the logger's level to ERROR
logger.setLevel(logging.ERROR)

# Get the directory path for the current module
dir_path = os.path.dirname(os.path.abspath(__file__))

# Define the path for the error log file
error_log_path = os.path.join(dir_path, "../log/error.log")

# Create a FileHandler object for the error log file
fh = logging.FileHandler(error_log_path)

# Set the level of the FileHandler to ERROR
fh.setLevel(logging.ERROR)

# Create a Formatter object to format the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the FileHandler
fh.setFormatter(formatter)

# Add the FileHandler to the logger
logger.addHandler(fh)


def clear_error_log():
    # For testing use only
    """
    Clear the error log file.

    Args:
        None.

    Returns:
        None.

    Raises:
        None.

    """

    # Clear the error log file
    clear_file(error_log_path)
