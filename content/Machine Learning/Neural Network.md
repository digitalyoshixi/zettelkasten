---
tags:
  - machine_learning
  - data_science
---
# Theory
A neural network consists of multiple layers of neurons.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_6814aae2bc5d3614.png)

- First layer is called the input layer for the training and testing data
- Last layer is the output layer, what we expect as the output: a number a classification, prediction, and more
- Layers in between are hidden layers that add complexity and sophistication to the model

the network part is that every neuron of one layer is connected to every neuron of the other layer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_5319e1a7191b0709.png)

so in this case every neuron of the input layer is connected to every neuron in the second layer

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_541c3d49277f52ce.png)

  

You can think of the hidden layers as random in the beginning.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_6ca91024e622b072.png)

no real functionality

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_996df6dc82c4c892.png)

if we have a supervised model, we have our input as the training data and our output as the training classification

say we have a neural network that takes handwritten digits. The out layer would have 10 neurons since there can be 10 possible digits. If say the input we had was an image that represented the digit 8, and the output had the neuron for digit 2 be the one most activated, we would need to rework the hidden middle layers in between.

Also if say we gave it an input of a 28px*28px image(784 pixels in total), we would be giving the input layer 784 neurons.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_ca774cf6e1c994a8.png)

### Neurons

Every neuron has a certain input. It can be training data, testing data from the input layer or an output from a previous neuron.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_8cfdfd33a287f2f1.png)

every neuron has an activation function which takes input and according to the input, increments the activation value of the neuron/ the neuron’s brightness. Say if the neuron inputted 1, we increase the activation value by 0.9

every neuron as long as its not in the output layer as an output. They output to the input of every neuron on the other layer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_925d512b9198b66.png)

During the output though, the transfer will have a weight saying how important is this neuron’s output to the other neuron?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_56b85e4aa56e0ddf.png)

for some neurons the weight is high. Very important for this neuron.

For some, the weight is nothing, this neuron is very useless for this neuron.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_b6d8080b9d7231fc.png)

when we keep feeding data to the network, it trys to adjust these weights in order to make the model better. On an incorrect result on the output layer, it feeds back the info of this wrong result to adjust the weights so the next prediciton will be more accurate.

  

### Activation functions

A few possible activation functions include:

**softmax:** usually used in the last layer output layer. scales the layer down to 1 so that every neuron is a percentage out of 100%.  
**sigmoid:** turn every value into a value between 0 and 1. -8000 could be 0.0000001, 9000000 could be 0.9999999

**ReLU(rectified linear unit):** if the value is negative, then it is 0. if the value is positive, then we don’t change it

  

### Gradient descent

This is the algorithm that allows our neural network to be optimized. During the neural network execution, it will shift the weights, the biases of the neurons.

Say we have our number reading model again that is fed an 28x28 image with pixels of the 255 color scale.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_a4efe26711019bb7.png)

if we fed it the image of 2, then the idea case is that the output neuron corresponding to 2 would have a value of 1(100%) and the other output neurons to have a value of 0(0%). however, what is most likely the case is that we don’t get 100% and we don’t get the correct majority of the neurons to agree on the right answer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_9584635fda933108.png)

what happens then is we come up with a loss function. The loss function tells us how wrong our model is. Its not the error, the error would be the percentage of misclassifications. The loss function produces a value that tells us how off we were from the desired results. A higher loss value, the worser the model. So our goal is to minimize that lost value.

  

### Loss function

So the loss function requires the weights, biases and the desired outcome and it calculates how wrong we are.

It compares the results of the neural network with the results we should have gotten.

The loss function is a very high dimensional function thousand dimensional probably. This is just a general visualization, however it is not accurate to how the real lost function works.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_fb18a60ae26d80a7.png)

our loss value may lie somewhere here. With the black dot. The goal of the black dot is to be at the global cost minimum, where we have the least loss value and the model is most accurate.

So we want to roll down to the bottom. We want to roll down in the direction of the steepest descent. When we take the gradient of the loss funciton, it tells us the direction we need to go to get the highest increase. Just get the negate the gradient, and you will the direction for going down. In higher dimensions, it will be negated on all axis. So we go down a bit, adjust the weights and biases according to that position, and rerun the network.

  

For a loss function that looks like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivlf_tmp_1815e5b119f183b.png)

if we use that technique, we are only getting a local minimum. We are not getting the global minimum. Because of that, we may start randomly on a different coordinate to see what happens. Gradient descent finds the most optimal solution for the local minimum(hopefully it is global)

The question is, if we know where the local minima is, why don’t we just adjust the weights and biases directly according to it?

**The answer is, that, LET THE PROCESS HAPPEN. Learning is slow, we don’t just learn immediately. What you must understand is that neural networks work around patterns. Jumping directly to a point would be jumping the gun. Know that this is the local minima, not the maximum. Immediately jumping to that point will produce undesired effects like oscillation where the model repeatedly jumps between 2 or more points, never learning and being stuck in an infinite loop.**

Also, the graph changes depending on the training example… I think…. IDK!


older versions had the [[Perceptron Model]] version of neural networks. they are not so good anymore


## Neural networks quick!

[https://www.youtube.com/watch?v=jmmW0F0biz0](https://www.youtube.com/watch?v=jmmW0F0biz0)

think of every node as its own linear regression model. A linear regression model is a mathematical model used to predict future events. The weights between each node determine how much influence each input has on its output. You take the output value of one node, multiply it by the weight to get the actual value to pass to the next nodes, input.

The example is do we want to go swimming? There are 3 input nodes

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivmq_tmp_ef6bf438bf60ce46.png)

lets say all input nodes are binary. True or false. The first input node asks the question: are there waves?, the second asks: is it crowded? The third asks: are there sharks?

Lets say that node1 = True(1), node2 = False(0) node3 = True(1)

each of these nodes’s output will have their own weights aswell. Lets say we care a lot about of there are waves.

Weight1 = 5.

we don’t care too much if its crowded

weight2 = 2

and we care a bit if there are sharks

weight3 = 4.

then, just multiply the values of the nodes with the weights

output1 = 1*5 = 5, output2 = 2*0 = 0, output 3 = 1*4 = 4.

lastly, we subtract the threshold(bias), so the final value for our answer is 5+4+0 – 3(if 3 is the bias/threshold). Our tendancy to swim has a value of 6.

now for each run of this algorithm, it finalizes by checking with its loss function, adjusting the weights and biases to produce more accurate results in the end.

There are multiple types of neural networks aswell.

**ANN:** the most basic one with the feed-for algorithm

**CNN:** convoluted neural network. Better for image recognition

**RNN:** recurrent neural network. Uses feedback loops and better for predicting future events.

A bias is a threshold.Data is passed

## 3Blue1Brown Neural networks

A neuron is just a thing that holds a number. Specifically a thing that holds a number between 0 and 1. 0.1, 0.2, 0.8, 0.6, 0.9, 0.7 and so on.

For MSINT model, the network starts with 784 neurons that hold values between 0 and 1 for the black and white pixels.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_f93641e6b5acd611.png)

0 for black pixels, 1 for white pixels.

This number inside a neuron is called its **activation**

you can think of a higher(1) to be that this neuron is VERY activated, and 0 to be that this neuron is dead bruh.

For the output layer, each neuron also has these 0-1 activation values. Now they represent how likely this number is to be the right one

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_28aa0a7985b8fae5.png)

activations of one layer determine the activations of another layer. The hidden layer has a lot of experimentation, and it is where the real learning of the neural network is done.

### Why layers?

When humans recognise digits, It could possibly be done by breaking every digit into its specific componenets.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_274d30c4d6fc7d6b.png)

a 9 may have a loop at the top and a line, a 8 may have 2 loops, 4 has 3 lines.

In an ideal world, every neuron in the 2nd to last layer in the neural network corresponds to one of these components.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_956df1a76f485261.png)

and everytime you feed a number with a loopdeyloop at the top, a specific neuron corresponding to that component lights up.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_bf55d25678ed4df.png)

and we don’t want it to be specificly a loop that looks like that. We want any generally loopy pattern to trigger that activation.

The question is how can we even know this is a loop?

Maybe the machine can classify a loop as a lot of small edges linked together.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_40505ac50c7b1e2f.png)

maybe the machine can classify a long line as a bunch of edges that retain similar vector directions

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_2a3d8d23b7623c65.png)

so our hope is that every neuron in the layer before the 2nd last hidden layer corresponds to one of these small edges.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_eb8c6f84e7bdf77a.png)

so maybe if we feed it a 9, it lights up all the neurons corresponding to specific little edges

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_7fbe4cef629ec1d6.png)

and in turn, those collection of little edges light up the bigger loop and long line nodes.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_f85b5487fea29c12.png)

and that big edge and big line light up the output neuron of 9 the most.

So our hope is that the neural network works something similar to this. Break down edges and patterns to help with image recognition.

Like a speech reader may take the raw audio, get the letters, turn letters into syllables, then turn syllables into words.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_478825aa6121e9bd.png)

  

### Parameters

So lets say we want a specific neuron in the 2nd layer to be able to detect if this specific edge is in the image:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_ea9382b5d03245d2.png)

what parameters would be need? What dials and knobs should we be able to tweak so that its expressive enough to capture this pixel pattern?

What we will have are weights in the connections of this neuron and every neuron of the first layer.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_6d95263416935833.png)

the weights are numbers. Then, take the activations of all those neurons * their weights and add them.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_ac6b2a0af574bc65.png)

lets say only these pixels mattered:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_75161e24ef3a3a65.png)

(the ones in green). All neurons that are not those pixels do not have high weights, all neurons that are the green pixels will have awesomely high weights.

You might also have some negative weights in the area around the positive weights, to say that we want exactly it to have pixels like these.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_2645ed7284cfa648.png)

the goal is that when the sum is largest, that is the perfect example of the edge we want. And that is when the hidden neuron lights up the most. That can only happen if the pixels in the last layer line up corresponding to the weights.

But remember, activations should be in between 0 and 1! if you add these weights like this, then you may end up with any negative or positive value!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_a3c042c7c49ede00.png)

what we have then is specific activation functions. The activation functions squish to make the values between the range of 0 and 1.

the sigmoid is the most common one.

The very final step is the bias. Say the neuron lights up tooo much! We need a threshold/bias. Maybe make it only light up if the weight value is over 10!

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_e984de976a9bd83c.png)

so the bias is a subtraction from the weighted sum. weight1+weight2+weight3…. - bias. Then run it through the activation function. The bias tells how high the weighted value needs to be so that the neuron can be meaningfully active.

And every neuron has this. Every neuron has their own weights for each neuron in the previous row. Also each ones have their own biases too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivms_tmp_71a9ee88a544a904.png)

like say we have 784 neurons in the first layer, and then 16 in the following hidden layer. That is 784*16 weights and 16 biases for the 1st hidden layer!

So learning is just the process of adjusting each weight and bias correctly so that the model can produce the correct results.

Soo much of neural networks is just linear algebra LEARN that.

  

You can really think of a neuron as a function that takes in all of the outputs of the previous layer and outputs a single number from 1 to 0.

the entire network really is a function that takes an image and returns a number from 1 to 10.

### ReLU vs sigmoid

Sigmoid is slow, ReLU is fast. 

Sigmoid is the function 1/(1-e^x). it looks like this.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivu4_tmp_4a12fb699aacb66c.png)

it is between 0 and 1.

a large value will never reach 1, a super small value will never reach 0. touching by a hair margin.

  

ReLU rectify linear unit is also used a lot! Its simple.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivu4_tmp_b2f96d10ae15746a.png)

### Back propogation

The next step and final step in the neural network is using the lessons learned from gradient descent and backwards propogating to change the weights and biases.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivtz_tmp_356244d693352b86.png)

so again, we have this neural network with cats and dogs. The value of the cat is 0.7 and the value of the dog neuron is 0.3. however, we know it should be 100% for cat and 0% for dog. Thus, the machine knows this and adjusts the weights and biases backwards. We adjust the weights and biases in the previojs layers. For example, if there is a neuron in the previous layer that added positively to the dog value, we might want to adjust the weight a bit to make it less trigger happy on the dog value.

And so we might have the corresponding following layer look like this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivtz_tmp_f8aee1650f3e01d4.png)

and we say, ok, we want to increase the top one’s weights for cat, decrease top ones weights for dog, increase the bias since its sending too little.

Then we see in the next following layer, and we ask the question, what neurons do I change to make the previously altered layer look like that?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivtz_tmp_154522aae6686466.png)

maybe its negative to a few bias, positive to a few weights, so on so forth.

  

Also, know that those modifcations occur because of one testing example, we may have another testing example we give it and the output is radically different.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivtz_tmp_49d5e2dbca22f51f.png)

and so, we modify slowly, surely, until we are perfect

