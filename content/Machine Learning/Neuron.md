---
tags:
  - machine_learning
  - statistics
---
This is the cell of a [[Neural Network|Neural Net]].
Holds an activation which is a continuous number from $0$ to $1$.
- A neuron is 'lit up' if its activation is 1
- A neuron is 'dark' if its activation is 0
![[Neuron-20260206224206179.webp]]
# Activation Formula
$$n = f(w_{1}n_{1} +\dots + w_{k}n_{k} + B)$$
Where:
- $n$ is the current neuron's activation
- $n_{1},\dots,n_{k}$ are all the previous neurons in the last [[Layer]]
- $w_{1},\dots,w_{k}$ are [[Weights]]
- $f(\cdot)$ is the [[Activation Function]]
- $B$ is the [[Machine Learning/Bias]]
# Example
![[Neuron-20250628010813725.webp|272]]
For a given image, a neuron could represent a single pixel's light. Then, [[Layer|Layers]] could be used to represent each row of pixels in the neural network.
# Neurons as Features
The hope for a neuron is that it is able to represent some tangible feature of an output. Like a loop of an image is from one neuron. [[Neuron Superposition]] attempts to disprove this.
![[Neuron-20250628011301449.webp]]