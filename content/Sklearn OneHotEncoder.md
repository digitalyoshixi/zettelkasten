---
tags:
  - machine_learning
  - python
---
Encoding that represents as a matrix if we are in one category or another
![[Sklearn OneHotEncoder-20250407004600089.webp]]
# Example
```python
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
# transforming the column after fitting
enc = enc.fit_transform(df[['nom_0']]).toarray()
# converting arrays to a dataframe
encoded_colm = pd.DataFrame(enc)
# concatenating dataframes
df = pd.concat([df, encoded_colm], axis=1)
# removing the encoded column.
df = df.drop(['nom_0'], axis=1)
df.head(10)
```