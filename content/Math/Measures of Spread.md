---
tags:
  - math
aliases:
  - Percentiles
---
Where you are on a measure of 0-100% Aka Percentiles.
Like if you are in the upper quartile, lower quartile
# Percentiles
The percent of all the data that are less than or equal to a specific data value
Eg. if you are above the 80%, then you are in the top 20%
### Percentile Rank
If we were to organize our data from smallest to largest, then the percentile index(or rank) that is the start of our percentile.
e.g. for a list like [0,2,6,7,21,53], the top 70% percentile rank would be index 5.

R = p(n+1)/100
p is the percentile
n is the size of the population
R is a whole number, **always** round down
### Percentile
p = $\frac{100(L+0.5E)}{n}$
L is the number of data less than the data point
E is the number of data equal to the data point
n is the size of the population

It is impossible to have a 100 percentile. 100 means that the only data is homogenous.
