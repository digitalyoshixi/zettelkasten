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
5. I also used stegonline, to see if it could better make out some details as the images for category 1 and category 3 are very noisy
   ![[DS3 Datathon Devlog-20250219190943239.webp]]
6. Also, turning images into grayscale helps define details a lot nicer.
   ![[DS3 Datathon Devlog-20250219192535513.webp]]
7. Gaussian blur was suggested, I do like this idea since it makes detail more clear, but we have to make sure that it does not over-blur
   ![[DS3 Datathon Devlog-20250219193122292.webp]]