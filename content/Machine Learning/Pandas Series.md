---
tags:
  - math
  - data_science
---
# Series
### .iloc()
- How you locate a index of the series
```
ceres.iloc([index])
```
### .name
- value of the series. The name of the series becomes its index or column name when used to make a dataframe
### .count()
the length of the series in elements

### ,head(num)
Returns the first X items in the row

### .tail(num)
Returns the last X items in the row

### .apply(function)
apply the changes in the function. Like run every element in the series through that function. The function must have 1 parameter and a return value.

### .sort_index()
sort by natural index order. Just a copy, no permanent modification unless you pass parameter inplace=True

### .sort_values()
sort by natural value order. Just a copy, no permanent modification unless you pass parameter inplace=True
