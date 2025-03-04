---
tags:
  - python
  - machine_learning
  - machine_learning
  - machine_learning
  - machine_learning
---
We want to attribute a png of somebody’s face to a entity, and when you give a video feed of somebody else’s face, they will not be flagged as the same entity as the first face.

We want to install **deepface** library here.

Once we done that, import the following 3 libraries.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_6bcb0aa3158ef6da.png)

threading for more cpu threads to help. Cv2 for computer vision and deepface for facial recognition.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_13fc7a5429734f96.png)

next we have our cap. The cap will have a DSHOW type cap.

Set our height and width

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_79dc689b45b0f8e0.png)

  

Next we have 3 global variables

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_7fe070f1b9ef8512.png)

we want to have a frame counter. We want a image to be taken every 60 (or 30) frames. Then we have a boolean for if the face is matched and a reference image for face matching.

  

Next we have a while loop

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_847d5f8c4b1c5219.png)

the while loop will chek if there is a return value. ( we will make that block do something in a second). We also have a segment which detects user input of q, if it is q then we break out the while loop and destroy all windows.

  

Neuralnine promised In the ret block, he would show how to view our camera feed. Lets hope he keeps his promise.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_d94afc26524e0ed1.png)

ok, so in the code inside ret for now, we have to compare the frame to the face.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_d461338b4571150c.png)

check if we are on the 30th counter. We want a 1 frame per 30 activaiton.

Then, we want to give threads to a checkface function. We feed that function a tuple. The tuple is just containing one item which is a copy of our current frame. There is a comma there because we must feed it a tuple in the args parameter. We need that comma to make it a tuple.

  

We also have an exception.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_635851a9b6e01190.png)

the exception will catch a ValueError. This is just what deepface does, if it cant find a face then it returns ValueError. We don’t care about what happens when this error happens, we just pass.

Also increment counter will you?

  

Next, this is all optional but we have a caption underneath the video feed which will say MATCH!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_c1436551be69c325.png)

that is, if we get a match from the checkface function.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_119775e5fbe53a18.png)

you may see I also added a else. The colors are BGR, so 0,255,0 is green and 0,0,255 is red.

  

Finally, we show the camera feed. He kept his promise.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_cc7849f14d203e63.png)

the title of the feed is “THE VIDEO”

  

The checkface function is defined like thus:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_ae1fc3f6668027f4.png)

we check if we can do this:

if the frame is the same as the reference image, then we change face_match to be true, if not, then it is false still

again, this one can fail due to numerous reasons. Except value error in that case.

  

### Error fixing

So, the first error I fixed was the file location.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_737accecffeb3e0.png)

reference image should have a absolute path with raw string.

  

Then, what I needed to do was download this file from: [https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5](https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5)

the raw h5 file and put it in my C:\Users\Digit\.deepface\weights folder.

  

And then it works!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_e5b680712a0e17a8.png)

from this reference:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivvq_tmp_9fcaf262b18e222b.png)

it checks the nose, eye, mouth positions. If I open my mouth, it flags it as FRAUD!