import math
import sys
import numpy as np
from scipy.special import lpmv
from pathlib import Path

from src.modules.geodetic_to_spherical import geodetic_to_spherical
from src.modules.parse_wmm import parse_wmm
from src.modules.gauss_coefficients import gauss_coefficients
from src.modules.schmidt_semi_normal import schmidt_semi_normalize
from src.modules.vector_components import vector_components

# TODO: .env or otherwise source these
MAX_DEGREES = 12  # n
MAX_ORDER = 12  # m
EPOCH = 2020.0
a = 6378137  # semi major in (m)

if __name__ == "__main__":
    print("Hello Geomagnetic World!")

    lat, lon, alt, input_time = map(float, sys.argv[1:5])
    lat_rad, lon_rad = math.radians(lat), math.radians(lon)
    r, geocentric_lat = geodetic_to_spherical(lat_rad, alt)

    # print("lat, lon, alt, input", lat, lon, alt, input_time)
    # print("geo lat", geocentric_lat)
    # print("r", r)

    g_t = np.zeros((13, 13))
    h_t = np.zeros((13, 13))

    script_dir = Path(__file__).parent.parent
    file_path = script_dir / "data" / "WMM2020COF/WMM.COF"
    g, h, g_dot, h_dot = parse_wmm(str(file_path))

    # TODO: this would be more efficient inside parse_wmm
    for n in range(1, MAX_DEGREES + 1):
        for m in range(0, n + 1):
            g_t[n][m], h_t[n][m] = gauss_coefficients(
                g[n][m], h[n][m], g_dot[n][m], h_dot[n][m], input_time, EPOCH
            )
            # print(f"n={n}, m={m}: g={g[n][m]}, h={h[n][m]}")
            # g_t[n][m] = g[n][m]
            # h_t[n][m] = h[n][m]

    # print("g_t[1][0]", g_t[1][0])
    # print("g_t[2][2]", g_t[2][2])
    # print("h_t[1][1]", h_t[1][1])
    # print("h_t[2][2]", h_t[2][2])

    x, y, z = vector_components(a, r, g_t, h_t, geocentric_lat, lon_rad)
    print(x, y, z)

    # print(lpmv(3, 3, math.sin(math.pi / 2)))
