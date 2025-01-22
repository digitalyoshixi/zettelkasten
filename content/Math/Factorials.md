---
tags:
  - math
aliases:
  - Factorial
---
A **!** FOR FACTORIAL
multiplies the number by each natural number below it.
`n! = (n)(n-1)(n-2)...(1)`
so, `4! = (4)(3)(2)(1)`

**You can only have integer factorial numbers**
`n >= 0`
0! = 1. Because there is only 1 arrangement for 0 objects

## Dividing factorials
dividing factorials is easy because each factorial may have other factorials inside it as factors.
For example:
```
10!/8! 
= 10*9*(8*7*6*5*4*3*2*1) / (8*7*6*5*4*3*2*1)
= 10*9 / 1
= 90
```
### Factor factorials
```
8!/(5!2!)
= 8*7*6/(2!)
= 8*7*6/(2)
= 8*7*3/1
= 186
```
Divide by big factorial first, then slowly work with the small factorial.

### Factorial base changing
If you have a bad factorial base, you can just multiply the numerator and denominator with same factor
```
7!/(2!5!)
= 7!/(2!5!) \* 3/3 = 
= (3*7!)/(3*2!5!)
= (3*7!)/(3!5!)
```

### Factorial simplifying
```
(n-1)!(n^2+n)
= (n-1)!(n)(n+1)
= (n+1)!
```
```
(n!)/(n-2)!
(n)(n-1)(n-2)! / (n-2)!
(n)(n-1)
n^2 - n - 20 = 0
quadratic formula: n=5,-4
n != -4. cannot negative factorial
n = 5
```

[[Reverse Factorials]]
