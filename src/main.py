import math
import sys
import numpy as np

from src.modules.geodetic_to_spherical import geodetic_to_spherical
from src.modules.parse_wmm import parse_wmm
from src.modules.gauss_coefficients import gauss_coefficients
from src.modules.schmidt_semi_normal import schmidt_semi_normalize
from src.modules.vector_components import vector_components

# TODO: see if these ever change
MAX_DEGREES = 12  # n
MAX_ORDER = 12  # m

# TODO: extract this from file
EPOCH = 2020.0

# TODO: const this
a = 6378137  # semi major in (m)

if __name__ == "__main__":
    print("Hello Geomagnetic World!")

    lat, lon, alt, input_time = map(float, sys.argv[1:5])
    r, geocentric_lat = geodetic_to_spherical(lat, alt)

    # print("lat, lon, alt, input", lat, lon, alt, input_time)
    # print("geo lat", geocentric_lat)
    # print("r", r)

    g_t = np.zeros((13, 13))
    h_t = np.zeros((13, 13))
    # TODO: .env this (or Py equivalent)
    g, h, g_dot, h_dot = parse_wmm(
        "/Users/braedon/noaa/declination-calculator/data/WMM2020COF/WMM.COF"
    )

    # TODO: this would be more efficient inside parse_wmm
    for n in range(MAX_DEGREES):
        for m in range(MAX_ORDER):
            g_t[n][m], h_t[n][m] = gauss_coefficients(
                g[n][m], h[n][m], g_dot[n][m], h_dot[n][m], input_time, EPOCH
            )

    # print("g_t[1][0]", g_t[1][0])
    # print("g_t[2][2]", g_t[2][2])
    # print("h_t[1][1]", h_t[1][1])
    # print("h_t[2][2]", h_t[2][2])

    x, y, z = vector_components(a, r, g_t, h_t, geocentric_lat, math.radians(lon))
    print(x, y, z)

    # test_3_0 = schmidt_semi_normalize(3, 0, math.sin(0.0))
    # print("test_3_0", test_3_0)
    # test_3_3 = schmidt_semi_normalize(3, 3, math.sin(0.0))
    # print("test_3_3", test_3_3)
