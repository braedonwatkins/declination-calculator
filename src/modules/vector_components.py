import math
from src.modules.schmidt_semi_normal import (
    schmidt_semi_normalize,
    schmidt_semi_normalize_d1,
)


def vector_components(a, r, g_t, h_t, phi_prime, lambda_):
    # print(n, m, a, r, phi_prime, lambda_)

    X_prime = 0.0
    Y_prime = 0.0
    Z_prime = 0.0

    for n in range(1, 13):
        factor = (a / r) ** (n + 2)

        for m in range(0, n + 1):
            schmidt_d1 = schmidt_semi_normalize_d1(n, m, math.sin(phi_prime))
            schmidt = schmidt_semi_normalize(n, m, math.sin(phi_prime))

            X_prime += (
                factor
                * (
                    g_t[n][m] * math.cos(m * lambda_)
                    + h_t[n][m] * math.sin(m * lambda_)
                )
                * schmidt_d1
            )

            Y_prime += (
                factor
                * m
                * (
                    g_t[n][m] * math.sin(m * lambda_)
                    - h_t[n][m] * math.cos(m * lambda_)
                )
                * schmidt
            )

            Z_prime += (
                (n + 1)
                * factor
                * (
                    g_t[n][m] * math.cos(m * lambda_)
                    + h_t[n][m] * math.sin(m * lambda_)
                )
                * schmidt
            )

    X_prime *= -1.0
    Y_prime *= 1 / math.cos(phi_prime)
    Z_prime *= -1.0

    return X_prime, Y_prime, Z_prime
