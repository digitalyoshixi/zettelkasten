---
tags:
  - programming
  - python
  - data_science
---
Essential for data science. It in it of itself is not enough, but numpy is the basis for matplotlib, pandas, they work with numpy as a basis foundation. It allows for efficent and effecive processing of lists and arrays. Data science uses linear algebra a lot, uses matrices, vectors and numpy allows processing of these in an efficient way.

We always alias numpy as np

  

to make an array in numpy, we just do np.array(list)

you pass a list into it.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_b351f606ff89c873.png)

the interesting thing here is when you operate lists in numpy, it actually elementwise operations.

  

You can also make a multidimensional array

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_3d55266ada3d81aa.png)

and you can print the shape of the matrix too using matrix.shape

  

numpy arrays are actually vectors. Thats why when you add 2 numpy arrays, you get the elementwise addition. A 4d vector can be like: np.array([2,3,4,5])

since there is 4 elements.

  

### Numpy X dimensions

To create an X dimensional array, you can use np.zeros()

the ammount of parameters you give it will make it a different dimensioned array, np.zeros(3,2,6) will make a 3x2x6 array(3d).

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_962ef8577233dceb.png)

you can also do the same with .ones().

You may also do any other number. Using .full()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_f67f6c2219f780db.png)

the first parameter is the shape, the second parameter is the element to fill with

  

you can also make an empty X dimensional array with np.empty(dimensiontuple). The array might look like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_7f766e36aec48beb.png)

You may also fill an array with random numbers. Just give it the dimensions parameter. np.random.random(dimensionstuple).

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_925fa9a4af2b9931.png)

Very useful for unbiased input

  

### Numpy function arrays

we may also want functions for numpy arrays

you have 2 options: np.arange and np.linspace.

  

np.arange() takes the starting point, ending point and stepsize as parameters

np.arange(3,9,2) will print [3,5,7]. the end point is exclusive

  

np.linspace will evenly distribute values for a line space. Will split an array into x ammount of elements evenly distributed.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_d4d8e0cf912c3aed.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_bd78a462a0e59cc1.png)

and so on, there are 100 elements here

  

### Numpy array attributes

.shape() gets the overall shape on an array, the dimensions and such

.size() gets the number of elements in the array.

.ndim() gets the dimension number that are safe(that are actual dimensions like u cannot have a 2d array if one of the 1darrays is bigger than the other) doesn’t give dimensions just tells you if a array is 2d, 3d, 4d, 1d, etc

.dtype() what is the datatype this array holds.

You can also specify the datatype inside a array by just adding another parameter which says dtype=datatype

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivgv_tmp_538503660d69f420.png)

numpy functions

Shape manipulation, aggregate and some more

  

### Mathematical functions

we know we can use regular arithmetic operations, but we can also use mathematical operations like sin,cos,tan elementwise too.

  

  

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivh5_tmp_8b0af40233c8235f.png)

np.cos(array) will cosine each element

np.sin(array) sine each element

np.tan(array) tangent each elements

there are no cot,csc,sec. They are just reciprocals so its not needed

np.exp(array) eulers number ^ x

np.sqrt(array) square root each elements

np.log(array) natural logarithm each elements

  

### Aggregating functions

array.sum() will sum up all the elements. Works no matter how big the array is

array.max() find the maximum element in the array. Any size

array.min() find minimum number in array

array.mean() average element

np.median(array) middle elements

np.std(array) standard deviation. How much does each value deviate from the mean array.

  

### Shape manipulation

Manipulates the shape of the array

array.reshape(tupleshape) reshape into a different sized array. Can reshape into different dimensioned array too as long as it can fit the same ammount of elements

array.flatten() turns the array into a 1d array. Some inputs must only be flattened in neural networks

array.transpose() rotates, flips array swaps the dimensions.

  

### List joining

np.concatenate(array1,array2,array3…) just like regular array concatenation. Adds directly to the end of another

np.stack(array1,array2,array3…) it like makes another dimension dude. Makes a new array then adds the 2 arrays to it so like it just adds a dimension, makes 2 lists a matrix and such

np.hstack(arraystuple) only works if both arrays have the same dimensions. concats each row/matrix/tensor,etc in one list to the corresponding row/matrix/tensor,etc on the other. Horizontal stack

np.vstack(arraystuple)

  

### Splitting

np.split(array, segments) opposite of stack. splits an array into dimensions smaller evenly between the segments given. Not elementwise, it depends on the immediate elements of the array and it must be evenly! No split can bleed into the element itself, we split the array, NOT the elements

np.hsplit(array, segments) split horizontally. Better visualized as segmenting vertically, but for some reason they are reversed.

np.vsplit(array,segments) split vertically. Also better visualized as splitting horizontally, but reversed nonetheless.

  

### Appending

np.append(array, element,axis) element must be the same dimension as the ARRAY, not the array’s elements, but the ARRAY itself. Axis is what axis, x,y,z(0,1,2,3)???

np.insert(array,index,element,axis) index of what immediate element to replace, axis again is optional

