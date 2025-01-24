import math

a = 6378137.0  # semi major axis (m)
f = 1 / 298.257223563  # flattening (f) is same as `1 - (b/a) = f`
e2 = 2 * f - f**2  # square of eccentricity (deviation from a sphere)


# TODO: Check for any math footguns div by 0, inefficiencies, etc.
def geodetic_to_spherical(lat: float, h: float) -> tuple[float, float]:
    """
    Converts geodetic coordinates to geocentric spherical radius and latitude


    Parameters:
        lat (float): Latitude in degrees
        h (float): altitude in meters

    Returns:
        (r, geocentric_lat) (tuple(float)): Geocentric spherical radius and latitude
    """

    # Prime vertical radius i.e. distance from center due to curvature
    R = a / math.sqrt(1 - e2 * math.sin(lat) ** 2)

    # just in case, here's the other geocentric coords
    # x = (N + h) * cos_lat * cos_lon_rad
    # y = (N + h) * cos_lat * sin_lon_rad
    p = (R + h) * math.cos(lat)  # eq to math.sqrt(x**2 + y**2)
    z = (R * (1 - e2) + h) * math.sin(lat)
    r = math.sqrt(p**2 + z**2)

    geocentric_lat = math.asin(z / r)

    return (r, geocentric_lat)
