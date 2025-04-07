---
tags:
  - machine_learning
---
Encoding for the frequency distributions.
# Example
```python
# grouping by frequency
fq = df.groupby('nom_0').size()/len(df)
# mapping values to dataframe
df.loc[:, "{}_freq_encode".format('nom_0')] = df['nom_0'].map(fq)
# drop original column.
df = df.drop(['nom_0'], axis=1)
fq.plot.bar(stacked=True)
df.head(10)
```