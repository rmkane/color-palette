#!/usr/bin/env python3

import logging
import json
from typing import List

from img_utils.json_encoder import MatrixJSONEncoder

logger = logging.getLogger(__name__)


class JSONWriter:
    @staticmethod
    def write_json(data: List[List[object]], output_path: str):
        """
        Write data to a JSON file.

        :param data: The data to write.
        :param output_path: The path to the output JSON file.
        """
        with open(output_path, 'w') as f:
            json.dump(data, f, cls=MatrixJSONEncoder, indent=2)

        logger.info(f'Hex matrix saved to {output_path}')
