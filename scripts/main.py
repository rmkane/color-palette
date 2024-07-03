#!/usr/bin/env python3

import os
import logging

from img_utils.image_scanner import ImageScanner
from img_utils.json_writer import JSONWriter
from img_utils.utils import get_script_path
from img_utils.image_processor import pixel_to_index, process_images

logging.basicConfig(level=logging.INFO)

script_dir = get_script_path()


def main():
    """
    Main function to process images and write the results to JSON files.
    """
    project_dir = os.path.join(script_dir, '..')
    image_dir = os.path.join(project_dir, 'images')
    data_dir = os.path.join(project_dir, 'data')

    scanner = ImageScanner(transformer=pixel_to_index)
    writer = JSONWriter()
    process_images(image_dir, data_dir, scanner, writer)


if __name__ == '__main__':
    main()
