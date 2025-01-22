---
tags:
  - machine_learning
  - machine_learning
  - algorithm
---
  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_da1f49c64ab0da6b.png)

we have mark and we want to determine if he will go outside or not today. What affects if he wants to go outside is if it is sunny, windy, rainy and if hes alone.

We give the decision tree the data of if he went outside and what conditions were it that day and the decision tree ends up with the classification of is he going outside or not?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_3400a046cd0300d8.png)

the decision tree asks a lot of questions which branch off to different paths. At the end of each branch it has a value of yes we are going outside or no we stay indoors. Some decisions the tree doesn’t even need to put. It may be that 2 decisions lead to the same outcome so the parent decision leads to a single outcome. Also the decisions don’t have to be binary, it can have 3 branches, 4 branches even more

  

how its done is we give it a root node. The root node asks the first question.

From that you can lead to several branches. In our example you ask for sunny and you get yes or no. So this is the dataset:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_2428eb25cfb8225f.png)

these are the bare minimum we need, sunny? Rainy? Windy? Alone? And the conclusion value.

So in the root branch where we ask for sunny, we check the result with the conclusion

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_e5601544308c6376.png)

see if there is an immediate correlation between sunny and conclusion. In our case, he always goes out when its sunny. Count the ammount of times the conclusion results in yes and how many times the conclusion results in no

Then we check the other node that is the rain node

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_9c43b53871812cdd.png)

if that result always concludes in a NO or it always concludes in a YES then we know there is a 100% correlation there and can end the branching there.

  

### Random forest classification

What your root node is matters. Every conclusion correlation we get is based off the root node. On occasion, starting at a different root node may crush a lot of redundant correlations like if it rain yes, then always no outside, we wouldn’t have to ask for rain several times if rain was the 3rd checked node. Rain node would be root and thus we never ask it more than once.

TLDR: Decision trees may vary wildly depending on the root node.

This is the problem that the random forest classification solves.

It will make several decision trees and train them on the same data

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_b177a77a2ad66369.png)

Then, we would test the forest with a testing data. And for the most voted on answer, that is the democratic mood of the forest, that is our answer. We reduce the risk of misclassifications.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_d9248cb1f76b5ef5.png)

  

### programming

So we will use 2 classifiers here. One for making the trees and one for the forest. You don’t need both, but we use both to just compare.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_6472f422636cc7c4.png)

then for data creation, get the dataset and the train_test_split

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_bc2ada25fc2bb386.png)

ok we got the data. Lets make the classifiers

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_c83ba7c3f99bea67.png)

then we test both models and see the results.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_278cb9bbe66f9144.png)

no suprise, more is merrier.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_fc4eb62e9ea0907e.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkh_tmp_226d3eacd7d7323e.png)

still, most of the time the supporting vector classifiers are the best way.