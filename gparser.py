import utils


def parse(file_name: str) -> str:
    final_text = ""
    with open(file_name, "r") as f:
        lines = f.readlines()
    for i in lines:
        parsed = i.split("=")
        if len(parsed) != 2:
            continue
        coordinates = parsed[1].strip().strip('"').split(",")
        converted_coordinate = utils.convert_res(
            int(coordinates[0]), int(coordinates[1])
        )
        final_text += (
            f'{parsed[0]} = "{converted_coordinate[0]},{converted_coordinate[1]}"\n'
        )
    return final_text
