---
tags:
  - math
aliases:
  - NonExclusive
  - Exclusive
  - Inclusive
---
Deals with boolean operators like OR,AND.

**OR**: Probability that either of the 2 events occur
**AND**: Probability that both events occur.
### Examples
Probability that dice roll results in 2 **OR** 5. the OR operator tells us to add the 2 probabilities of either case. so, 1/6 + 1/6 = 2/6 = 1/3.
Probability is 1/3

# Mututally Exclusive Events
Venn diagrams.  

![[Pasted image 20230908142857.png]]
What a mutually exclusive means is that there is no shared probabilities between these 2 cases.
There is no intersection between the 2 classes.

- Events that have different attributes
- Cannot occur simultaneously

## Probability of Mutual Exclusive Events
picnic basket 3 3 ham, 2 turkey, 4 egg.
probability that random choose either ham or egg?

**Solution:**
P(H or E): 3/10 + 4/10 = 7/10
# Non-Exclusive Events
So, in this example, we are asking the number of cards that are diamond, face card or both.
The thing with face cards is that they can also be a diamond card. 3 in fact.
So, there is an intersection here
![[Pasted image 20230908143354.png]]
We can add # of diamonds and # of face.
13 diamonds and 12 faces. BUT 3 cards dJack, dQueen and dKing occur in both sets.
so, you must remove those 3, because you would be counting them twice which is illegal.
so, 13 + 12 - 3 = 22.

# Additive Principle (Rule of Sum)
### Mutually Exclusive Events
the probability of either two mutually exclusive events. A or B is:
P(A or B) = P(A) + P(B)

### Non-Exclusive Events:
Similar, but you need to take the probability of both occurring.
P(A or B) = P(A) + P(B) - P(A and B)
