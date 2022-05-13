import decimal
from decimal import Decimal
import string

decimal.getcontext().prec = 24
MAXPLACE = Decimal(10) ** -20


def convert_res(x: int, y: int, from_res: tuple, to_res: tuple) -> tuple:
    # decrease by -1 because it starts at 1 not 0.
    f_x = Decimal(to_res[0] - 1) / Decimal(from_res[0] - 1)
    f_y = Decimal(to_res[1] - 1) / Decimal(from_res[1] - 1)
    f_x = f_x.quantize(MAXPLACE)
    f_y = f_y.quantize(MAXPLACE)
    return (round(Decimal(x) * f_x), round(Decimal(y) * f_y))


def write_file(path, text):
    with open(path, "w") as fil:
        fil.write(text)


def clean_str(text):
    # remove all non number characters in a string.
    return "".join([i for i in text if i in string.digits or i == " "]).strip()
