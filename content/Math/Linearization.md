---
tags:
  - math
  - calculus
aliases:
  - Tangent Line Approximation
  - Linear Approximation
---
Tangent lines can be used to approximate functions.
Given a function that is not currently linear, it can be approximated with:
$$L(x)=f(a)+f'(a)(x-a)$$
This is pretty much the [[Instantaneous Rate of Change|Tangent]]
Observe that when x is close to a, $f(x)$ is close to the $L(x)$

# Example
If you wanted to linear approximate at $f(8.1)$, then you can get the linear approximation at $L(8)$ to approximate $L(8.1)$
![[Linearization-20241128143504461.webp]]
1. Find a point close to 8 - say 8.1
2. Get the tangent equation for points close to 8. This is $L(x)=f'(8)(x-8)+f(8)$
3. $f(8.1) \approx L(8.1)$
4. Judge approximation is over or under by checking concavity at 8.1. 
	1. Concave up -> approximation under
	2. Concave down -> approximation over
