# Global Declination Calculator

## Description

For this project I would like to create my own global declination counter. To do this I will be using the [2025 World Magnetic Model (WMM)](https://www.ncei.noaa.gov/products/world-magnetic-model). The equations I use will be motivated by the technical report in their documentation.

I may refer to a *numerical example* or *equation numbers* which are found in the World Magnetic Model Technical Report.

The process I have in mind is something to the effect of:

1. Model Implementation (spherical harmonics, coordinate transformations, calculate field components)
2. User Interface (interactive map, input fields, display of declination, and other UI ["juice"](https://garden.bradwoods.io/notes/design/juice))
3. Validation & Testing (compare to WMM calculator, error handling, uncertainty estimates, testing suite)

## Model Implementation

### Inputs

The code I wrote takes in three arguments **latitude (*&phi;*))**, **longitude (*&lambda;*))**, and **height (*h*))** such that lat. and lon. are measured in degrees and height is measured in meters above sea level. 

I then convert lat. and lon. to radians and keep height as-is. Note, there is a section in the report that defines height as Height Above Epsilloid (HAE) but the paper admits that the difference between this and Mean Sea Level (MSL) height will only produce error within 0.1 nT so I chose to ignore it for now.

Comparing these values to the numerical example my input is valid. 

### Geodetic to Geocentric Coordinates

My understanding right now is that data measured from satellites is what we call geodetic. Of course this is accurate to Earth's irregular shape which is tricky to model mathematically and programatically. According to [this WMM technical report](
https://repository.library.noaa.gov/view/noaa/24390/noaa_24390_DS1.pdf) we should be treating Earth's real, irregular shape, as the [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) ellipsoid.

Therefore, any spherical harmonics we need to do we will need to use this conversion.

#### Implementation

Using equations (7) in the technical report I obtain **geocentric latitude ( *&phi;*' )** and **geocentric radius ( *r* )**. 

I validated ***&phi;'*** and ***r*** against the numerical example. 

### Gaussian Coefficients

The next step is to read in the coefficients from the WMM and apply some linear interpolation w.r.t. time ***t***. I can't say I totally understand the motivation behind this step but you don't need to build a hammer to use it :p

#### Implementation

Using equation (9) I iterated through all elements of the *n x m* array and applied the linear interpolation.

I validated **g(*n,m,t*)** and **h(*n,m,t*)** for `n = 1,2` `m = 1,2` and `t = 2022.5` against the numerical example.

### Field Vector Components

When validating against the WMM I was able to get correct results within a reasonable margin $\pm 0.5$% for field vector components ***X'***, ***Y'***, and ***Z'***. The following was my approach.

> [!WARNING] 
> The scipy library function `lpmv()` assumes a Condon-Shortley Phase factor which will undoubtedly skew your results.

#### Associated Legendre Functions

Using the python library scipy I was able to calculate the Associated Legendre functions with `scipy.lpmv(m,n,mu)`.

The technical report doesn't give solutions to any associated legendre functions. However, they do provide the generated functions for `n = 3` and `m=1,2,3`. I analytically solved these and compared to `scipy.lpmv(m,n,mu)`. 

The solutions were correct for `m=2,3` but was incorrect for `m=1`.

I traced this to the textbook source (*Heiskanen and Moritz, 1967*) where they suggest:

$$ P_{3,1}(\cos(\theta)) = \sin(\theta) ( \frac{15}{2} \cos^2 (\theta) - \frac{3}{2} ) $$

While I thought this was errata, it was actually the first sign that the Condon-Shortley term was the issue, had I known what that was and the context of its existence.

#### Schmidt Semi-Normalization

The schmidt semi-normalization described in the technical report was trivial enough to implement. 

Given that the Schmidt Semi-Normalization for ***X'*** is more complex I turned my attention to validating for ***Y'*** and ***Z'***. Since there were no values provided I analytically solved for `n=3` and `m=1,2,3`. 

Given my analytical solution for $\bar{P}_n^m(\sin(\phi'))$ where `n=3` and `m=1,2,3` my code appears to solve the schmidt normalization correctly.

#### Magnetic Potential

Given equation  (12) which defines ***Z'*** in terms of $\bar{P}_n^m(\sin(\phi'))$ I was able to analytically solve for `n=3` and `m=1,2,3`. 
For these inputs, my code output is valid.

##### Before LPMV Correction 

However, the total sum that produces ***Z'*** was incorrect by a large margin for many inputs, including the numerical example. Similarly, my ***X'*** and ***Y'*** was also incorrect by a large margin.

##### After LPMV Correction

I discovered the root of my error was the Condon-Shortley Phase term assumed in `scipy.lpmv()`. Once I accounted for this the large margin of error was corrected. 

### Conclusion

Currently I am still observing relatively small amounts of error $\pm 0.5$%. I assume these are the results of rounding errors since the technical document seems to state no more than 0.1nT of error which is much smaller.

I won't worry about this too much at the moment while I work on the UI just to have something presentable in a reasonable timeline but I do intend on coming back to it to increase accuracy.

## Web Frontend

TBA
