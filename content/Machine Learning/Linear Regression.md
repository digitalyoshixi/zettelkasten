---
tags:
  - machine_learning
  - machine_learning
  - algorithm
---
The first machine learning algorithm for supervised learning. It models the relationship based on a scalar quantity to one explanatory variable. There is an independent variable that dictates a dependent variable’s value. You may have a graph like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_d7e72e4f055d154e.png)

The independent variable is time studied, the dependant one is score. The goal is to plot a line of best fit for this data using f(x) = mx+b. Its called a linear regression because it uses a single line. A regular regression would just be a curve that passes through all points, not very generalized.

The machine learning model, if it knows this trend, can predict future values.

Linear models are the most acurate the more variables you have, like a 20dimensional data set, the linear model performs better. In a 3d space, a linear model would be a plane, since the 3 axis.

  

### Programming

First import the numpy, matplotlib to visualize and sklearn.

Then make 2 arrays. One for time studied and the other for grade received.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_2aa0987f9a14c624.png)

then we need to make the arrays vertical, so transpose then using .reshape

-1 is a wildcard. We tell numpy to ‘figure it out’ given the other axis. The shape must always have the same area, so for a 2d array, if we give it one dimension, it knows the number of elements and it figures out the size of the other dimension.

Additionally, this also makes the arrays 2d now. Cuz we reshape on 2 axis.

Then we need to make the line of best fit. Make the linear regression model and make the line of best fit.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_461896c642a0c0af.png)

Then plot it out using matplotlib with a scatter plot.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_f3ebf759aaadce39.png)

the line of best fit is on ln 12. we give it a range of x values for the first argument, and the second argument of y values is generated from model.predict(xvalues). And the x values have to be reshaped into vertical 2d list format too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_ee41091b24d7512b.png)

  

### Predictions

The model can predict a y value given an x value as we did above with line of best fit.

Model.predict(numpyxvaluesarray)

you must feed it a numpy x values array which is in 2d vertical format. It returns a numpy y values array which is also in 2d vertical format.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_1a46da87f4686414.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_e98debc569debd79.png)

  

### Testing models

We don’t know how good the model is. To test our model, we may use 80% of our data to train the model, then leave 20% of the data to use for testing the model.

We can do this by using train_test_split from the sklearn library to split our data

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_d81d7fc4e3f1cfd6.png)

use as many lists as you want seperated by commands, then give it a test_size=number:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_f9881b33b2bf5b0c.png)

timestudied is split into timetrain and timetest

grades is split into gradetrain and gradetest

the 2 lists match eachother aswell. Every time in the timetrain/timetest corresponds to the index in gradetrain,gradetest. If you did a train_test_split for both lists seperately, you would get different results that don’t match the indexes.

  

Then to test, you use model.score(numpyxarray,numpyyarray)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_a9a0ce6638950245.png)

gives a numerical value of standard deviation from line of best fit.

every time you run it you get different training sets and different testing sets.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_48598376e4464bb.png)

the score:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_9b0ee7d49b6844d5.png)

53% off

another:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_9aa63198cb0cfbef.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_cf26ef614ca46138.png)

71% off

  

Here is running the simulation 20 times:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_9ffe0a2784aeaed8.png)

and the results:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_5b0dc1e33ccdcef6.png)

you see there is one that is -200% off. Lets see if we can make it better.

Change test_size to 0.3

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_bb21e4336dd27bd6.png)

o no its even worse

what about 0.1?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_20f64a19c6d651ba.png)

OH MY SHIT THATS HORRIBLE!

0.25 is pretty good though

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivir_tmp_768bfcc9c8106947.png)