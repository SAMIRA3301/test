# --encoding: utf-8
"""Module for searching degree."""


def search_degree(a: float, t: float, r: float, v: float):
    """This function searches degree

    First, it is imported from ceil and pi from the math module,
     then the length of the circle is calculated,
     then the distance traveled is calculated,
     then the degree is returned
    Args:
        t(float): time
        a(float): acceleration
        r(float): radius
        v(float): speed
    Returns:
        float -> degree

    """
    from math import pi, ceil
    length_circle = 2*pi*r
    way = v * t + (a * t**2)/2
    factor = ceil(way/length_circle/360)
    return round(360*factor - way/length_circle, 2)


