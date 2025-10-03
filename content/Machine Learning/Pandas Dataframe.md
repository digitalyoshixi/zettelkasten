---
tags:
  - python
  - data_science
---
To create a data frame, we first need a dictionary with all the column values assigned to a column name. Then turn that dictionary into a pandas data frame
# Boilerplate
```python
import pandas as pd
df = pd.DataFrame()   # an empty DataFrame
# Append columns by directly assigning values
df['Name'] = None
df['Age'] = None
# Create new rows as separate DataFrames
new_row1 = pd.DataFrame({'Name': ['Charlie'], 'Age': [28]})
new_row2 = pd.DataFrame({'Name': ['David'], 'Age': [35]})

df = pd.concat([df, new_row1, new_row2], ignore_index=True) # Appending new rows using concat()
display(df)
```
# Dataframe attributes and functions

Similar to series attributes, dataframes share a bit between them.

**.head(num)** the first X rows of the dataframe

**.tail(num)** the last X rows of the dataframe

**.ndim** the dimension the database is in. only a integer

**.shape** the shape of the database

**.dtypes** the data types of EACH row

**.T** gives us a transposed version of the

**.iloc** locate from index. Allows for indexing and slicing to get a column from a columnname, you will do referencing with square brackets. To get a cell from the column, turn the column iloc then grab the square bracket reference again.
