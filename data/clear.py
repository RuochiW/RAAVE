"""
@RW
"""

import os


def clear_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        with open(file_path, "w") as f:
            pass
