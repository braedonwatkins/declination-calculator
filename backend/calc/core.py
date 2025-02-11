import math
import numpy as np
from pathlib import Path

from ..calc.const import *
from dotenv import load_dotenv
import os

load_dotenv()

from ..utils.parse_wmm import parse_wmm
from ..calc.geodetic_to_spherical import geodetic_to_spherical
from ..calc.gauss_coefficients import gauss_coefficients
from ..calc.vector_components import vector_components
from ..my_types import FieldVector


def field_vector(lat: float, lon: float, alt: float, input_time: float) -> FieldVector:

    lat_rad, lon_rad = math.radians(lat), math.radians(lon)

    r, geocentric_lat = geodetic_to_spherical(lat_rad, alt)

    # print("lat, lon, alt, input", lat, lon, alt, input_time)
    # print("geo lat", geocentric_lat)
    # print("r", r)

    g_t = np.zeros((MAX_DEGREE + 1, MAX_ORDER + 1))
    h_t = np.zeros((MAX_DEGREE + 1, MAX_ORDER + 1))

    # if env is set up will grab that path, otherwise assume unaltered in ./data/
    script_dir = Path(__file__).parent.parent
    implicit_path = str(script_dir / "data" / f"WMM{int(EPOCH)}COF/WMM.COF")
    explicit_path = os.getenv("DATA_PATH")

    g, h, g_dot, h_dot = parse_wmm(explicit_path if explicit_path else implicit_path)

    # TODO: just define the whole loop in guass coefficients file
    for n in range(1, MAX_DEGREE + 1):
        for m in range(0, n + 1):
            g_t[n][m], h_t[n][m] = gauss_coefficients(
                g[n][m], h[n][m], g_dot[n][m], h_dot[n][m], input_time, EPOCH
            )
            # print(f"n={n}, m={m}: g={g[n][m]}, h={h[n][m]}")
            # g_t[n][m] = g[n][m]
            # h_t[n][m] = h[n][m]

    x_prime, y_prime, z_prime = vector_components(
        A, r, g_t, h_t, geocentric_lat, lon_rad
    )

    # #NOTE: secular components... break this to its own function, maybe
    # x_dot_prime, y_dot_prime, z_dot_prime = vector_components(
    #     a, r, g_dot, h_dot, geocentric_lat, lon_rad
    # )
    # x_dot = x_dot_prime * math.cos(geocentric_lat - lat_rad) - z_dot_prime * math.sin(
    #     geocentric_lat - lat_rad
    # )
    # y_dot = y_dot_prime
    # z_dot = z_dot_prime * math.sin(geocentric_lat - lat_rad) + z_dot_prime * math.cos(
    #     geocentric_lat - lat_rad
    # )

    x = x_prime * math.cos(geocentric_lat - lat_rad) - z_prime * math.sin(
        geocentric_lat - lat_rad
    )
    y = y_prime
    z = x_prime * math.sin(geocentric_lat - lat_rad) + z_prime * math.cos(
        geocentric_lat - lat_rad
    )
    # print(f"X {x:.2f} Y {y:.2f} Z {z:.2f}")

    H = np.sqrt(x**2 + y**2)
    F = np.sqrt(H**2 + z**2)
    I = np.arctan(z / H)
    D = np.arctan(y / x)
    # print("declination?", D)

    fieldVector = FieldVector(x, y, z, H, F, I, D)

    return fieldVector
