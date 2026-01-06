---
tags:
  - math
---
The big one. Culminates everything we learned.
## Probability using permutations
1 older bro, 1 younger bro, 5 other racers. what is probability that older bro first lane, younger bro in 2nd lane?
$_{7}P_{2}$ = 42
only 1 case where older bro is first, younger is second.
1/42 
## Probability using Combinations
group of 3 members selected from 5 doctors and 7 technicians. what is probability that focus group comprised of doctors only?
$n(S)$ = $_{12}C_{3}$ = 220
$n(doctors)$ = $_{5}C_{3}$ = 10
10/220 = 1/22.

## Probability using fundamental counting principle
### Birthday Question
what is probability that 2 students out of a class of 24 have same birthday?
n(s) = 365^24. total possibilities
365 days in a year.
24 students.
Student permutations:
order matters, we decide a different birthday for different people.
$_{365}P_{24}$ = 1.44e^61
The probability that they have different is: $\frac{_{365}P_{24}}{365^{24}}$ = 0.4617
So, the probability they have same is: 1 - 0.4617 = 0.5383
53.83% likelihood.

### Question 2
52 cards, 13 dealt to each player. Probability that our hand is entirely heart cards?
$n(S)$ = $_{52}C_{13}$ 
$n(e)$ = $_{13}C_{13}*_{39}C_{0}$ = 1
$P(e)$ = $\frac{1}{_{52}C_{13}}$
Very low

