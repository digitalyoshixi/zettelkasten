---
tags:
  - python
  - machine_learning
  - machine_learning
  - machine_learning
  - machine_learning
---
[https://www.youtube.com/watch?v=lE9eZ-FGwoE&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=17](https://www.youtube.com/watch?v=lE9eZ-FGwoE&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=17)

so, what the idea of this script is, is that we have a program that will view our camera and be able to tell what is a book? What is a chair? What is a human? And be able to tell us what is what.

We utilize a pre-trained model to save us the hassle of training them ourselves.

[https://github.com/chuanqi305/MobileNet-SSD](https://github.com/chuanqi305/MobileNet-SSD)

we grab a caffemodel and proto.txt file. Its all we need.

What caffe is, is just like tensorflow and pytorch its a deep learning framework.

We are able to use it all the same as an exported model of tensorflow. Just with some extra steps.

[https://drive.google.com/drive/folders/13nAcSOx_S8QkbDw_oEimv0yRyfJazUNG](https://drive.google.com/drive/folders/13nAcSOx_S8QkbDw_oEimv0yRyfJazUNG)

so, what happened was the github link died, but good people in the youtube comments provided the resources. Lets just check for viruses.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzu_tmp_86cbc369aa86db5a.png)

no worries here.

### Mobilenet SSD

A mobilenet SSD is a object detection model that reads images and computes a bounding box around a object it recognizes as falling under a category.

Like if you have smart camera apps that auto-recognise people and put bounding boxes around them.

SSD means single shot multibox detector. ( actually it should be SSMD wth?) its a neural network that detects objects in images. Mobilenet are classes of efficient models used primarily for vision of mobile devices.

  

### Programming

[https://www.youtube.com/watch?v=lE9eZ-FGwoE&t=146s](https://www.youtube.com/watch?v=lE9eZ-FGwoE&t=146s)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_5b1c5ff5d256ae92.png)

so this is the folder.

In our python code, we import only 2 libraries. Woowee

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_5648b6a469cec5f2.png)

and then we also have to give it the paths for our image and our model:  
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_8a6037bd0b509c3f.png)

as well, we have this confidence ranges.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_4db9ac8c35370d1f.png)

the minimum confidence cutoff is at 20%. so any object it is less than 20% sure it is correct, it will not include in our results. Know that it has classes of 20 objects, and we don’t want a result of 0.000001% for most of the objects that aren’t related.

Uh, so he said he got his object list from the github, this is where it is:

[https://github.com/chuanqi305/MobileNet-SSD/blob/97406996b1eee2d40eb0a00ae567cf41e23369f9/demo.py#L30](https://github.com/chuanqi305/MobileNet-SSD/blob/97406996b1eee2d40eb0a00ae567cf41e23369f9/demo.py#L30)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_5e937e6651715941.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_83eae2bc80d52d79.png)

and so the AI would, when received an image, be able to classify each person with a bounding box as being uniquely person with a confidence rating.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_453fd4868164b317.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_fc4308a980bb9211.png)

we want each class of object to have their own special color scheme. So a sofa has a color box of red, a person has a color box of cyan. Don’t really need to be too precise, just have some random colors

so this is how the color scheme is made:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivzw_tmp_da14e4ee8b532059.png)

this is how our random colors look:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_17839c04b35019f0.png)

there are like 18 rows with 3 columns each so its rgb colors.

Its a different colors each time.

You can give it a seed with np.seed(someint)

next we want to load in the caffemodel. Caffe again is a special framework for making the models, we must load caffe-based so its readNetFromCaffe.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_65056e59118ee45c.png)

so we need to feed an image into the model and it will return the result of the classification and the boxes. We need to feed it a 300x300 image.

Why is it 300x300? Well in the same github, we have the preprocessing here:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_d88606cf5642a219.png)

they resize their images using cv2.resize to a 300x300 image. They also remove 127.5 and then multiply by 0.007843 for some reason?

Its also good to note that we also require postprocessing of the results aswell.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_9a57217adc916b61.png)

we will cover this later. It resizes the image again and draws the detection boxes on the image too.

  

ok so lets preprocess. First load the image with cv2.imread()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_3385f343ca6dc803.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_b42f4daceb4fbbb6.png)

wryyy

I don’t like that I have to use blob. Like so crowded, there must be a simpler way, and there is. I will try it later just so It can be simpler.

Anyhow, the main thing to worry about here is the blob.

  

### Blob

Blob stands for Binary Large OBject. What it is, is just a large friggin object that stores collections of binaries. [https://en.wikipedia.org/wiki/Binary_large_object](https://en.wikipedia.org/wiki/Binary_large_object)

typically images, audios and other multimedia objects.

Blob is a general term aswell, just for representing data like for NoSQL, a blob is how you can store key-value pairs.

Blob in caffe deep learning is used to represent multi-dimensional arrays.

The mutli-dimensional array is what blob refers to in our case.

  

Anyhow, the arguments for this blob are:

**image:** just a cv2 image object. Its called Umat

**scale factor:** float for the scale factor. The demo used the number 0.007843. its what the image is multiplied with

**size:** a cv2.typing.Size or just a tuple for the size of the image given. Kind of redundant, but I guess they didn’t bother to program in auto-size recognition. Actually, good on them, make things more lightweight.

**Mean:** a value you subtract from the image. Demo uses 127.5.

  

ok so thats the blob.

Lets feed in the blob as an input

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_3c74e7d1a506f306.png)

then lets run the model and grab the return value. The return value is detected objects

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_188e6794a557cb14.png)

the type of this return value is a numpy.ndarray, so just a basic numpy array. The size of it is 700 for me. With a shape of (1,1,100,7)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_75fb5a3406a41b78.png)

so its a 4d shape.

I wonder what the first dimension is?

100 is probably the objects its detected?

7 is each of the special parameters the object detected may have? Like its bounding box dimensions, the class?

If we print one of the 3rd dimension objects, we get a list.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_96198cfdddbc15d0.png)

and the hypothesis seems right.

So this is a detected object. It probably includes the classification of the object somewhere like maybe the first element, also the bounding box most definitely.

So

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_f861735e6318d7e.png)

is the first object,

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_698f730785f76c31.png)

be the second object

so on so forth until 99. cuz, yk we have 100 objects

  

and so, I have been told the second element of the object is the classification.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_52a483434d2b9df2.png)

now I want you to notice 2 things. So I printed

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_49fe3d7bad17b68b.png)

for both the program runs.

But, I changed the scalefactor and mean of the preprocessed image between them.

Now, look at that massive different in class. What is class 11? what is class 15?

  

ok, and also we have the other elenments.

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_363ec9e999845cee.png)

The 3rd element is the confidence, the 4th and 5th and 6th and 7th dictate the coordinates. The 4th element is the upper left x coordinate, the 5th element is the upperleft y coordinate, the 6th element is the lower right x coordinate and the 7th element is the lower right y coordinate.

The idea is that the coordinate values are normalized, so we can multiply them by the image height and image with to get the actual coordinates of the bounding boxes on the actual image.

  

Ok so lets draw them bounding boxes now.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_44784d2ad4143a73.png)

iterate through all the objects and check the confidence rating. If confidence rating for that object is bigger than the min confidence, then we want to draw the bounding box

  

also, there is a really cool thing

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_f0eca8c6539b9c8c.png)

instead of referencing like list[x][y][z], we can do list[x,y,z] to get that specific value. I don’t care to use it, im already used to stacking square brackets, but you can do it if you want to.

  

Ok back to what happens when the confidence rating is good enough.

We store the class index.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_285cd06f0f4f0425.png)

and then also the real coordinates of the bounding box

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_71d2c16dcc6613ef.png)

and then we have a prediciton text

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_1d7c9c1c08385b3.png)

for the classification and how confident we are that this is the said class as a percentage up to 2 places.

And at last we have to make the rectangle.

This is done very simple with cv2.rectangle()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_34c15cbbce2be016.png)

cv2 rectangle recieves those arguments.

And then later we also have a caption for the box for what item it views

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_102714c1c402396a.png)

then lastly, we give it our image

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_8abec8a5ab124474.png)

and it is all captioned well.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_124f1b8fc1eb8901.png)

looks kinda nasty.

Ok so it works, lets see if I can do my hypothesis of antiblob.

I tried the antiblob hypothesis, turns out, you still need to convert it to blob afterwards.

  

### Camera reading

So instead of a static image, we will view our camera feed for objects. Not that hard to be honest.

We delete our old resize image in preprocessing and replace it with our camera feed for camera 0.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_5401bb0ee7124d25.png)

and then very simply we get the image from the cap.read() return.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw06_tmp_b72765f291ca7d5c.png)

as the second parameter. So same deal as using a static image, do the same code below, indent it.

And also, instead of waitkey(0), make it waitkey(5) or something like that, just not 0 or below cuz waitkey(num) is the framerate and so if you make it 0fps then it will not update the feed.