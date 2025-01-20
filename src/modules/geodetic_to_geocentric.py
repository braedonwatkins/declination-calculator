import math

a = 6378137.0  # semi major axis (m)
f = 1 / 298.257223563  # flattening (f) is same as `1 - (b/a) = f`
e2 = 2 * f - f**2  # square of eccentricity (deviation from a sphere)


def geodetic_to_geocentric(
    lat: float, lon: float, alt: float
) -> tuple[float, float, float]:
    """
    Converts geodetic coordinates to geocentric / rectangular coordinates


    Parameters:
        lat (float): Latitude in degrees
        lon (float): Longitude in degrees
        alt (float): altitude in meters

    Returns:
        (x,y,z) (tuple): Geocentric coordinates in meters
    """

    lat_rad = math.radians(lat)  # phi
    lon_rad = math.radians(lon)  # lambda

    # cache trig functions to avoid recalculating
    sin_lat_rad = math.sin(lat_rad)
    cos_lat_rad = math.cos(lat_rad)
    sin_lon_rad = math.sin(lon_rad)
    cos_lon_rad = math.cos(lon_rad)

    # Prime vertical radius i.e. distance from center due to curvature
    # More intuitive but more computationally expensive definition:
    # N = a / math.sqrt((a * cos_lon_rad) **2 + (b * sin_lon_rad**2))
    N = a / math.sqrt(1 - e2 * sin_lat_rad**2)

    # these have cool derivations but i won't bloat comments with it
    x = (N + alt) * cos_lat_rad * cos_lon_rad
    y = (N + alt) * cos_lat_rad * sin_lon_rad
    z = ((1 - e2) * N + alt) * sin_lat_rad

    return (x, y, z)
