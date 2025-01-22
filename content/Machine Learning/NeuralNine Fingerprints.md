---
tags:
  - NeuralNine
  - neural_networks
  - machine_learning
  - machine_learning
  - python
---
## NeuralNine finger print recognition

We will make a program to find who’s fingerprint is this?

  

### Dataset

We will be using a kaggle dataset finally!

[https://www.kaggle.com/datasets/ruizgara/socofing](https://www.kaggle.com/datasets/ruizgara/socofing)

we use a fingerprint dataset from somebody

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_8cd8def6361c330e.png)

now, in this dataset we have 2 folders. One is altered data, so somebody has their fingerprint defected. Some computer drew some strokes on the finger. Another is real which has real fingerprints.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_d32a67386a3d76f8.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_9c94a15408e5568e.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_fb71f03ef3592199.png) ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_6254fc2f825e9f57.png)

Real → altered fingers are shown above

  

I don’t know the context as to if these altered fingerprints are going to be counted as true human fingers or not, I believe they sohuld be because it kind of looks like the finger is pressing down on the camera.

Lets wait for the actual program to see for certain.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_b02ed672c52c2a2.png)

there datasets are always ginormous.

Once downloaded, lets put it inside of the same folder as our python program

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_8631503f8f98f4ac.png)

SOCOFing

weird how there is a SOCOFing folder inside of another SOCOFing.

  

### Understanding SOCOFing

[https://arxiv.org/ftp/arxiv/papers/1807/1807.10609.pdf](https://arxiv.org/ftp/arxiv/papers/1807/1807.10609.pdf)

the Sokoto Coventry Fingerprint dataset consists of 6,000 images of fingers from 600 africans. The images vary in gender and have 3 types of alterations. Obliteration, central rotation and z-cut. They are all denoted as Obl, CR, Zcut.

Below is an example of each:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_b420b179e160018e.png) central rotation. Part of the finger is rotated

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_c14963afb82c2790.png) obliteration. Some of the finger is noised.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_a9219381b00644f4.png) Zcut. Some marking of a finger cut I guess. Very sloppily done.

  

All the files are in bmap too

there are also difficulties in the alterations.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_2ca5ae57b9efce57.png)

Easy medium hard.

Depending on the difficulty, the alterations will be more intense. Hard has the most striking differences from the original.

Fingerprints are very complex and unique, its extremely unlikely to find 2 fingerprints that are the exact same. Thus, we are able to find a specific fingerprint regardless of the defects.

  

### Programming

The we need 2 libraries. Os and cv2

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_733999f556911757.png)

im going to load in an image then im going to print it. It should be a numpy array of 255 color.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_2e64c587e6931bb9.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_f7084caf7c70cbd8.png)

and yes it is.

The image I chose looks like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_66e7640b602a01f9.png)

it 19th subject’s left thumb with a central rotation applied.

Note that this is a modified image. We give it a modified image, it tries to find the original image.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_eb5d6371b895c05d.png)

we have 2 variables imageguess and filename.

We also have a few variables for common similarities between the 2 images.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_70109694b8c9e0db.png)

2 keypoints and 1 matchpoint variable to compare 2 images always. And through those variables, we will receive a score. We check the similarity score of the current image with the sample image to see if it beats our previous bestmatchscore.

  

Then, we want to go through all the files and then check each one if they are similar to the sample image.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_3ceead8a501c672.png)

there are in total 6,000 images. Windows file sorting will make it so that the more lowvalue digits there is, the higher it is on the sorting hierarchy. So 11 would be greater than 2. like I only have person no# 19, but I need to list around 2000 files to actually get there, like if it was following normal commonsense sorting then it would be 190 I believe.

Just know that file is a string for the filename. Its not a file location. Its just a string for the filename. In order for us to read the image, we need to append the directory(relative) to it.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_e02e2362e2cca8e9.png)

and above code will print all the file images.

Ok remove the printing section, all we need is the cv2 image read line

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_7d57e44ca27ac1f7.png)

ok, next we want to create a SIFT object. SIFT is **Scale Invariant Feature Transfer**. [https://en.wikipedia.org/wiki/Scale-invariant_feature_transform](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform)

this will get us to find all the differences between the 2 images through finding keypoints.

SIFT keypoints are gathered through comparing the sample image to our 2000 original images and finding features based on euclidian distance of the feature vectors. Sets of keypoints that agree on location, scale orientation will tally up and contribute to an overall confidence rating. We find the correct image based on the confidence rating.

So, we make the sift mask like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_19e328b555b259df.png)

keypoints are interesting and unique structures in the image, descriptors are descriptions of these keypoints. Lets make them like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_45c6373ef13845fd.png)

so we get our keypoints from the sift. One for the sample image, and another for the real image we are comparing it to.

Next, we match the keypoints. We use Flann which is fast library for approximate nearest neighbours.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_7b10cdeeed4abc3f.png)

Algorithm 1 for KD tree data structure. Aswell as 10 trees for the algorithm to use. We have a knn match with 2 k for the 2 keypoints aswell as their descrptors.

Before we go further it is a good idea to understand SIFT a bit more.

  

### SIFT

SIFT is used for object recognition. Finding similarities between 2 objects through use of keypoints.

Keypoints are specific points on an image that have a unique visual characteristic that would not change much if scaled, rotated or illuminated more. Keypoints are often found in the SIFT algorithm from applying a DoG(difference of gausiun) pyramin and finding the local extremas.

Descriptors are the numerical representation of the local image AROUND the keypoint. Typically a histogram of gradient orientations of the image patch around the image.

To match keypoints between different images, you need to compare the descriptors of keypoints from one image with the descriptors of keypoints from another image. Commonly we are using distance to compare 2 images.

  

  

Ok back to the code.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_11c216c6ba563b31.png)

this is what we have next. We want to parse through our matches and make a list of the close matches. Our threshold is that the difference between 1 distance to another has to be less than 10%.

next we want a keypoint quantity. Note we are SIFTing 2 images so the 2 images may have different quantity of keypoints. We get the smaller number of keypoints to make parsing a lot easier.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_5a199183056cc2db.png)

we will always want the image with the smaller # of keypoints to use as our keypoint quantity.

  

Then, almost there. We want to check the similarscore of this image to that of the best score.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_a39c9fae2d6f1b20.png)

update the file, the imageguess, acutally you don’t even need the imageguess I believe.

  

Ok last thing.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_1534bde00999ab2c.png)

print the best match score and show the matches of SIFT. And then show the image.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_d4b264fa5cf3158a.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivw6_tmp_194cdab2f43d7e54.png)

Cool I guess.****