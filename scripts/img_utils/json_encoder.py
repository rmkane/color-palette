#!/usr/bin/env python3

import json


class MatrixJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder to keep 2D arrays on the same line.
    """

    def iterencode(self, obj, _one_shot=False):
        """
        Encode the object as a JSON string.

        :param obj: The object to encode.
        :param _one_shot: Whether to encode the object in one shot.
        :return: The JSON string representation of the object.
        """
        if self._is_2d_array(obj):
            return self._encode_2d_array(obj)
        return super().iterencode(obj, _one_shot)

    def _encode_2d_array(self, array):
        """
        Encode a 2D array as a single line JSON string.

        :param array: The 2D array to encode.
        :return: The JSON string representation of the 2D array.
        """
        indent_str = ' ' * (self.indent or 0)
        formatted_rows = [f"{indent_str}{json.dumps(row)}" for row in array]
        return '[\n' + ',\n'.join(formatted_rows) + '\n]'

    @staticmethod
    def _is_2d_array(obj):
        """
        Check if the object is a 2D array.

        :param obj: The object to check.
        :return: True if the object is a 2D array, False otherwise.
        """
        return isinstance(obj, list) and all(isinstance(el, list) for el in obj)


if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    with open('data.json', 'w') as file:
        print(MatrixJSONEncoder(indent=2).encode(data))
