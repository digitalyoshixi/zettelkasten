---
tags:
  - uiux
---
A predictive model of human movement.
# Law
*Closer and bigger targets are easier to select than small and far ones.*
The time required to move to a target area is a function based off the distance to the target and the width of the target.
$$T = a+b\log_{2}(\frac{D}{S+1})$$
- $T$ is the time to move
- $a$ is the intercept where $T = 0$ (empirically derrived)
- $b$ is the slope (empirically derrived)
- $D$ is the distance
- $S$ is the size