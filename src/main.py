from modules.geodetic_to_geocentric import geodetic_to_geocentric
import sys

if __name__ == "__main__":
    print("Hello Geomagnetic World!")

    lat, long, alt = map(float, sys.argv[1:4])
    print(geodetic_to_geocentric(lat, long, alt))
