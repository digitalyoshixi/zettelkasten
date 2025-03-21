---
tags:
  - machine_learning
aliases:
  - XGBoost
---
This is a optimized version of [[Random Forest Classification]].
- Avoids overfitting
- Newer decision trees fix the mistakes from the old ones trees
# Using with [[Sci-kit Learn]]
```python
from xgboost import XGBClassifier
# read data
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=.2)
# create model instance
bst = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1, objective='binary:logistic')
# fit model
bst.fit(X_train, y_train)
# make predictions
preds = bst.predict(X_test)
```