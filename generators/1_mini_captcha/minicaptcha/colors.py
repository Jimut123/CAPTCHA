'''this module make main color tint and shade then return it as hex color.'''

import typing
from random import randint


def make_Tint(color: str, percent: int) -> str:
    percent = abs(percent)
    if percent > 100:
        raise ValueError('percent must be between 0 and 100')
    color = color.lstrip('#')
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    rgb = tuple(map(lambda x: round(x + ((255 - x) * (percent/100))), rgb))
    rgb = tuple(map(lambda x: format(x, '#04x'), rgb))
    return '#' + rgb[0][2::] + rgb[1][2::] + rgb[2][2::]


def make_Shade(color: str, percent: int) -> str:

    if percent > 100:
        raise ValueError('percent must be between 0 and 100')
    color = color.lstrip('#')
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

    rgb = tuple(map(lambda x: round(x * (abs(percent) / 100)), rgb))

    rgb = tuple(map(lambda x: format(x, '#04x'), rgb))

    return '#' + rgb[0][2::] + rgb[1][2::] + rgb[2][2::]


# https://github.com/edelstone/tints-and-shades
def random_hex_color(python_hex_format=False):
    if python_hex_format == True:
        return
    return format(randint(0, 16777215), '#08x').replace('0x', '#')
