# --encoding: utf-8

import pytest

from main import search_degree

"""Testin search degree"""

test = [(60, 3, 5, 9, 170.92), (46, 3, 5, 7, 248.72),
        (10, 100, 2, 1000, 246.34),
        (10, 500, 2, 5000, 151.69), (17, 0, 2, 0, 0), ]


@pytest.mark.parametrize('a, t, r, v, exp', test)
def test_degree(a: float, t: float, r: float, v: float, exp: float):
    """ Compares the resulting value with the response
    Args:
        :param a: float
        :param t: float
        :param r: float
        :param v: float
        :param exp:
    :return:

    """
    assert search_degree(t, a, r, v) == exp
