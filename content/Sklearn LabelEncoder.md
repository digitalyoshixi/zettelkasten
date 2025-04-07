---
tags:
  - math
  - python
---
# Use
```python
from sklearn.preprocessing import LabelEncoder  
le = LabelEncoder()
df['ord_2'] = le.fit_transform(df['ord_2'])
sns.set(style ="darkgrid")
sns.countplot(df['ord_2'])
```