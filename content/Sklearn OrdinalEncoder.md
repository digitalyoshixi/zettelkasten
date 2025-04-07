---
tags:
  - machine_learning
  - python
---
Ensures [[Ordinal Encoding]].
# Example
```python
from sklearn.preprocessing import OrdinalEncoder
ord1 = OrdinalEncoder()
# fitting encoder
ord1.fit([df['ord_2']])
# transforming the column after fitting
df["ord_2"] = ord1.transform(df[["ord_2"]])
df.head(10)
```