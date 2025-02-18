---
tags:
  - machine_learning
  - data_science
aliases:
  - SVM
---
A [[Classification Model]] that attempts to find the [[Hyperplane]] that best separates data points while maximizing margins between classes.

# [[Sci-kit Learn]] Code Snippet
```
from sklearn.svm import SVC  
# Create an SVM model  
model = SVC()  
# Fit the model to your training data  
model.fit(X_train, y_train)  
# Make predictions  
predictions = model.predict(X_test)
```