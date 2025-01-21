from modules.geodetic_to_spherical import geodetic_to_spherical
import sys

from src.modules.geodetic_to_spherical import geodetic_to_spherical

if __name__ == "__main__":
    print("Hello Geomagnetic World!")

    lat, alt = map(float, sys.argv[1:3])
    print(geodetic_to_spherical(lat, alt))
