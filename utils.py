# later: expand this function to not hardcode resolutions and allow it to convert from and to any resolution
def convert_res(x: int, y: int) -> tuple:
    # decrese by -1 because it starts at 0 not 1.
    return (round(1366 / 1920 * x) - 1, round(768 / 1080 * y) - 1)
