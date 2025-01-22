---
tags:
  - machine_learning
  - machine_learning
  - algorithm
---
Very powerful tools for classifying data by using support vectors. Can even outperform neural networks in tasks like reading handwritten digits.

How it works is imagine we have 2 classes on a 2d graph and depending on where we put an unclassified point, we want to be able to classify it

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_15ef524df3a67fa.png)

what we did for K-nearest was check for the points that had the most similar properties to the unclassified point. What we do with a support vector is we actually train with a mathematical function to split the data

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_da129dea644f0090.png)

alright easy. We need to make these curves/lines/planes/curvedplanes/hyperplanes/hypercurvedplanes.

Now there are usually an infinite ammount of ways to split some lines, you can have lines like this

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_d63e8e1d86695c54.png)

and they all split the classes

  

so the line we use is going to be the most generalized line. The one that is the farthest away from all points as possible. This is how it would look like:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_cc951f8b81b8a8de.png)

in order to find that line, we use support vectors. We have a line, and we draw a parallel support vector to the nearest point of a class.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_eb8037be2cf7d1ba.png)

the spacing between each nearest class point to the line is the margin. If the margin for each class is the same or close enough to the same, then this line is good.

  

### Kernels

For certain data sets, it is impossible to draw lines that seperate data.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_e2ee58a4dad96931.png)

like if I wanted to seperate blue and red, I couldn’t because its not possible for a line to segment half way.

What a kernel is is turning a dataset higher one dimension, then finding the hyperplane to seperate the data. Since its a 2d dataset, we will elevate it to the 3rd dimensions and make a plane that only touches blue and another plane that only touches red.

  

### Soft margins

Are a way to allow outliers in the divison up to a certain point.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_c7944e9f55fc8652.png)

above is the optimal way to divide the 2 classes, however some blue is in the red class and some red is in the blue class. The soft margin we can give it is 2 to tell it we can allow up to 2 misclassifications so there is a better model. By allowing some misclassifications in the moment, you make the model better in the future.

Soft margins very softly affect data scores. They very slightly move the margin to be bigger or smaller

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_42bbf165ba21ae87.png)

  

### Programming

The module we use is from sci-py and it is **from sklearn.svm import SVC**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_22ae6847e38d18ad.png)

firstly, get your data training and testing data.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_20b4c20874a64538.png)

then we will make our classifier model which is SVC classfier.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_9c1bafd2c437b375.png)

you make the kernel argument any of the following:

1. rbf. Slow but accurate
    
2. poly / polynomial
    
3. linear. Quick but choppy
    
4. sigmoid
    
5. precomputed
    

we can also give the classifier a soft margin for the parameter C

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_6e5890732c3926fb.png)

  

then lets train it. Simple fit with the testing data

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_fdbd78f543e15d93.png)

and at last we can test the model using score

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_4d863b7d9725501b.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_b33d84335d9fadf9.png)

decent results

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_a613378d2228d552.png)

compared to a K-nearest algorithm, the support vector ranks higher 4-7% better.

  

### Unrandom states

To stop random training and testing splits, then you need to give the train_set_split a seed.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_f49987ffc7f4daff.png)

random_state = any number

###   

### string formatting like C and such

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjy_tmp_3f7c796759e0b0b9.png)

is how you format python strings. You need the f’’ with some curly braces for the datatype to format