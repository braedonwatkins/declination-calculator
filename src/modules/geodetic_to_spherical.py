import math

a = 6378137.0  # semi major axis (m)
f = 1 / 298.257223563  # flattening (f) is same as `1 - (b/a) = f`
e2 = 2 * f - f**2  # square of eccentricity (deviation from a sphere)


def geodetic_to_spherical(lat: float, alt: float) -> tuple[float, float]:
    """
    Converts geodetic coordinates to geocentric spherical radius and latitude


    Parameters:
        lat (float): Latitude in degrees
        alt (float): altitude in meters

    Returns:
        (r, geocentric_lat) (tuple): Geocentric spherical radius and latitude
    """

    lat_rad = math.radians(lat)  # phi

    # cache trig functions to avoid recalculating
    sin_lat_rad = math.sin(lat_rad)
    cos_lat_rad = math.cos(lat_rad)

    # Prime vertical radius i.e. distance from center due to curvature
    N = a / math.sqrt(1 - e2 * sin_lat_rad**2)

    # just in case, here's the other geocentric coords
    # x = (N + alt) * cos_lat_rad * cos_lon_rad
    # y = (N + alt) * cos_lat_rad * sin_lon_rad

    z = ((1 - e2) * N + alt) * sin_lat_rad
    p = (N + alt) * cos_lat_rad  # eq to math.sqrt(x**2 + y**2)
    r = math.sqrt(p**2 + z**2)
    geocentric_lat = math.asin(z / r)

    return (r, geocentric_lat)
