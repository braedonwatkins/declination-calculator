import math
import numpy as np
import pytest
import warnings
from hypothesis import given, strategies as st
from scipy.special import lpmv


# TODO: Docstring both of these...
def schmidt_semi_normalize(n: int, m: int, mu: float) -> float:
    if m == 0:
        normalization = 1.0
    elif m > 0:
        normalization = math.sqrt(2.0 * math.factorial(n - m) / math.factorial(n + m))
    else:
        raise Exception()  # TODO: handle this, though who would input m < 0? corrupted files maybe

    legendre = lpmv(m, n, mu)

    # NOTE: this cancels the Condon-Shortley Phase!!!
    if m % 2 == 1:
        legendre *= -1.0

    # print(n, m, normalization, legendre)
    return normalization * legendre


def schmidt_semi_normalize_d1(n: int, m: int, phi: float, mu: float) -> float:
    legendre_cur = schmidt_semi_normalize(n, m, mu)
    legendre_next = schmidt_semi_normalize(n + 1, m, mu)

    term1 = (n + 1) * math.tan(phi) * legendre_cur
    term2 = math.sqrt((n + 1) ** 2 - m**2) * (1 / math.cos(phi)) * legendre_next

    return term1 - term2
