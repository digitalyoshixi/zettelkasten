---
tags:
  - math
---
https://math.stackexchange.com/questions/171882/is-there-a-way-to-reverse-factorials
A method of finding the [[Factorials|Factorial]] from a given number.
For number **n**, keep dividing by natural numbers 1->inf, increasing the natural number each division until you reach a **number >= 1**.

# Examples
## Example 1
With a perfect factorial like 5040:
```
5040/1 = 5040
5040/2 = 2520
2520/3 = 840
840/4 = 210
210/5 = 42
42/6 = 7
7/1 = 1
```
In this case, the factorial is 7!
## Example 2
With a number not perfectly factorialable like 60:
```
60/1 = 60
60/2 = 30
30/3 = 10
10/4 = 2.5
2.5/5 = 0.5
```
For this case, there is no factorial for 60, the closest is 5! which is 120.
