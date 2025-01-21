import math
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

    # this might be the goofiest part of the code
    # i have a hard time believing it's more readable inline but i'll defer to the opinions of the smart people
    term0 = schmidt_semi_normalize(n, m, math.sin(mu))
    term1 = n + 1
    term2 = math.tan(mu)
    term3 = math.sqrt((term1) ** 2 - (m**2))
    term4 = 1 / (math.cos(mu))

    res = term0 * (term1 * term2 - term3 * term4)
    return res
