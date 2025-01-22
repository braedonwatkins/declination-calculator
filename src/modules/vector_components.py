import math
from src.modules.schmidt_semi_normal import (
    schmidt_semi_normalize,
    schmidt_semi_normalize_d1,
)


# TODO: obviously needs another pass for vectorization / precomputing, going for functionality first
def vector_components(a, r, g_t, h_t, phi_prime, lambda_):
    # print(n, m, a, r, phi_prime, lambda_)

    X_prime = 0.0
    Y_prime = 0.0
    Z_prime = 0.0

    for n in range(1, 13):
        factor = (a / r) ** (n + 2)

        # print(f"\nFor n={n}:")
        # print(f"factor = {factor}")

        for m in range(0, n + 1):
            schmidt_d1 = schmidt_semi_normalize_d1(n, m, math.sin(phi_prime))
            schmidt = schmidt_semi_normalize(n, m, math.sin(phi_prime))

            print(f"n={n}, m={m}:")
            print(f"  schmidt = {schmidt}")
            print(f"  schmidt_d1 = {schmidt_d1}")

            # print(f"\n  For m={m}:")
            # print(f"  schmidt_d1 = {schmidt_d1}")
            # print(f"  schmidt = {schmidt}")
            # print(f"  cos(m*lambda) = {math.cos(m*lambda_)}")
            # print(f"  sin(m*lambda) = {math.sin(m*lambda_)}")
            # print(f"  g_t[n][m] = {g_t[n][m]}")
            # print(f"  h_t[n][m] = {h_t[n][m]}")

            x_cur = (
                factor
                * (
                    g_t[n][m] * math.cos(m * lambda_)
                    + h_t[n][m] * math.sin(m * lambda_)
                )
                * schmidt_d1
            )
            y_cur = (
                factor
                * m
                * (
                    g_t[n][m] * math.sin(m * lambda_)
                    - h_t[n][m] * math.cos(m * lambda_)
                )
                * schmidt
            )
            z_cur = (
                (n + 1)
                * factor
                * (
                    g_t[n][m] * math.cos(m * lambda_)
                    + h_t[n][m] * math.sin(m * lambda_)
                )
                * schmidt
            )

            X_prime += x_cur
            Y_prime += y_cur
            Z_prime += z_cur

            # print(f"\n  m={m}:")
            # print(f"  Current terms: X={x_cur:.2f}, Y={y_cur:.2f}, Z={z_cur:.2f}")
            # print(
            #     f"  Running totals: X={X_prime:.2f}, Y={Y_prime:.2f}, Z={Z_prime:.2f}"
            # )

    # print(f"X_prime = {X_prime}")
    # print(f"Y_prime = {Y_prime}")
    # print(f"Z_prime = {Z_prime}")
    X_prime *= -1.0
    Y_prime *= 1 / math.cos(phi_prime)
    Z_prime *= -1.0

    return X_prime, Y_prime, Z_prime
