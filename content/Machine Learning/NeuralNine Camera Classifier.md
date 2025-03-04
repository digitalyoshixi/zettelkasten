---
tags:
  - machine_learning
  - machine_learning
  - machine_learning
  - machine_learning
  - python
---
He made a tkinter ui for training a model. How cool is that?

A model that is trained on the fly, then using tkinter.

So you would hold up a cup and then press the cup button to train your own images of a cup, then you give it images of a book, train, and then, when you hold a new image, it can classify it.

So whenever you take images, they are saved to a folder on the computer, the folder is the classname.

So there are these features:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw0x_tmp_fd19477f13131148.png)

autoprediction just predicts whatever is in the camera feed at any given time, cpu intensive.

Phone will take a picture of your feed and then save it as training data

book similar to phone, but for a different class

train model will train the model on your phone, book data.

Predict will just predict whatever is in the frame as what class whenever you click it

reset will clear the training data.

  

So, its not limited to a certain class of object, you can literally classify anything, just granted you have the images.

  

### Camera

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw0x_tmp_10fcffba765ff2c9.png)

the only library we will be using is cv2.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw0x_tmp_6d227f206b385699.png)

the entirety of this script is just one custom object.

We have this class which is Camera, the camera has a property .camera which is the video capture. There is also a getframe function which is for grabbing each frame and returning the return value and the cvtColor value.

### App

So we have the camera script working, now lets create the actual app for the camera. The app will build the ui, it will train the model, it will save the images, it will get the camera, it will classify, pretty much all the functionality.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_734115d2cbd75170.png)

above is all the imported libraries we want.

Im going to try a sort of challenge. So hes building is model with a set of 2 classes. I am going to try to see if I can make the number of classes adjustable.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_44e3f7ba5400d85e.png)

we have also, a class for the App itself.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_888091669afd6e6d.png)

  

### None vs Ellipsis

So, I thought there was no real different for placeholders. I just used to, if there was a placeholder value I would just make the value None, but apparently, that is bad practice? Instead, None should only be used for placeholder parameters for functions and default return values.

… is for placeholder code. Saying, that I will add something here at a later time. It will not break the code, but it will just print an ellipsis data type. So, its just placeholder for the programmers.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_3b2c0936b203ab48.png) ’

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_31fa96c9aa258a3a.png)

  

  

so return back to the program,

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_c9dfa3001db987a2.png)

we want to give it a property of model.

I don’t know much about classes, ive used them before, never really gave them too much thought, il check a tutorial out later today.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_5a3c9ddd68960350.png)

we will also have the autopredict feature be false right off the bat.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_223a482508711fc2.png)

we load the camera object we previously made.

Hes having chronological difficulties.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_c4716f9960debd5a.png)

and has added properties that he is supposed to add in the future.

Anyhow, we have a initgui method, a delay property a window property with attribute of topmost and a mainloop method for the window

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_e5c72342fb6143b0.png)

then we have a function called autopredict toggle which is very simple.

Then we will have another function called initgui()

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_ffd2bc2367bfc0a0.png)

its a simple tkinter gui. Lets just change it a bit to make it fit our challenge.

This is my patch, it may or may not work.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_22b38fa15e8359f8.png)

  

he also did a slip up in his camera script, we need to add these 2 lines because we will be using the height and width of the camera.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_dea5fcfde3f112f8.png) \

so added into the camera script.

So a quick description of the buttons:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_685297154426defb.png)

each button is assigned to be placed on our self.window, each button as a text, width of button, the height is set automatically so don’t worry about that and we ave the command of the button which will be it runs a function.

We anchor it in the center of the x axis of the window and expand = true for the y to be adjustable according to the button text. Acutally pack has 3 options.

[https://www.activestate.com/resources/quick-reads/how-to-position-buttons-in-tkinter-with-pack/](https://www.activestate.com/resources/quick-reads/how-to-position-buttons-in-tkinter-with-pack/)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_5dae8f069a5306d1.png)

side option aligns text on a side like tkinter.LEFT, tkinter.TOP so it will always be on a side. fill will align it to the next open spot vertically, expand will do something similar to fill, but also scale the y scale accordingly.

  

Right so I actually like this a lot, he gave us a chunk of code with functions named appropriately, now our next path is set out, complete the functions it requires of us.

Lets make the saveforclass funciton first

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_468c3c116d9eea80.png)

so it will have a single parameter( ignoring the self parameter), it will have a classnum parameter.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_8e25db5a7f29d7d2.png)

What we will have is we make a directory for every class and then we take a snapshot of the camera feed as a jpg image

  

### JPEG vs PNG for ML

So, we used jpeg for this. Jpeg is good for this project because video feeds will represent their image data in the jpg format anyways, so its a bit useless to convert to PNG. Acutally, pngs have their purpose. PNGs are a lossless format, so things that require sharp lines and solid colors and accurate detail, use PNG. For video-related activities, it’d be best to use jpg. But to be honest, the file format doesn’t matter a lot. I am a PNG supporter because png is the most commonly used format, but all the neural network sees is the individual pixels as neurons, so it really doesn’t care. but if you want compressed, use JPG, JPG wins in that regard.

  

  

Ok, back to the code

save the current frame as image and save the return value too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_ee038b118e247034.png)

and then we make the directories for the images to be stored if we have not already.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_4344e03064dbbef0.png)

and acutally this is a bit redundant, but it is done here, I can edit it after script is created to suit my own philosophy.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_f7cd70bd0a3e5b82.png)

after we make the directory, we will create our image inside the directory and then resize it, give it antialiasing so its more sharp and then save it. Then we just update the counters.

  

Then we are going to have our reset function to clear the directories.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_b992bd0468e35c8b.png)

so we will first iterate through all directories and then delete every file in every directory. Unlink is the same as delete. Acutally il just use os.remove.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_bfebeec6e7ee6cef.png)

then also reset the counters, the model( we didn’t get to that yet)

and reset the classification prediction text.

  

To the next function!

The update function exists to update the camera feed for ourselves each time. Remember how there is a viewport being shown in our tkinter, thats this function.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_b8b370d484136daf.png)

so we will have this autopredict feature as well. If autopredict is on, then we want it to predict every frame of the camera. We will work on the predict function later so this can work. For now put a pass.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_d44edaca1de2bbc.png)

don’t know exactly how this works. We will have our photo property for this class and also modify the canvas to include this photo which is anchored in the top left corner.

Lastly, we will make sure this function runs recursively after a delay.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_f235d090aa7a498c.png)

  

so there is only 2 functions that we have not completed.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_d78f07f640021362.png)

so lets get to that now shall we.

  

### Model

So we are using traditional machine learning which I did not expect. So no neural networks here, just a simple machine learning model. We use linear support vector which is quite good. We could have also used K-Nearest neighbours, random forest, or a neural network, the process is all the same.

We preprocess the images, turn them into numpy arrays, pass them into the model, fit the model, and then use the model for predictions.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_564bb43ce26f4a53.png)

then we have the class.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_ce7959213d9d7ff0.png)

the constructor will just make itself a model = linear support vector.

Then we will have 2 functions

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_cfe9df8fd2032e1c.png)

train and predict.

Making and using.

So in the train function we want to preprocess the data. We have X directories for each class which are filled with images that need to be processed. We need to get the images into the script, turn them into numpy arrays and also make sure that they are classified data that is labeled.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_400e3b22ff8d0672.png)

in our trainmodel function we will iterate through all of the images in every directory.

Now, we want to reshape the image into a numpy 1d array so that it can be fed into the model. To make it into a 1d shape, we will need.

To find that out, I make a quick script to take a quick pic.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_68ee30ae78a1dd0e.png)

then check the image dimensions of the image:  
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_b4d58092c203fcbe.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_4742831bf3231621.png)

640*480 = 307200

so then just reshape into that 1d shape

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_3e61795e0f4e3684.png)

when you are done that then add the image and class to the image list

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_f74ebf2efb389e36.png)

then we reshape image list to the amount of images we have. Then we fit it. Print a nice message for the console and we are done.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_80d329d2172393f6.png)

  

the predict method is made as such:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_df16fc0ebeb2ebfb.png)

we grab the image, preprocess it, reshape it, then predict from our just trained model.

And the thing is, in our app, we need to also make a function in our app that uses this predict method in this script. So lets do that redundant thing :/

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_b216e35a621711ee.png)

  

ok done with most of the stuff, now lets make the main script so we can run the app.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw11_tmp_c781b1d7fd4a9f83.png)

now lets run. Definitely some bugs I guarantee it.