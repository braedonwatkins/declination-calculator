import math
import numpy as np
import pytest
import warnings
from hypothesis import given, strategies as st
from scipy.special import lpmv

# TODO: Docstring both of these... maybe?


def schmidt_semi_normalize(n: int, m: int, mu: float) -> float:
    if m > 0:
        numerator = math.factorial(n - m)
        denomenator = math.factorial(n - m)
        legendre = lpmv(n, m, mu)

        return math.sqrt(2 * (numerator / denomenator)) * legendre
    else:
        return 0.0


def schmidt_semi_normalize_d1(n: int, m: int, mu: float) -> float:
    legendre_cur = schmidt_semi_normalize(n, m, mu)
    legendre_next = schmidt_semi_normalize(n + 1, m, mu)

    return (n + 1) * (
        math.tan(mu) * legendre_cur
        - math.sqrt((n + 1) ** 2 - m**2) * (1 / math.cos(mu)) * legendre_next
    )


# an attempt at testing
# def test_known_values():
#     """Test against known values for simple cases"""
#     # Test P₀⁰(x) = 1
#     assert abs(schmidt_semi_normalize(0, 0, 0.0) - 1.0) < 1e-10

#     # Test P₁⁰(x) = x
#     test_points = [-0.5, 0.0, 0.5]
#     for x in test_points:
#         assert abs(schmidt_semi_normalize(1, 0, x) - x) < 1e-10


# @given(
#     st.integers(min_value=0, max_value=5),  # n
#     st.integers(min_value=0, max_value=3),  # m
#     st.floats(min_value=-0.99, max_value=0.99),  # mu
# )
# def test_property_based(n, m, mu):
#     """Property-based testing using Hypothesis"""
#     if m <= n:  # Valid input condition
#         with warnings.catch_warnings():
#             warnings.simplefilter("ignore")
#             result = schmidt_semi_normalize(n, m, mu)
#             assert not math.isnan(result)
#             assert not math.isinf(result)


# def test_symmetry():
#     """Test symmetry properties of the functions"""
#     n, m = 2, 1
#     test_points = np.linspace(-0.99, 0.99, 10)
#     for mu in test_points:
#         # Test that P_n^m(μ) = (-1)^m P_n^m(-μ) for even n
#         if n % 2 == 0:
#             val_pos = schmidt_semi_normalize(n, m, mu)
#             val_neg = schmidt_semi_normalize(n, m, -mu)
#             assert abs(val_pos - ((-1) ** m * val_neg)) < 1e-10


# def test_orthogonality():
#     """Test orthogonality relations"""
#     n1, n2 = 2, 3
#     m = 1
#     # Integrate P_n1^m * P_n2^m over [-1, 1]
#     x = np.linspace(-0.99, 0.99, 1000)
#     dx = x[1] - x[0]
#     integrand = [
#         schmidt_semi_normalize(n1, m, mu) * schmidt_semi_normalize(n2, m, mu)
#         for mu in x
#     ]
#     integral = sum(integrand) * dx
#     assert abs(integral) < 1e-2  # Should be close to 0 for n1 ≠ n2


# def test_edge_cases():
#     """Test edge cases and error conditions"""
#     # Test m = 0 case
#     assert abs(schmidt_semi_normalize(1, 0, 0.5) - lpmv(0, 1, 0.5)) < 1e-10

#     # Test that m > n raises appropriate error or returns valid result
#     with pytest.raises(ValueError):
#         schmidt_semi_normalize(1, 2, 0.5)

    # this might be the goofiest part of the code
    # i have a hard time believing it's more readable inline but i'll defer to the opinions of the smart people
    term0 = schmidt_semi_normalize(n, m, math.sin(mu))
    term1 = n + 1
    term2 = math.tan(mu)
    term3 = math.sqrt((term1) ** 2 - (m**2))
    term4 = 1 / (math.cos(mu))

    res = term0 * (term1 * term2 - term3 * term4)
    return res
