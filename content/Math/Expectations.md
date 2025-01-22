---
tags:
  - math
  - distributions
aliases:
  - Average
  - Mean
---
An expectation of value E(X) means the expectation or average 

It is calculated through different means
Probability has everything to do with expectations

### Fair game
The Expected value of a fair game is 0.

# Expectation Formula
For every P(x) of a random variable X, we multiply outcome X with the P(X), then add each of these together.
a\*P(a) + b\*P(b) + c\*P(c) ... = Expectation
### Example
A game involves rolling a die. A player who rolls an even number recieves coins equal to 2\* roll. For odd, you lose 3\*roll.
For this game to be a fair game, the expected value must be zero. Is it a fair game?

| Roll | value, x | P(x) | x\*P(x) |
| ---- | -------- | ---- | ------ |
| 1    | -3       | 1/6  | -3/6       |
| 2    | 4        | 1/6  | 4/6       |
| 3    | -9       | 1/6  | -9/6       |
| 4    | 8        | 1/6  | 8/6       |
| 5    | -15      | 1/6  | -15/6       |
| 6    | 12       | 1/6  | 12/6       |
$-\frac{3}{6} + \frac{4}{6} + -\frac{9}{6} + \frac{8}{6} + -\frac{15}{6} + \frac{12}{6} = -\frac{1}{2}$ Not a fair game. Its not zero, its -1/2

For an event that says something like: If you roll a one, roll again, then the value of '1' is zero. Its does not affect the x\*P(x)
