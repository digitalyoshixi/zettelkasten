---
tags:
  - neural_networks
  - meta
  - machine_learning
  - machine_learning
---
[https://cs.stackexchange.com/questions/58131/are-neural-networks-a-type-of-reinforcement-learning-or-are-they-different](https://cs.stackexchange.com/questions/58131/are-neural-networks-a-type-of-reinforcement-learning-or-are-they-different)

There are 5 problems you can distinguish in machine learning:

**Regression**: Predicting a continuous variable

- You have a photo of a person and you want to tell how old the person is (e.g. howhot.io)
    

- **Classification**: Predicting a variable with finite possible values
    
    - MNIST: You get a 28px x 28px image. You know it is either 0, or 1, or 2, ..., or 9. So a digit. You have to say which one.
        
    - ImageNet: You get a bigger image. You have to decide which one of a 1000 classes it is (dog, cat, car, house, ...). You can be sure it is one (and exactly one) of those.
        
    - [http://write-math.com](http://write-math.com/): Classify a handwritten symbol into about 380 classes
        
    - [https://howhot.io/](https://howhot.io/): Classify gender
        
- **Clustering**: Grouping data
    
    - You have a lot of portrait images (or crops of images). You know there is exactly one persons face on it. You don't know how many people there are in total. Now you would like to group it so that each group is one person.
        
    - Species: You properties of animals and you want to group them. So you want a hierarchical clustering which puts closely related animals (dogs, cats; fly, moscito) closer together than not related ones (dogs, flys)
        
- **Collaborative Filtering**: Filling gaps
    
    - Netflix: You have a lot of movies, a lot of ratings. However, not every person rated every movie. In fact, probably no person did. But you want to fill the gaps so that you can tell the users which movies they should watch because they will probably like it.
        
    - Amazon: pretty much the same as with Netflix, but for all kinds of products
        
- **Reinforcement learning** (RL): Learning with environment
    
    - Self-driving cars
        
    - Playing games (e.g. Backgammon, Go, [Atari](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) ([video](https://www.youtube.com/watch?v=V1eYniJ0Rnk)))