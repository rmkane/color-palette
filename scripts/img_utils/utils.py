#!/usr/bin/env python3

import os
import sys


def get_script_path():
    """
    Get the directory path of the currently executing script.

    :return: The directory path of the script.
    :rtype: str
    """
    return os.path.dirname(os.path.realpath(sys.argv[0]))
