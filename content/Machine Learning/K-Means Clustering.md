---
tags:
  - machine_learning
  - machine_learning
  - algorithm
---
This is our first unsupervised model.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkv_tmp_7b74c55ba97eebb.png)

so we just have a bunch of unclassified clusters on our graph. We want to find a certain K amount of clusters, and then when we give an unclustered point we can assign a cluster to it.

Real data may not be as good as the graph above, we may also work in 20 dimensions, 40 dimensions high ass dimensions. The computer needs an algorithm

  

The algorithm goes like this:

you give it a K number of clusters and it places centroids around the grid.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkv_tmp_c19e50b7df7cc24d.png)

the centroids are the centres of the clusters and they are randomly placed. Then for each datapoint, we ask it: where is the nearest centroid?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkv_tmp_17eb9fef90ab460f.png)

_drawing is not the most accurate_

then, we delete the centroid we already have and place it in the centre of all the points so that the centroid is actually in the center.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkv_tmp_7528ce8c038b5286.png)

but you see, its not very valid anymore.

So we do the same again, we ask with the new centroids for every point, what centroid am I nearest to? And they all update

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkv_tmp_6e48f61943d9a26c.png)

Centroids center

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivkv_tmp_b88e4d8d4e7792df.png)

then ask again for all points: what centroid am I closest to? Nothing changes and this is how the algorithm ends.

### Programming

We still use sci-py.

**From sklearn.clusters import KMeans**

we also want to use scale from preprocessing to normalize our data into 0 and 1.

**From sklearn.preprocessing import scale**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl9_tmp_95879193ca17f8ed.png)

the dataset we will be using is the load_digits dataset.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl9_tmp_f085950fc1bdba3f.png)

this is a dataset of hand-written digits.

We don’t want to tell the ai what clasification each digit is, we just want it to spot patterns in the data and we want it to add new data to see what category it fits in. we give the model a bunch of pictures and the model tells us which pictures are similar and which are not.

  

Ok lets make the data now.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl9_tmp_c2333f0464014ab2.png)

we load the digits then we scale to normalize

  

then we make the model.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl9_tmp_2751e8e535f381ec.png)

n_clusters is the number of clusters we want.

init is the initialization method. We could pass an array or callable in there, but make it random for now it works.

n_init is the number of times we want to try to start with different init positions. How many times we want our centroids to be randomized.

The model just fits data, just one data, there is no class just points.

  

Now it is important to know we cannot test this. It doesn’t know there is a true or a false answer.

We could use the predict feature, and it will tell us what cluster our bunch of pixels belong to, but it will not know what digit it is.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl9_tmp_cd1dc8338dc32d7a.png)

_pretend there is an image file there_