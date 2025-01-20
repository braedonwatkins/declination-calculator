# Global Declination Calculator

## Description

For this project I would like to create my own global declination counter. To do this I will be using the [2025 World Magnetic Model (WMM)](https://www.ncei.noaa.gov/products/world-magnetic-model).

The process I have in mind is something to the effect of:

1. Model Implementation (spherical harmonics, coordinate transformations, calculate field components)
2. User Interface (interactive map, input fields, display of declination, and other UI ["juice"](https://garden.bradwoods.io/notes/design/juice))
3. Validation & Testing (compare to WMM calculator, error handling, uncertainty estimates, testing suite)

## Model Implementation

- started by creating a util module for converting geodetic coordinates to geocentric
    - note to self: e is used to resemble eccentricity in these equations *not*euler's number!

### Geodetic to Geocentric

My understanding right now is that data measured from satellites is what we call geodetic. Of course this is accurate to Earth's irregular shape which is tricky to model mathematically and programatically. According to [this WMM technical report](
https://repository.library.noaa.gov/view/noaa/24390/noaa_24390_DS1.pdf) we should be treating Earth's real, irregular shape, as the [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) ellipsoid.

Therefore, any spherical harmonics or spherical approximations we need to do we will need to use this conversion.

## PREV: Intermag Data Pipeline

### Description

This was an attempt at writing my own data pipeline for Intermag data. However, it was a challenge getting my hands on relevant data so I've pivoted.

I'm keeping it here as a record of what I attempted in case anyone else would like to try in the future.

### Data Collection

The first step of course is to collect some data to compile this source of truth into. 

#### Intermag FTP

The first attempt was [Intermag](https://intermagnet.org/faq/02.how-do-I-get-realtime-data.html) which suggests to FTP. 

However, this data source appears to consistently disconnect. It appears that the documentation hasn't caught up but there is some reference [elsewhere](https://intermagnet.org/meetings/2023May-Sopron/INTERMAGNETMeetingMinutes-SopronMay2023-Public.pdf) that this now requires credentials. While I could attempt to get credentials, as I'm not using this for commercial purposes, I suspect this will take a while so I moved on.

There is no reference of an Intermag API that I could find. That sucked. 

#### NGDC FTP

It looks like there is some FTP stuff available [here](ftp://ftp.ngdc.noaa.gov/wdc/geomagnetism/data/observatories/definitive). However, there are two problems:

1. It seems severely dated. Everything comes up as created in 2008.
2. The directories are cryptic and unlabeled. They are all either 3 letter abbreviations or just automated names. This is making it challenging to understand what all is in here.

For now, I am moving on from this source but it could be worth coming back to.

#### SGAS FTP

For whatever reason I had [this FTP link](ftp.swpc.noaa.gov/pub/warehouse) in my terminal history. Gave it a shot and found some SGAS data.

However, the extent of geomagnetic data I could gather was qualitative i.e. `The geomagnetic field was quiet` which is not quite what I'm looking for. 

