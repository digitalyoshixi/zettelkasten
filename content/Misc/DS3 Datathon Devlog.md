---
tags:
  - hackathons
---
This is my very first datathon, I know a little bit about machine learning
# Day 1 - Car Evaluation
1. We spun up a simple sklearn random forest classifier
2. We tweaked the parameters of random forest classifier to use a higher number of decision tree and reached an accuracy of 99.8%
3. Another team member used [[eXtreme Gradient Boosting|XGBoost]] and got 100%
# Day 2 - Accident Classification
1. We used the same random forest classification model, testing it on the newer with some irrelevant columns dropped that we knew were irrelevant (note we did not go through full data sanitization at this point, we just wanted  a trial run to see how well random forest performs)
2. Score of 91%-ish
3. Testing on [[Support Vector Machines|SVM]], we got 82.5%, so random forest is still the way to go
4. Tested for each column to see if removing it would increase accuracy, our final drop and keep column list was this:
```python
df.drop(columns=["ID", "Zipcode", "Country", "Start_Lat", "Start_Lng", "End_Lat", "End_Lng", "Weather_Timestamp", "Street", "City", "Country", "Nautical_Twilight", "Astronomical_Twilight", "Turning_Loop"])

goodcals = ["Severity", "Distance(mi)", "Temperature(F)", "Humidity(%)", "Pressure(in)", "Visibility(mi)", "Wind_Speed(mph)", "Precipitation(in)"]
```
5. Ran an outlier script to remove the datapoints that are 3 standard deviations away from the median.
6. Switched to [[LightBGM]] model, which ran really really really fast!
7. Final accuracy was like 96%
# Day 3 - Fungi Classification
At this point in time, I started waking up pretty damn late. Like 12pm midday
1. We started with a convolutional neural network using MobileNetV2
2. Running the model, we got a output that seemed really bad. It was classifying 95% of the testing data as class 2.
3. A hint was given on the discord that we should be using feature classifcation ![[DS3 Datathon Devlog-20250219185949845.webp]]
4. Created an excalidraw canvas to outline which mushrooms have which key features so that we have a better understanding of which mushrooms have which features
   ![[DS3 Datathon Devlog-20250219210732359.webp]]
https://excalidraw.com/#json=DOyZdcKVawY2DGbX2nlpV,H6whZTYreGNEgTQDCk6q5w
1. I also used stegonline, to see if it could better make out some details as the images for category 1 and category 3 are very noisy
   ![[DS3 Datathon Devlog-20250219190943239.webp]]
6. Also, turning images into grayscale helps define details a lot nicer.
   ![[DS3 Datathon Devlog-20250219192535513.webp]]
7. Gaussian blur was suggested, I do like this idea since it makes detail more clear, but we have to make sure that it does not over-blur
   ![[DS3 Datathon Devlog-20250219193122292.webp]]
8. There is a way to get features with [[OpenCV]], here is our code. We get stuff like this:
   ![[DS3 Datathon Devlog-20250219210554882.webp]]
```python
import pandas as pd
import numpy as np
import cv2 # added for image preprocessing
from keras._tf_keras.keras.preprocessing.image import imagedatagenerator, load_img, img_to_array
from tqdm import tqdm # for progress bar
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import labelencoder

def preprocess_image(image_path):
"""loads and preprocesses an image: converting to grayscale, resizing, normalizing, and applying edge detection."""

img = cv2.imread(image_path, cv2.imread_grayscale) # load image in grayscale

img = cv2.resize(img, (224, 224)) # resize image

# apply contrast limited adaptive histogram equalization (clahe)

clahe = cv2.createclahe(cliplimit=2.0, tilegridsize=(8, 8))

img = clahe.apply(img)

# apply gaussian blur to reduce noise

img = cv2.gaussianblur(img, (3, 3), 0)
  
# extract edges using canny edge detection
edges = cv2.canny(img, threshold1=100, threshold2=200)

cv2.imwrite("test/testimg" + str(i) + ".png", img)

cv2.imwrite("test/edgeimg" + str(i) + ".png", edges)


# load training data
df_train = pd.read_csv("fungi_train.csv")

# preprocess all images

for i, row in df_train.iterrows():
print(row["path"])
preprocess_image(row["path"])
```
1. We also tried using [[Oriented Fast and Rotated BRIEF]], but it seems like it finds features that are irrelevant
![[DS3 Datathon Devlog-20250219210529992.webp]]
With this code:
```python
import cv2

import numpy as np

import pandas as pd

import os

from tqdm import tqdm

from sklearn.preprocessing import LabelEncoder

import tensorflow as tf

from tensorflow import keras

from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

from sklearn.model_selection import train_test_split

  

# Load training and test data

df_train = pd.read_csv("fungi_train.csv")

  

# Initialize ORB detector

orb = cv2.ORB_create(nfeatures=20)

def extract_orb_features(image_path):

"""Extract ORB keypoints and descriptors from an image."""

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:

return None, None

keypoints, descriptors = orb.detectAndCompute(img, None)

# Draw keypoints on the image

return cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image with keypoints

  

counter = 0

# Compute ORB features for training images

for row in tqdm(df_train.itertuples(), total=len(df_train), desc="Extracting ORB Features"):

img_with_keypoints = extract_orb_features(row.Path)

cv2.imwrite("orbedges/features" + str(counter) + ".png", img_with_keypoints)

counter += 1
```
# Day 4 - Fungi Preprocessing Again
1. I tried a new script, this one will filter out the darkest parts of the image. I also used a generous amount of [[Gaussian Blur]] to denoise.
2. A read the research paper on this topic linked on the kaggle. https://arxiv.org/pdf/2109.07322.
	1. The best performing model was:
		1. [[ResNet50]] with transfer learning
		2. [[InceptionV3]] without transfer learning
	2. They used preprocessing techniques that removed images which were irrelevant in content
	   - Those with black-lens contour
	     ![[DS3 Datathon Devlog-20250220210009647.webp]]
	   - Those that have no fungal spores
	     ![[DS3 Datathon Devlog-20250220210037634.webp]]
	   - 