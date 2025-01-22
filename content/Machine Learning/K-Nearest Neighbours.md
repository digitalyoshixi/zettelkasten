---
tags:
  - machine_learning
  - machine_learning
  - algorithm
---
This algorithm allows us to classify unknown data using data that is already classified. As you can guess, this is a supervised model

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_7b61eca97ca22478.png)

we have a scatterplot here with overweight people(fat but short) in red and underweight people(tall but skinny) in blue.

There are only 2 classes. Either overweight or underweight.

We have a grey dot that is unclassified. We must classify it. To classify it, we find K of our closest neightbours. If k is one. We check only our closest, if k is 2, then we check 2 of the closest, if k is 3 then 3 closest. We check the distances and the classes of our closest neightbours to determine our result.

If we had a green segment in the middle, and if k = 4, then these could be the neighbours

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_90c787244c2ee507.png)

1 neighbour is green, 3 others are red

  

good practice is to avoid making k divisible by the number of classes you have. Cause if you have k=3 neighbours and 3 classess, you can have cases where you have 1 of each class as your neighbours.

  

### SKlearn datasets and data mining

Sklearn comes with a lot of datasets. We will import one that is for malignant or benign tumors.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_484004ebe4d7cb31.png)

its all from sklearn.datasets

when we load the data, it is actually a bunch object

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_f78fdb857587d9d6.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_fcb757ee3f3a7f64.png)

a bunch object is pretty much sci-py’s version of a dictionary

so we can get the keys.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_8d39f455a13e25c7.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_e21a23b3f7329b57.png)

data and target are the important ones. These 2 are the actual data, the other is just for descriptive purposes of this dataset.

all of Scikit-Learn datasets are divided into `data` and `target`. `data`

both lists in .data and .targets have a length of 529. so both are mapped to eachother. I print data and I print target. Data is the data, target tells us if the dataset is for malginant tumors or benign tumors.

The data list is a 2d list of other lists which are quantities. it is too big to contain in one print. There are 529 of these lists yknow!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_7df7e1fa0f1ff002.png)

The target list is a list of 1s and 0s.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_996fe466a31c4c73.png)

like tha. 0 means malignant, 1 means benign

to understand a bit more, go back to print the keys of data. There are a few things of note

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_45f8b3625d984c99.png)

lets read the DESCR which is the description of this dataset.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_974c5d634c41cab5.png)

So it says number of instances = 569. ok ok, and also 30 attributes. These 30 attributes are the classes. How does that work with 569 instances though? Well the thing about this dataset is that its for people. So an instance could be a person testing. Remember how the data list is a 2d list with other lists? What if we find the length of one of those lists?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_99d627783fa134a0.png)

Aaand it is:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_87b9fb3521bfaa6c.png)

30! hell ya!

I see this could be a relational database. One table is for patients and tumor condition.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_11cd6ac759a9e7e.png)

and another table for the patient and their testing parameters

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_d9715561adb4677c.png)

by the way, you can get the features from just doing data.feature_names

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_676dd7610ee8574a.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_38f44def303539d4.png)

  

### Programming

Lets first get the data. We use data.data and data.target(benign or malignant) as the testing and training data.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_abdc4ffec1e5c031.png)

now we want to train the dataset now. use the KnearestNeighbours algorithm and give it the number of neighbours.

Use the model building function KnearestNeighbours, then fit the training data in it

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_2718b3407637a9fd.png)

know that these xtrain, ytrain, xtest, ytest arrays are already vertical, courtesty of the scipy datasets

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_7c316a304983c69e.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivjc_tmp_b82323f0abae77cf.png)

most have a 95% accuracy. This is very good.