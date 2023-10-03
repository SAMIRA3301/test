"""Module for searching degree."""


def search_degree(t: float, a: float, r: float, v: float) -> float:
    """This function searches degree

    Args:
        t(float): time
        a(float): acceleration
        r(float): radius
        v(float): speed
    Returns:
        float -> degree

    """
    from math import pi
    length_circle = 2*pi*r
    way = v * t + (a * t**2)/2
    return 360 - way/length_circle
