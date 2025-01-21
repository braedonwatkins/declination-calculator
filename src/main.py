import sys
import numpy as np

from modules.geodetic_to_spherical import geodetic_to_spherical
from modules.parse_wmm import parse_wmm
from modules.gauss_coefficients import gauss_coefficients

# TODO: see if these ever change
MAX_DEGREES = 12  # n
MAX_ORDER = 12  # m

# TODO: extract this from file
EPOCH = 2025.0

if __name__ == "__main__":
    print("Hello Geomagnetic World!")

    # TODO: .env this (or Py equivalent)
    g, h, g_dot, h_dot = parse_wmm(
        "/Users/braedon/noaa/declination-calculator/data/WMM2025COF/WMM.COF"
    )

    # input_time = float(input("Enter Year as Float: "))

    g_t = np.zeros((13, 13))
    h_t = np.zeros((13, 13))

    for i in range(MAX_DEGREES):
        for j in range(MAX_ORDER):
            g_t[i][j], h_t[i][j] = gauss_coefficients(
                g[i][j], h[i][j], g_dot[i][j], h_dot[i][j], 2025.0, EPOCH
            )

    # np.set_printoptions(precision=2, suppress=True)
    # print(np.array_str(g_t))

    # lat, alt = map(float, sys.argv[1:3])
    # print(geodetic_to_spherical(lat, alt))
