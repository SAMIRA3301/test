# --encoding: utf-8


def search_degree(t: float, a: float, r: float, v: float):
    from math import pi
    length_circle = 2*pi*r
    way = v * t + (a * t**2)/2
    return 360 - way/length_circle


print(search_degree(60, 3, 5, 9))
