---
tags:
  - machine_learning
aliases:
  - XGBoost
---
This is a optimized version of [[Random Forest Classification]].
- Avoids overfitting
- Newer decision trees fix the mistakes from the old ones trees
# XGBClassifier
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
# XGBRegressor
```python
from sklearn.metrics import mean_squared_error
import xgboost as xgb
from sklearn.model_selection import train_test_split

# read data
data = pd.read_csv("../Data/FID/good.csv").head(50000)
x_train, x_test, y_train, y_test = train_test_split(data.drop(columns=['ILI_CASE']), data["ILI_CASE"], test_size=.2)

bst = xgb.XGBRegressor(n_estimators=20, objective='reg:squarederror')
bst.fit(x_train,y_train)

preds = bst.predict(x_test)

print(mean_squared_error(y_test, preds))
```