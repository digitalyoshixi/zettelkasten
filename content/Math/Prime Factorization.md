---
tags:
  - math
---
To find all the factors, of any number, you will need to find a set of prime factors.
This is a [[Polynomial Time]] algorithm
![[Pasted image 20231002191712.png]]
This works for all numbers.
The set of prime factors will **Always** be the same
# Finding Sets Example
For the number 21, I am to find all the prime factors of it
![[Pasted image 20231002192024.png]]
The prime factors are: 2,3 and 3
this works if I chose other prime factors in different steps too.
![[Pasted image 20231002192153.png]]
3,2,2. same set.
## Finding the factors
{2,3,3} is the set. 1 is also in the set
Mutliply every number in the set with every other number all possible times to get all factors.
1 \* 1 = **1**
2 \* 1 = **2**
3 \* 1 = **3**
2 \* 3 = **6**
3 \* 3 = **9**
2 \* 3 \ * 3 = **18**
factors are: 1,2,3,6,9,18

# Finding Perfect Square Factors
Say you have a number 3600, you want to get all perfect square factors.
The prime factorization of 3600 is $2^4*3^2*5^2$
A perfect square occurs when the degrees of the terms are even.
So $2^0*3^2*5^2$ or $2^4*3^2*5^0$ as examples, there are a lot more.
