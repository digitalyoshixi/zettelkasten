---
tags:
  - python
  - data_science
aliases:
  - Pandas Write CSV
  - Pandas Read CSV
---
```python
import pandas as pd 
# reading to csv
df = pandas.read_csv("data.csv")
smaller = df.head(10000)
print(smaller-)
# Writing csv
smaller.to_csv("pruned.csv")
```
