def gauss_coefficients(
    g: float, h: float, g_dot: float, h_dot: float, t: float, t0: float
) -> tuple[float, float]:

    delta_t = t - t0

    g_t = g + delta_t * g_dot
    h_t = h + delta_t * h_dot

    return g_t, h_t
