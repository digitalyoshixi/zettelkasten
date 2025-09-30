---
tags:
  - math
  - distributions
---
A [[Discrete Distribution]] used to model [[Independent Events|Independent]] [[Bernoulli Trials]] .
Uses [[Binomial Theorem]] in tandem with probabilities to get our probability distributions.
![[Binomial Distribution-20250930153414494.webp]]
# Probability in a Binomial Distribution
$P(x)=_{n}C_{x}p^xq^{n-x}$
- p is the probability of success on any individual trial. (eg. 50% a coin toss)
- q = 1 - p
- n = number of trials
- P total number of trials
- x = result
# Expectation Formula
$$E(X) = np$$
# Examples
### Example 1
heads probability 50%, tails probability 50%. probability distribution of flipping 3 times
**Note that h + t = 1. 100% divided up into probability sets**
$h = 1/2, t = 1/2$
$(h+t)^3$
##### Solution
$(h+t)^3 = h^3 + 3(h^2)(t) + 3(h)(t^2) + t^3$
\= (1/8) + (3/8) + (3/8) + (1/8)
first term is P(no tails), P(no tails) = 1/8
P(one tail) = 2nd term. P(one tails) = 3/8
P(second tail) = 3rd term. P(second tails) = 3/8
P(third tail) = 1/8

### Example 2
Flip a coin 4 times. GIve the probability distribution where 'T' is the successful outcome T = the number of Tails. What is the expected number of 'T's?

| T = t | P(T = 1) |
| ----- | -------- |
| 0     | 1/16     |
| 1     | =$_{4}C_{1} * \left( \frac{1}{2} \right)^1 * \left( \frac{1}{2} \right)^3 = \frac{4}{16}$ |
| 2     | =$_{4}C_{2} * \left( \frac{1}{2} \right)^2 * \left( \frac{1}{2} \right)^2 = \frac{6}{16}$         | 
| 3     | 4/16         |
| 4      | 1/16         |
This follows pascal triangle you see! If you add up all the probabilities, they should equal 1.
1/16 + 4/16 + 6/16 + 4/16 + 1/16 = 16/16 = 1!
The expected number is 2.

### Example 3
Game consists of rolling a pair of dice 10 times. for each sum that equals 6,7,8 or 2, you win 1 dollar. it costs 5 dollars to play the game. Is this a fair game?
##### Solution
n = 10
p = ...
cases for 7 : {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)} = 6 cases
cases for 6 : {(1,5),(2,4),(3,3),(4,2),(5,1)} = 5 cases
cases for 8 : {(2,6),(3,5),(4,4),(5,3),{6,2}} = 5 cases
6 + 5 + 5
total possibilities = 6^2 = 36
p = 16/36

E(X) = np
= 10 (4/9)
= 40/9
= 4.44

4.44 is smaller than 5 dollar. not fair!
