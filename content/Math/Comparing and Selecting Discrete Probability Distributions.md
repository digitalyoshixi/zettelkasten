---
tags:
  - math
  - distributions
---
When to use each distributions?
# Uniform Distribution
### Parameters
n : number of possible outcomes
### Definition of Random Variable x
x maps a specific outcome to a probability
### Range of values for x
Dependent on event. 
If its a dice, its 6
If its a 4 color spinner, its 4
Depends, depends
### Probability Formula
P(X=x) = 1/n
### Expectation Formula
E(x) = $\sum xP(x)$
### Identifying Characteristics
All probabilities are the same
its $\frac{1}{n}$
# Binomial Distribution
### Parameters
n : number of trials
p : probability of success
q : probability of failure

### Definition of Random Variable x:
x is the number of specific successes
### Range of Values for x:
0 to n
### Probability Formula
P(X=x) = $_{n}C_{x}p^xq^{n-x}$
### Expectation Formula
E(X) = np
### Identifying Characteristics
- Bernoulli Trials
- Independent Trials
# Geometric Distribution
### Parameters
n : number of trials
p : probability of success
q : probability of failure
Exact same as Binomial Distribution
### Definition of Random Variable x:
Number of failures **before** a success
### Range of Values for x:
0 -> n-1
cause remember, it is **before** 
### Probability Formula
P(X=x) = $q^{x}p$
discrete### Expectation Formula
E(x) = q/p
### Identifying Characteristics
- Waiting time distribution. You are waiting until the success occurs
- Bernoulli Trials
- Independent Events
### Keywords
- Waiting for success to occur at a certain spot. Eg, win first try, win 2nd try.
- Fewer than
# Hyper Geometric Distribution
### Parameters
n : population
a : number of available successes
r : number of selections
### Definition of Random Variable X:
represents the number of successful selections
### Range of Values for x
0 to r
### Probability Formula
P(X=x) = $\frac{_{a}C_{x} * _{n-a}C_{r-x}}{_{n}C_{r}}$
### Expectation Formula
E(x) = ra/n
### Identifying Characteristics
- Dependent Trials
- Bernoulli Trials
