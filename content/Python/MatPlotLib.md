---
tags:
  - python
  - programming
  - data_science
---
Matplotlib is how we plot our devious plots. Mostly in the form of functions.

**Import matplotlib.pyplot as plt**

plt is the standard alias

  

### Drawing

for matplotlib to draw us our function, we need to give it the x and y values first. Define a range of x and put it into a y value funciton then input into matplotlib

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_d2961be3965e8c0.png)

my y function is just x^2 so it will be a parabola. To run these into matplot, just do plt.plot(x,y) and then show the graph using plt.show()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_35e9473174a56d18.png)

  

We can also plot multiple graphs on the same axis. Just do another plot with a different function.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_7e0d178f7f669e41.png)

Now on run, it looks like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_428128db9e0e0970.png)

  

### fun feature of color

We can have fun with the graph plot. Give it some styles like red graph, blue graph, black graph

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_dcb89bc44629274e.png)

thats a red graph

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_a99ba2121895fb79.png)

thats a dash red graph

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_c7138c4b5f8208bb.png)

thats a dotted green graph

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhd_tmp_483fbec7c22b9699.png)

thats a triangle dotten yellow graph'

### subplots

You have several plots inside one window.

plt.subplot(NumrowNumcolumnIndex) the reason why that parameter is like that is because you just give it one integer, but the integer has 3 digits. The firs digit is the number of rows to subplot, the second is the number of columns to subplot, the third is what index am i

first 2 digits don’t change for subplot, only 3rd does because index always differs. You must store this subplot as a variable, then variable.plot(x,y) to plot.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhm_tmp_4af4b125e1e4b442.png)

also use plt.tightlayout() before show to make it look nicer

  

### Multiple windows(figures)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhm_tmp_135e585dc8057f55.png)

simply do np.figure(fignum) and then do all your plotting below it, then if you want another window, do another figure, so on so forth

### Pie charts

The simplest rendition of the pie graph is just pass it a single number list. plt.pie(numlist)

to give it labels: plt.pie(numlist,labels=labelslist)

to give it percents, you do plt.pie(numlist,labels=labelslist,autopct=’%.2f\%\%\’) to show it at 2 decimal places

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhp_tmp_16574cfab94c710b.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhp_tmp_68632e20d3179e71.png)

### 3d Graph

We want to plot a 3d graph. To do this, we must first import another library from mpl_toolkits.

From mpl_toolkits import mplot3d

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhs_tmp_7f86f35506da6fcb.png)

this is the most rudimentary way to show a 3d grid

  

then lets get our table of values, xyz axis all 3.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhs_tmp_d992b59c47a48a4c.png)

then just do ax.plot3D(x,y,z)


Some graphs are surfaces, not points. To graph this, we must have our xyz table of values, but have one plane be a matrix, then just ax.plot_surface(X,Y,Z)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhs_tmp_c881c7d45a6a497c.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivhs_tmp_effde9e6455e49eb.png)