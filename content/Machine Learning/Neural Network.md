---
tags:
  - machine_learning
  - data_science
aliases:
  - Neural Net
---
A neural network is a [[Stochastic Algorithm|Probabilistic Algorithm]] created by [[Differentiable Programming]] comprised of nodes with weights and biases generated.
# Types
- [[Recurrent Neural Networks]]
- [[Convoluted Neural Network]]
# Theory
![[Neural Network-20250628005102541.webp]]
A neural network consists of [[Layer|Layers]] of [[Neuron|Neurons]] that are activated depending on their [[Activation Function]] and the total input value calculated by the [[Weights]],[[Bias]] of previous input layers. 
This process is repeated until we compute the output neurons in the final layer for practical use.
Weights and Biases are later refined during [[Gradient Descent]] by [[Math/Back Propagation]] in the training phase.
# Concepts
- [[Neuron]]
- [[Layer]]
- [[Activation Function]]
- [[Math/Biases]]
- [[Weights]]
- [[Loss Function]]
- [[Gradient Descent]]
- [[Back Propagation]]





So we want to roll down to the bottom. We want to roll down in the direction of the steepest descent. When we take the gradient of the loss funciton, it tells us the direction we need to go to get the highest increase. Just get the negate the gradient, and you will the direction for going down. In higher dimensions, it will be negated on all axis. So we go down a bit, adjust the weights and biases according to that position, and rerun the network.

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

