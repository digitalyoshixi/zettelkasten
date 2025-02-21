---
tags:
  - python
  - machine_learning
---
```python
import cv2
import numpy as np 
import pandas as pd 

img = cv2.imread(row["Path"], cv2.IMREAD_GRAYSCALE) # Grayscale
# img = cv2.imread(row["Path"], cv2.IMREAD_RGB) # RGB
print(img) # a numpy matrix
```