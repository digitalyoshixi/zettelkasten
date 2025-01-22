---
tags:
  - math
  - distributions
---
# Example 2
What is the probability that a second tail occurs on the 6th toss of a fair coin?

##### Answer
there are $_{5}C_{1}$ ways for a tail to occur in the first

the probability of the second tail, P(x=2) means that one of the first 5 is tails, and we get tails for the final one.
$P(x = 2) =  _{5}C_{1} \left( \frac{1}{2} \right)^4\left( \frac{1}{2} \right)^1 * (\frac{1}{2})$
That is, 5/64.

# Example 3
A quiz given. each question requires a true, false or cannot tell responses. The quiz has 10 questions in it.
a) what is probability that Fermin will get exactly 6 questions correct if he only guesses
##### Answer
P(x=6) = $_{10}C_{6}(\frac{1}{3})^6(\frac{2}{3})^4 = 0.0569$

b) what is probability that his first question he gets right is the third question?
##### Answer
$(\frac{2}{3})^2(\frac{1}{3})=\frac{4}{27}$

c) what is the excepted number of correct questions that Fermin will guess?
##### Answer 
p = 1/3
E(x) = n \* p
(10)(1/3)
E(x) = 3.333333333



# Example 4
standard 52 deck. if you draw a face card, win 10 cents. if you draw ace card, win 25 cents. if you draw anything else, you lose 5 cents.

This is not a probability distribution because there are multiple win conditions going on.

But the E(x) = (3/13)\*10 + (1/13)\*25 + (9/13) \*(-5) 
= 1
