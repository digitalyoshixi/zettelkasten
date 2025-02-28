---
tags:
  - machine_learning
aliases:
  - LSTM
---
A type of [[Recurrent Neural Networks]] that is designed to prevent the [[Vanishing and Exploding Gradient Problem]].
# Process
1. Nodes no longer have weights and biases
   ![[Long Short Term Memory-20250228035127976.webp]]
2. A state that represents the long-term memory connects all nodes
3. A state that represents short-term memory connects all nodes with a weight connecting to each mode
4. ![[Long Short Term Memory-20250228035346266.webp]]
	   1. Input is first passed into short-term memory
	   2. Input is multiplied by weight
	   3. Short term memory is multipled by another weight then added to the input's weighted value
	   4. Passed into activation function
	   5. Activation function output represents the percentage of the long-term memory to be remembered