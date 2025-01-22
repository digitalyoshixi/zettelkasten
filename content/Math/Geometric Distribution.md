---
tags:
  - math
  - distributions
aliases:
  - Waiting-time_Distribution
---
You are waiting for a time of something to occur

Examples include: 
- In some board games, you cannot move forward until you roll a specific number. and that could take several tries.
- Manufacturers of products like switches, relays and hard drives need to know how many operations their products can perform before failing.
The critical quantity in this situation is called the waiting time or waiting period. the number of
trials before a specific outcome.

### Binomial similarities
A geometric distribution has a specified number of independant trials with 2 possible outcomes following [[Bernoulli Trials]]. SAME AS BINOMIAL

### Binomial Differences
In a geometric distribution, the random variable is number of failures before the sucess occurs
In a binomial distribution, the random variable is number of trials


# Probability distribution formula
P(x) = q^x \* p

p = probability of success.
q = probability of failure
x - random variable for number of failures before success occurs. usually its success - 1.

# Expectation formula
E(x) = $\sum\limits_{x\to0}^\infty = xP(x)$
= q/p
### Example
Calculate the probability distribution for getting out of jail in MONOPOLY in x rolls of dice.
p  = 6/36 = 1/6
q = 5/6
E(x) = (5/6)/(1/6) = 5
5 tries before getting a success

# Geometric Distribution
Why is it called geometric distribution?
Lets to an example
### Example
p = 0.1
q = 0.9

| x   | P(x)                  |
| --- | --------------------- |
| 0   | 0.9^0 \* 0.1          |
| 1   | 0.9^1 \* 0.1 = 0.09   |
| 2   | 0.9^2 \* 0.1 = 0.081  |
| 3   | 0.9^3 \* 0.1 = 0.0729 |
 
These numbers are a sequence
literally $ar^n$


