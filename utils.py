def convert_res(x: int, y: int, from_res: tuple, to_res: tuple) -> tuple:
    # decrese by -1 because it starts at 1 not 0.
    return (round(to_res[0] / from_res[0] * x) - 1, round(to_res[1] / from_res[1] * y) - 1)


def write_file(path, text):
    with open(path, "w") as fil:
        fil.write(text)
