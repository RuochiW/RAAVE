"""
Database Management

Author: Ruochi Wang

Date: April 8, 2023

Purpose: Provide a simple and consistent way to read and write database

License: MIT License

Dependencies: sqlite3

To install the required dependencies, run the following command:

pip install sqlite3

"""

# Import the os module for remove and create file
import os


def clear_file(file_path):
    # For testing use only
    """
    Clear the file.

    Args:
        file_path: A path to the file.

    Returns:
        None.

    Raises:
        None.

    """

    # Check if the file path exist
    if os.path.exists(file_path):

        # Remove the file
        os.remove(file_path)

        # Open the file in write mode
        with open(file_path, "w") as f:

            # Close file
            pass
