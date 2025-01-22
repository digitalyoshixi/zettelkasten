---
tags:
  - math
  - distributions
---
# Example 1
The probability of tossing a head with a weighted coin is 0.4, if the coin is tossed 60 times, what is the probability that:
a) 10 or fewer heads are tossed
b) exactly 20 heads are tossed
### Solution a):
n = 60
p = 0.4
q = 0.6

Can we use normal approximation? np = 24 > 5. YES
P(x<=10) = P(x < 10.5)
$\sigma$ = $\sqrt{ v a ri a n c e }$
$v a r i a n c e = n p q$
$v a r i a n c e = 14.4$
$\sigma=3.8$

now convert the x score to the z score
P(x<10.5)
P(z<$\frac{10.5-24}{3.8}$)
P(z<-3.55) = 0.00019262
This is almost zero.

### Solution b):
P(x=20) = P(19.5<x<20.5)
z-score area:
P(z<zscore of 19.5) = P(z<-1.18) = 0.119
P(z<zscore of 20.5) = P(z<-0.92) = 0.17879
P(19.5<x<20.5) = 0.17879 - 0.119
						 = 0.05979

When you use BP P(x=20), you get 0.0616. not too bad. almost 0.02 off, very damn close

# Example 2
A student is writing a true-false test. if he is answering 10 questions, what is the probability that he will answer 3 or less questions correctly
### Solution
Can we use normal distributions?
n = 10
p = 0.5
q = 0.5
np = 5. 5 is not > 5.
WE CANNOT USE NORMAL DISTRIBUTION.
WE MUST USE BINOMIAL DISTRIBUTION
use [[Binomial Distribution]] to solve it.
BD: P(x<3) = P(x=0) + P(x=1) + P(x=2) + P(x=3) ...

# Example 3
Eric rolls a dice 100 times. what is pribability that he will roll a sum of 7 between 10 to 15 times?
n = 100
p = 1/6
q = 5/6
np = 100/6 > 5
P(10<=x<=15)
turn to continuous interval
P(9.5<=x<=15.5)
find z scores
z score of 9.5 = -1.92
z score of 15.5 = -0.31
Always the bigger number first.
P(z<-0.31) - P(z<-1.92) = 0.6274 - 0.3783 = 0.3509

# Example 4
What is the probability of rolling more than 10 "3"s when rolling a dice 100 times?
p=1/6
q = 5/6
n=100
100/6 > 5. we can use continuous
P(x>=10) to continuous interval is: P(x>9.5)
z-score of 9.5 is: $\frac{9.5-\left( \frac{50}{3} \right)}{\sqrt{ 500 }/{3}}$ 
...
0.7967
79.67%
