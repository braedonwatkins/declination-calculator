import math

from calc.const import MAX_DEGREE
from calc.schmidt_semi_normal import (
    schmidt_semi_normalize,
    schmidt_semi_normalize_d1,
)


# TODO: obviously needs another pass for vectorization / precomputing, going for functionality first
def vector_components(a, r, g_t, h_t, phi_prime, lambda_):
    # print(a, r, phi_prime, lambda_)

    X_prime = 0.0
    Y_prime = 0.0
    Z_prime = 0.0

    for n in range(1, MAX_DEGREE + 1):
        x_cur = 0.0
        y_cur = 0.0
        z_cur = 0.0

        for m in range(0, n + 1):
            # print(f"g_{n}_{m}: {g_t[n][m]}")
            # print(f"h_{n}_{m}: {h_t[n][m]}")
            sin_phi_prime = math.sin(phi_prime)
            schmidt_d1 = schmidt_semi_normalize_d1(n, m, phi_prime, sin_phi_prime)
            schmidt = schmidt_semi_normalize(n, m, sin_phi_prime)
            # schmidt_d1 = lpmv(m, n, math.sin(phi_prime))
            # schmidt = lpmv(m, n, math.sin(phi_prime))

            m_lambda = m * lambda_

            x_cur += (
                g_t[n][m] * math.cos(m_lambda) + h_t[n][m] * math.sin(m_lambda)
            ) * schmidt_d1

            y_cur += (
                m
                * (g_t[n][m] * math.sin(m_lambda) - h_t[n][m] * math.cos(m_lambda))
                * schmidt
            )

            z_cur += (
                g_t[n][m] * math.cos(m_lambda) + h_t[n][m] * math.sin(m_lambda)
            ) * schmidt

        factor = (a / r) ** (n + 2)
        X_prime -= factor * x_cur
        Y_prime += factor * y_cur
        Z_prime -= (n + 1) * factor * z_cur

        # print(f"X' {X_prime:.2f} Y' {Y_prime:.2f} Z' {Z_prime:.2f}")

    Y_prime *= 1 / math.cos(phi_prime)

    return X_prime, Y_prime, Z_prime
