# gparser.py
# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.


import utils
import logging
import time


def parse(file_name: str, from_res: tuple, to_res: tuple) -> str:
    final_text = ""
    with open(file_name, "r") as f:
        lines = f.readlines()
    logging.info(
        f"Parsing {file_name} with {len(lines)} entries: from: {from_res} to: {to_res}."
    )
    start = time.perf_counter_ns()
    for i in lines:
        parsed = i.split("=")
        if len(parsed) != 2:
            continue
        coordinates = parsed[1].strip().strip('"').split(",")
        converted_coordinate = utils.convert_res(
            int(coordinates[0]), int(coordinates[1]), from_res, to_res
        )
        final_text += (
            f'{parsed[0]} = "{converted_coordinate[0]},{converted_coordinate[1]}"\n'
        )
    logging.info(
        f"parse complete: took {(time.perf_counter_ns() - start) / 1000000} milliseconds"
    )
    return final_text
