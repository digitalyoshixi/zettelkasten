---
tags:
  - machine_learning
  - machine_learning
  - machine_learning
---
A neural network model that is outdated and sucks, nobody uses it anymore. For a neuron, instead of increasing the activation we start with a bias value and for every input instead of increasing the bias, we subtract from the bias. Same sort of logic, but it is more stupid like who wants this?

[https://pabloinsente.github.io/the-perceptron](https://pabloinsente.github.io/the-perceptron)

It was a relic of its time. The early form of a neural network developed by McCulloch and Pitts was rudimentary. It was able to emulate a wide variety of boolean functions using only binary methods. However, this model lacked the characteristics of a biological model such as the complex connectivity patterns and continuous values(rather than binary) and most importantly, a learning procedure. The brain is stochastic, its noisy and unpredictable compared to the structured, predictable nature of McCulloch and Pitts’ model.

Rosenblatt introduced his model the perceptron in 1958. he thought that to understand the mind of higher organisms(like us!), they would need to answer 3 questions.

1. detection
    
2. storage
    
3. effect of stored information on future perception and behavior
    

Rosenblatt sums us detection as relative to our physiology.

The following 2 problems of storage and effect are talked about more below.

  

### Information Storage problem

Rosenblatt says there are 2 approaches to this problem. The coded representation and the connectionist approach.

The coded representation postulates that sensory information is stored in coded representations and that there is a 1-1 mapping of sensory stimuli and a stored pattern.

The connectionist approach says that there is no such thing as records of information in your brain, no memory pattern is imprinted from stimuli. Instead memory is stored as a preferences for a particular response instead of topographic representations. By response, Rosenblatt means the electrochemical and behavioral response from a stimuli.

Think about it in this manner: there is no unique cluster of neurons, wired in an invariant manner, that “code” the memory of a triangle. What we have instead, is a series of associations among an unprecise set of neurons, that -importantly- “tend to react” in the presence of any stimulus that looks like a triangle.

  

### The effect of stored information on future perception and behavior

Once I have the concept stored in my brain, how does having such information in my brain impact my reaction to it? From mental and behavioral response.

The coded construction will say we use 2 processess. One that recognises this is what we know, and the other that controls the reaction. The one that controls the reaction must be connected to each stimulus.

The connectionist will say that the responses and stimulus get blended into one. The response will use the same activitiy patterns which activated the stimulus.