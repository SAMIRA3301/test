# --encoding: utf-8
"""Module for searching degree."""
from math import pi, ceil


def search_degree(axiliration: float, time: float, radius: float, speed: float):
    """Function is searching degree.

    First, it is imported from ceil and pi from the math module,
    then the length of the circle is calculated,
    then the distance traveled is calculated,
    then the degree is returned

    Args:
        time: float
        axiliration: float
        radius: float
        speed: float
    Returns:
        :return float

    """
    const_rad = 360
    length_circle = 2 * pi * radius
    way = speed * time + (axiliration * time ** 2) / 2
    factor = ceil(way / length_circle / const_rad)
    return round(const_rad * factor - way / length_circle, 2)
