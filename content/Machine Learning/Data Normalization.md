---
tags:
  - math
  - data_science
  - machine_learning
aliases:
  - Normalize
---
[https://www.geeksforgeeks.org/what-is-data-normalization/](https://www.geeksforgeeks.org/what-is-data-normalization/)

Part of the [[Preprocessing]] stage of any problem. It is scaling the data to be analyzed in a specific range to provide better results. Data Normalization disposes of various anomalies that can make an examination of the information more complicated. It also makes data more clustered

[https://www.youtube.com/watch?v=sxEqtjLC0aM](https://www.youtube.com/watch?v=sxEqtjLC0aM)

scaling can be though of as just changing the values of the data where the ratios are the same but the actual values are smaller.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl2_tmp_795ce3f46da4e47b.png)

scale it down perfectly, and you get normalization where the data is in smaller ranges and is not affected in its ratios.

There are a few normalization techniques

1. min max normalizaiton. The formula is (x – x_min) / (x_max – x_min)
    
    ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl2_tmp_3b7b57a13897df6.png) the data is between 0 and 1![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl2_tmp_3d4ee6ddaa39dd91.png)
    
2. Z score / standardization. Formula is (x – x_mean)/(std). Subtract x by x mean and divide by standard deviation.
    
    ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl2_tmp_2c311ee4203d4d.png) a misconception beginners have is that standardization distributions are normal distributions. This is not even true!
    

Standardization is important for :

1. convergence. when data is being converged at the same time. one dataset is huge! Another is tiny tiny small, as a result to keep both datasets read within the same time, the stepsize for the small one is small, the stepsize for the huge one is huge causing unwanted oscilization during convergence.
    
2. Computing distance correctly. You have an algorithm that gets distance. But you see the x axis is huge! If you measure here, then your result will be too big and the x is too big relative to y. If you don’t scale both features to have the same distance scale, then you will have data that is compares on the wrong axis/features.
    
    ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl2_tmp_5ab35987a5c8004a.png) left is before scale. Right is after ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivl2_tmp_a01b1c25ea8d983a.png)