import math
import pytest
from ..calc.geodetic_to_spherical import geodetic_to_spherical

# TODO: .env this
B = 6356752.314245

test_data = [
    (-1.39626, 100000.0, -1.3951289589, 6457402.3484473705),
]


@pytest.mark.parametrize("lat, h, test_geo_lat, test_r", test_data)
def test_radius(lat, h, test_geo_lat, test_r):
    r, _ = geodetic_to_spherical(lat, h)

    assert r == pytest.approx(test_r, rel=1e-5)


@pytest.mark.parametrize("lat, h, test_geo_lat, test_r", test_data)
def test_lat(lat, h, test_geo_lat, test_r):
    _, geo_lat = geodetic_to_spherical(lat, h)
    assert geo_lat == pytest.approx(test_geo_lat, rel=1e-5)


zero_data = [(0.0, 0.0, 0.0, 6378137.0)]


@pytest.mark.parametrize("lat,h,test_geo_lat,test_r", zero_data)
def test_zeros(lat, h, test_geo_lat, test_r):
    r, geo_lat = geodetic_to_spherical(lat, h)

    assert r == pytest.approx(test_r, rel=1e-5)
    assert geo_lat == pytest.approx(test_geo_lat, rel=1e-5)


pole_data = [(math.pi / 2, 0.0, math.pi / 2, B)]


@pytest.mark.parametrize("lat,h,test_geo_lat,test_r", pole_data)
def test_pole(lat, h, test_geo_lat, test_r):
    r, geo_lat = geodetic_to_spherical(lat, h)

    assert r == pytest.approx(test_r, rel=1e-5)
    assert geo_lat == pytest.approx(test_geo_lat, rel=1e-5)
