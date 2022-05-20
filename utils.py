#    Gc resizer, A program to change resolution coordinates for a golden cursor file.

#    Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi 

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
