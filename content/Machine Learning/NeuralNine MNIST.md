---
tags:
  - neural_networks
  - machine_learning
  - machine_learning
  - python
  - NeuralNine
---
Yea we are going to make an ai to read hand-written digits.

We are going to need the **cv2** library to read

to install **cv2**, type: **pip install opencv-python**

cv is computer vision so it processes images into data we can use for our neural network

we also want numpy, matplotlib and tensorflow too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_290533e12da92218.png)

tensorflow is the neural network

### Programming

we will also use the MNIST dataset which is a dataset of around 6000 samples of hand-written digits

the MNIST dataset is in tensorflow. This is how we import it:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_dc7b2d8f91e24cda.png)

we print, it is this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_85de9a34ca9942b1.png)

it is the directory of where the dataset is. Succ cess

the mnist dataset is classified so this is a supervised model.

This is how we load the data:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_347828087d98c908.png)

it is around a 10-20% data split

the next step is to normalize the data. Scale it down so the computer can read it easier.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_e1dbb9ea5c037e22.png)

you see tensorflow replaces a lot of sci-py’s functions aswell. There is little use using both libraries at the same time, and tensorflow is much more powerful than sci-py.

  

Now lets make the neural network model. We want 1 input layer, 2 hidden layers and 1 output layer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_7bc0beb7f098411f.png)

above code is how we make a basic, rudimentary, naked, barebones neural network.

Lets add the input layer now.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_59afcfcd107eae0b.png)

the first layer will take a 28x28 and then flatten it to 784 neurons.

Then we make a hidden layer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_ca5b98c7dc8e7b91.png)

we add the dense layer. Everything in this layer will be connected to the neurons on the previous layer. And our hidden layer here has 128 neurons. We will also have the activation function of each layer be relu so the values are always 0 or positive.

Add another hidden layer

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_1d20ddd7cb99b0b0.png)

and finally the output layer. Its another dense layer, but we don’t add any other dense layers after it so it is technically the output.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_1b3abe378d3399c1.png)

what softmax does is that it takes every activation value of every neuron in the layer, scales the layer down to 1 so that every neuron is a percentage of what we think the hand-written digit is.

Almost there. compile the model

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_27b80db93c96c9d5.png)

dunno what all this does, but our loss function used for improving the model is spare_categorical_crossentropy, and we just look for the accuracy metric.

Finally we fit the model

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_46a559c4a5fd3d35.png)

epochs is how many times do we want the model to see the same data over and over again? How many times to repeat the process? Give it 3. it has 2 tries to learn from its mistakes

  

ok lets test the model now.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_633b8ee590d79b92.png)

also save the model as a model file. We want to use the model ourselves and feed it some images later.

Ok run the program ok?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_d365ac59a1315911.png)

you see there is a warning. It doesn’t affect anything at all, just that the function is not callable. Its probably a old function they don’t use anymore

  

### New data

Ok lets draw some drawings and feed it to the model, hope it doesn’t explode!

I have a 1 2 3 and 4

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_ac1910658d40f308.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_9a67fd511291c488.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_38a057d70bbc131c.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_fdda78a6edbd05a1.png)

28x28 pixels. I put them in the same folder as my model which was created

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_91dcfa34efd8af1b.png)

then I have this segment to read the data.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_ce84ee89b775010f.png)

again, cv is computer vision so it is how we read images. The [:,:,0] means we are reading the entire image, not slicing anywhere or anybody, I have the range from 2 to 4 because I only have images 2 to 3. I will be 2 and 3. I am also matplotlib plotting the images so we can see them.

We have these specific segments to adjust the colormaps so that the model can read it easier

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_d52fd14da566c3ca.png)

cmap is binary, invert the np array so that it is black on white instead of white on black.

  

The last step is to feed it into the model

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_75e7245836ea499c.png)

this is the model’s prediction. Prediction is a list of the output layer. We want to print only the neuron with the highest lighting. Lucky for us, like really lucky, like this is probably the only datamodel that we can do this, we can just print the index of that list which has the highest lighting and that is our digit.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_7579ddfed83011d.png)

print the argmax. The argmax just gives us the index with the largest numerical value in the list

ok, we run now

libreoffice crashed. Tldr, the results were bad.

Ok new drawings;

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_ddc029a35aa74019.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_8998b2807eeb8daf.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_a3a55ca989d9384.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_b67f35ffbc2444e0.png)

the results are:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_c0940f261c5eefa5.png)

also quite shite. Ahh oh well, ¾ is pretty good I guess. I could run it through some more epochs, or maybe find more datasets. Maybe can write real hand-written digits too.

  

## Reading the keras dataset

So I know the MNIST dataset is big like really big like 6000. but for some reason, I only have 1875 for each epoch run. Why??? lets look at the dataset.

It is stored at

`C:\Users\My_User_Name\.keras\datasets`

and I see mnist.npz

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlw_tmp_b21ce1b14672b39f.png)

I can open .npz files using python numpy.

Huh, I read and I got more confused.

Anyhow got a new skill anyways.

  

The real reason why it is 1875 is because: [https://stackoverflow.com/questions/62186784/why-the-model-is-training-on-only-1875-training-set-images-if-there-are-60000-im](https://stackoverflow.com/questions/62186784/why-the-model-is-training-on-only-1875-training-set-images-if-there-are-60000-im)

it is reading in batches of 32 images at once. How optimized!