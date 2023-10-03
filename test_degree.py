# --encoding: utf-8

import pytest

from main import search_degree

"""Testin search degree."""

test = [(60, 3, 5, 9, 170.92), (46, 3, 5, 7, 248.72),
        (10, 100, 2, 1000, 246.34),
        (10, 500, 2, 5000, 151.69), (17, 0, 2, 0, 0), ]


@pytest.mark.parametrize('axiliration, time, radius, speed, exp', test)
def test_degree(axiliration: float, time: float, radius: float, speed: float, exp: float):
    """ Compares the resulting value with the response.

    Args:
        :param axiliration: float
        :param time: float
        :param radius: float
        :param speed: float
        :param exp:
    :return:

    """
    assert search_degree(time, axiliration, radius, speed) == exp
