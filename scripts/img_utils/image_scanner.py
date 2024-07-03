#!/usr/bin/env python3

from PIL import Image
from typing import Callable, List


class ImageScanner:
    def __init__(self, transformer: Callable[[tuple], int], mode: str = 'RGB'):
        """
        Initialize the ImageScanner.

        :param transformer: A function to transform a pixel to a desired value.
        :param mode: The mode to convert the image to (default is 'RGB').
        """
        self.transformer = transformer
        self.mode = mode

    def read_img(self, img_path: str) -> List[int]:
        """
        Read and transform the image at the given path.

        :param img_path: The path to the image file.
        :return: A list of transformed pixel values.
        """
        image = Image.open(img_path)
        image = image.convert(self.mode)
        width, height = image.size
        return [
            [self.transformer(image.getpixel((x, y))) for y in range(height)]
            for x in range(width)
        ]
