---
tags:
  - machine_learning
  - machine_learning
  - machine_learning
  - python
  - machine_learning
---

To build a image classification neural network, you use a convolutional neural networks. Convolutional neural networks are the type of neural networks that you use when dealing with image data, audio data, or just generally to find patterns in data.

In this tutorial we use a keras dataset with some images. There are 10 possible classifications in this dataset. Images can be a plane, they can be a truck, horse, etc.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_2845d92ce58bdd09.png) c

from the cifar10 dataset. [https://paperswithcode.com/dataset/cifar-10](https://paperswithcode.com/dataset/cifar-10)

60,000 images. 10 classes. 6,000 images each class.

  

### programming

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_c3f7a484a3d25444.png)

these are the libraries we are going to need.

Lets get the data in here too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_3cef954b2520eac6.png)

we get the training data, testing data and then we scale them down. The pixel values down from 0-255 to 0-1. this will be good to use for the activation values of the input layer.

Now if we print the labels, it is only from 0-9.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_f6b954f2974dcb18.png)

you see, the labels are in number. So idk maybe 6 corresponds to ‘dog’ and 9 is ‘ship’ idk idk.

So what we do is we are going to make a list. The list will be the string values of these number labels. I don’t need a lookup table, I just use a regular list because I can index the list instead.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_95c733ebd21571af.png)

this is actually quite a challenging problem. A deer and a horse, a truck and a car, we can differentiate these things easily from the specific qualities like size, shape, texture. We also ignore the rotation and orientation of an object mostly. We have to understand that an AI doesn’t know what these things like antlers are, and admitedly the images are in quite low resolution. Around 20-50x20-50 px.

  

Lets look at the images now

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_b01180af07cc1399.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_a979f2057bf4f0e3.png)

yeah its not too easy to recognise these images as a human.

  

The next step we are inclined to do is to scale down the dataset to have a smaller ammount of images. Will make the program run-time smoother

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_a1737afa4c794587.png)

before the training images & training labels were 50,000. now they are 20,000. the testingimages and testinglabels use to be 10,000. now they are 40,000.

a 60% reduction overall

not needed, but we want to save computer resources.

  

Now lets build the neural network

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_d7565f9a3f528de7.png)

sequential yknow basic framework barebones structure.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_65c5eed0fad41eca.png)

The input layer is convoluted Conv2D infact. There are 32 neurons and there is a 3x3 as the convolution matrix filter. The activation function is ReLU and at last the input shape is 32*32*3. resolution is 32px by 32px with 3 color channels.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_a1708ed9b3e939e.png)

And also, everytime you have a convoluted layer, you also have a max layer right after it which simplifies the output of the previous layer. This could be considered a hidden layer since its not the input layer but it is necessary to have right after the input layer so idk what you would call that.

The max layer has a 2x2 filter

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_85b2d4cab69b8966.png)

after that we have another convolutional layer, 64 neurons this time, same 3x3 filter and with a relu activation function. Alongside it we also have a max pooling with 2x2 filter

after that we have another convolutional later, 64 neurons and 3x3 filter

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_192e7b7fe7ae95fb.png)

now after that we have a flattened layer. This will flatten the convolutional layer before it into a 1 dimensional array

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_1261593912027c34.png)

and finally 2 dense layers. One is the output with the softmax activation

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_d71f4df08f6c76af.png)

and so this is the entire network:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_c5a48e6540062d7f.png)

the convolutional layers filters for features in an image. Like a horse has long legs, a cat has pointy ears, a plane has wings, it looks for all these features, max pooling will then reduce the image to the essential information, then toss to another convolutional layer, reduce, then flatten, dense layers for complexity. The output layer scales the results down to probability of classifications.

  

At last, compile the model and fit the training data in it

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_aba6dec3c95f929f.png)

validation data here to help with the loss function is the testingimages and testing labels

  

write some evaluation test on the model before we save it

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_72cd7d86294d6f0f.png)

and now we save it:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_125373db09931d76.png)

ok run the program now.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_6b7bf06bd11931fd.png)

the loss doesn’t really matter a lot. The loss is just a metric for the computer. What we really are interested in is the accuracy value.

Its at a 64%. not the greatest, but still pretty impressive given that a guess at random would be only 10% accurate and the AI has hardly an idea about to concept of antlers.

  

Ok we made the model. Lets load it so we don’t have to make it everytime we run the script.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_d9b7e5b601ad2796.png)

  

### Using real images

We are going to grab some images off of yandex, scale them down ourselves manually and then feed them into the neural network to test it.

I use photoshop. Crop it down, then I go to properties and click Image size and change it to 32x32

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_ccd635975ab63a19.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_6ba1ada699768804.jpg) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_104f86b0a13644e9.jpg) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_e94377df444046b1.jpg) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_797dfcc739056eab.jpg) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_dd73dc17838bd8c4.png)

can you guess what the images are?

I put them into my python directory

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_d88d26d4dabc6e45.png)

ugh so disorganized.

  

To load the images into the script we use opencv and numpy.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_ff263f87362228eb.png)

a problem here is that the images we load in with CV by default use the BGR color format, but up til now we have been using the RGB color format. To change this, we need to convert the color schemes.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_5774d0f22c8413fc.png)

we can show using matplotlib

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_b3637313fe1e80f7.png)

  

now lets predict the classification of this image

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_9c175cbf75a20071.png)

we first convert the model into a numpy array divided by 255 cuz remember we scaled our testing data input to be between 0 and 1. we do model.predict with that new numpy image array.

Then from the softmax output, we want to grab the maximum value. The maximum value will be in a index format like 0-9 cuz remember thats what it does always. We will then need to convert that input to a class string from our classnames list![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_cba3e20d219ca68c.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_1970298d8bd0b880.png)

argmax will get us the index of the maximum value

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_1449191822b04228.png)

and that should be it.

  

For horse.jpg: ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_6ba1ada699768804.jpg) it says:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_611cc1ddeb2ab39e.png)

for horse2,jpg: ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_104f86b0a13644e9.jpg) it says: ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_ef2952eb42d28528.png)

for plane.jpg: ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_dd73dc17838bd8c4.png) it says:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_2eb7678b6a0f01a7.png)

for car.jpg:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_797dfcc739056eab.jpg) it says:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_a539d167edfd91c9.png)

for deer.jpg:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_e94377df444046b1.jpg) it says:![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivoj_tmp_8d3ee5019c28a1b4.png)

  

40% winrate. Eh, alright I guess. The images I fed were not that great.