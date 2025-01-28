# Global Declination Calculator

## Description

For this project I would like to create my own global declination counter. To do this I will be using the [2025 World Magnetic Model (WMM)](https://www.ncei.noaa.gov/products/world-magnetic-model). The equations I use will be motivated by the technical report in their documentation.

The process I have in mind is something to the effect of:

1. Model Implementation (spherical harmonics, coordinate transformations, calculate field components)
2. User Interface (interactive map, input fields, display of declination, and other UI ["juice"](https://garden.bradwoods.io/notes/design/juice))
3. Validation & Testing (compare to WMM calculator, error handling, uncertainty estimates, testing suite)

## Model Implementation

### Geodetic to Geocentric Coordinates

My understanding right now is that data measured from satellites is what we call geodetic. Of course this is accurate to Earth's irregular shape which is tricky to model mathematically and programatically. According to [this WMM technical report](
https://repository.library.noaa.gov/view/noaa/24390/noaa_24390_DS1.pdf) we should be treating Earth's real, irregular shape, as the [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) ellipsoid.

Therefore, any spherical harmonics we need to do we will need to use this conversion.

#### Implementation

Using equations (7) in the technical report I obtain **geocentric latitude ( &phi;' )** and **geocentric radius ( r )**. 

**&phi;'** and **r** are validated to be correct against the numerical example provided in the technical report.


