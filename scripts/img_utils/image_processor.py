#!/usr/bin/env python3

import os
from typing import List

from img_utils.colors import colors
from img_utils.image_scanner import ImageScanner
from img_utils.json_writer import JSONWriter


def process_images(img_dir: str, data_dir: str, scanner: ImageScanner, writer: JSONWriter):
    """
    Process all images in a directory and save their transformed data.

    :param img_dir: Directory containing image files.
    :param data_dir: Directory to save the output JSON files.
    :param scanner: An instance of ImageScanner.
    :param writer: An instance of JSONWriter.
    """
    os.makedirs(data_dir, exist_ok=True)
    
    for image_path in os.listdir(img_dir):
        if is_image_file(image_path):
            full_image_path = os.path.join(img_dir, image_path)
            output_path = derive_output_path(image_path, data_dir)
            process_single_image(full_image_path, scanner, writer, output_path)


def process_single_image(image_path: str, scanner: ImageScanner, writer: JSONWriter, output_path: str):
    """
    Process a single image file and save its transformed data.

    :param image_path: Path to the image file.
    :param scanner: An instance of ImageScanner.
    :param writer: An instance of JSONWriter.
    :param output_path: Path to save the output JSON file.
    """
    writer.write_json(scanner.read_img(image_path), output_path)


def pixel_to_index(pixel: tuple) -> int:
    """
    Transform a pixel to an index based on its color.

    :param pixel: A tuple representing the RGB values of the pixel.
    :return: The index of the color in the colors list.
    """
    return lookup_color(pixel_to_hex(pixel), colors)


def pixel_to_hex(pixel: tuple) -> str:
    """
    Convert a pixel to its hexadecimal color representation.

    :param pixel: A tuple representing the RGB values of the pixel.
    :return: The hexadecimal color string.
    """
    r, g, b = pixel
    return f'#{r:02x}{g:02x}{b:02x}'


def lookup_color(hex_color: str, colors: List[str]) -> int:
    """
    Look up the index of a color in the colors list.

    :param hex_color: The hexadecimal color string.
    :param colors: The list of colors.
    :return: The index of the color in the list.
    """
    return colors.index(hex_color)


def derive_output_path(img_path: str, output_dir: str) -> str:
    """
    Derive the output path for the JSON file based on the image path.

    :param img_path: The path to the image file.
    :param output_dir: The directory to save the output JSON file.
    :return: The path to the output JSON file.
    """
    return os.path.join(output_dir, os.path.basename(img_path).replace('.png', '.json'))


def is_image_file(file_path: str) -> bool:
    """
    Check if a file is an image file.

    :param file_path: The path to the file.
    :return: True if the file is an image file, False otherwise.
    """
    return file_path.lower().endswith('.png')
