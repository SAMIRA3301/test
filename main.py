# --encoding: utf-8
"""Module for searching degree."""


def search_degree(axiliration: float, time: float, radius: float, speed: float):
    """This function searches degree.

    First, it is imported from ceil and pi from the math module,
     then the length of the circle is calculated,
     then the distance traveled is calculated,
     then the degree is returned
    Args:
        time(float): time
        axiliration(float): acceleration
        radius(float): radius
        speed(float): speed
    Returns:
        float -> degree

    """
    from math import pi, ceil
    length_circle = 2*pi*radius
    way = speed * time + (axiliration * time**2)/2
    factor = ceil(way/length_circle/360)
    return round(360*factor - way/length_circle, 2)


