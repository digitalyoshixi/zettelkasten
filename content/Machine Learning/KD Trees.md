---
tags:
  - programming
  - algorithm
---
[https://www.youtube.com/watch?v=BK5x7IUTIyU](https://www.youtube.com/watch?v=BK5x7IUTIyU)

Again, like I said before FLANN uses the KD tree data structure. It is a datastructure used to assist in finding the closest point to a select point. It is one of the quickest methods to finding close distances of one point to another.

The KD tree is like a regular tree but instead of holding 1 binary value, it holds K values.

You see a regular tree would just have True or False. A K-D tree point will be able to hold K ammount of properties. This means that this tree can be in the 3rd dimension if K is 3, 4th dimension if K is 4.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_af12b0b9eb2e2ab0.png)

the K-D tree above has 2 for K.

  

so, the question here is that we have a grid of arbitrary points here. And we want to plop a point down and find where the closest point to our placed point is.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_75b5f1cd4ddf6564.png)

lets say every point has the 2 properties x and y.

if we had all these points in memory, we could perform a binary search and just check every point with the previous highscore and see if it beats the distance. That would take a tremendous ammount of time though.

So, we would put these points into a data structure that allows us to better search through them. The K-D tree is the solution to this.

The K-D tree will split the points into 2 groups, then it will split those groups into 2 more groups, and on and on until there is only 1 node left in its own group.

And so our first split can look like this:  
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_af3d443914d966fa.png)

we split at lets say point A.

this is how the tree is constructed. It will find a point it wants to split at, then it makes that the rootnode/currentnode.

So our tree will start with root node A

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_c6a2af828f823450.png) .

so a general rule of thumb is that since we are using 2 dimensions, a 2 = K tree, its a good idea to alternate the splits on different axis. So split once on the X axis, split another on the Y axis.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_651d3987274699c6.png)

so, we split not exactly straight, we split on a point, these points being point B and point C.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_f1a04e0f3332e835.png)

then, we repeat once more.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_d8a919a1c430182f.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_f3773ffdbdd3b4c2.png)

we would technically still split it once more time. Its not truly helpful.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_c6ad329c11a063b1.png)

we just have leaf nodes now.

  

So now we compare our point with a point on the grid.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_ba9a65f3f2bb2b9b.png)

our root node is A. we compare our point’s X to A’s X. if its less, then we continue on the left branch. We go to child B.

then we compare B.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_8a761873fb6732f.png)

my point has smaller Y than B, so I go right branch to E.

now compare E’s X

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_2161c8ba60209347.png)

we are on E’s left side. Lets go to left branch.

And at last we are at the endpoint. G.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_c073956ff8ddebab.png)

But we are not quite done yet.

There might be some tricky points like a point on the other side of E.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_1f5c8e83968ede8e.png)

say like this. We never saw that because we are only checking for if our written point is left or right of E. it is left, but there is a green that is closer

so we need to make our way back up the tree A TINY bit.

We first say ok, the minimum distance is point G. then we ask ourselves, is the distance from our point to E smaller? If not, we are still OK. Now we want to check the values on the other side of E. if there is no values on the other side of the E that is closer than our current min distance, then we are good. As long as theres a change theres a point that could be super close, usually we just go up 1 or 2 nodes.

So il tell you this is how it checks.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_453919e8ee29b3c6.png)

we may be tempted to check B. on the other side of B. but, we firstly need to compare the distance of our min distance to the distance of B. as long as our min distance is bigger than the distance of B, then there is no point in checking the other side of B.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivx6_tmp_af0f0e1bdd99a482.png)

check A, no, still farther than our G point. And we are done. thus, we know our min distance point is G.

  

this data structure works very well for a 2d point because we know how to split things.