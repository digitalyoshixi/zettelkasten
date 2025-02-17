---
tags:
  - python
  - data_science
---
### Aggregate functions

All for dataframes

**.count()** returns the count of the number of elements in each row.

**.sum()** returns the summed rows. String rows concatenate, number rows addition, bool rows, well, bools are converted to ints then added

**.prod()** returns the product rows. Cannot work if there are strings.

you can also use these for regular series aswell.

  

### Statistical functions

**.mean()** gets the average granted there is no string rows

**.median()** middle element good if you have a lot of outliers

**.mode()** value that occurs most often

**.std()** standard deviation. How much do the values tend to deviate from the mean

**.max()** return maximum number

**.min()** return minimum number

**.describe()** a description of all previously mentioned statistics.