---
tags:
  - machine_learning
---
The method to revise the [[Weights]] and [[Bias|Biases]] of a [[Neural Network|Neural Net]].
Back propogation is performed uniformly from all input types so that one category does not affect the weights/biases too much.
# Process
1. Find the expected activation for each neuron, compared to the actual activation, and store the value of the difference.
      ![[Back Propagation-20250628014727328.webp|288]]
2. To modify the activation, you can either:
	1. Change the bias of the current neuron, in proportion to 
	2. Change the weights of the previous neurons with respect to the activation of those previous neurons
	3. Change the activation of the last neurons with respect to the weights of those previous neurons (repeat this process for them)
	   ![[Back Propagation-20250628015143215.webp|387]]