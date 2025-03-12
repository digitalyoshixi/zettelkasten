---
aliases: 
tags:
  - math
---
# $\lim_{x\to a}f(x) = L$
Its a notation to signify the y value that you get when you x approaches a value.
The value of f(x) can be made arbitrarily close to L by choosing x sufficiently close to a but not equal to A
See [[Limits Formalized Definition]]
# Why Limits?
### Limits Can Exist At Discontinuities
![[Pasted image 20240205142812.png|344]]
A limit would exist at this discontinuity. The left limit will have the same value as the right limit.
# Finding Limits
### Existence Hints
A limit exists if:
- A valid coordinate exists
- A valid hole coordinate exists. Limits exist at holes
They do not exist if:
- Single limits $\lim_{x\to a^{-}} \neq \lim_{x \to a^+}$
	- There is a asymptote at the x value with **No cross over point**
- Algebra with [[Limit Properties]] returns `undefined`
- They approach infinity
- The value that approach is oscillating between two values (https://www.youtube.com/watch?v=isMZo-OFJOs)
	- $\lim_{ x \to \infty }\sin x$
	- $\lim_{ x \to -\infty }\sin x$
	- $\lim_{ x \to \infty }\cos x$
	- $\lim_{ x \to -\infty }\cos x$
	- $\lim_{ x \to -\infty }\tan x$
	- $\lim_{ x \to -\infty }\tan x$
	- $\lim_{ x \to \infty } \frac{1}{\sin x}$
	- $\lim_{ x \to -\infty } \frac{1}{\sin x}$
	- $\lim_{ x \to \infty } \frac{1}{\cos x}$
	- $\lim_{ x \to -\infty } \frac{1}{\cos x}$
	- $\lim_{ x \to \infty } \frac{1}{\tan x}$
	- $\lim_{ x \to -\infty } \frac{1}{\tan x}$
### Algebraic Proof
- Use Algebra with [[Limit Properties]]
- You can use direct substitution if there is no hole in the equation
##### Limit Finding Techniques
- [[Limit Rationalization]]
- [[Limit Substitution]]
- [[Limit Division]]
- [[Limits with Euler's Number]]
- [[Squeeze Theorem]]
- [[L'Hopital's Rule]]
### Graphic Proof
- The limit is that point it naturally approaches. Follow the curve, not the jump
![[Limits-20240207200022123.webp|254]]
# [[Limit Properties]]
You require the properties of limits to be able to get the limits of any function
https://en.wikibooks.org/wiki/Calculus/Proofs_of_Some_Basic_Limit_Rules
To use limit rules, you need to prove that each limit used in the limit rule exists. (Unless its for constants and pre-made functions like sin(), cos(), tan(),etc)
##### Identity Rule
$$\lim_{x \to a} x = a$$
##### Constant Rule
if $a$ and $k$ for any constants then
$$\lim_{x \to a} k = k$$

##### Sums & Difference Rule
The limit of the sum, is the sum of the limits.
$$\lim_{x \to a}[f(x) \pm g(x)] = \lim_{x \to a}[f(x)] \pm \lim_{x \to a}[g(x)]$$
##### Scalar Product Rule
$$\lim_{x \to a} [cf(x)] = c[\lim_{ x \to a}f(x)]$$
##### Product Rule
$$\lim_{x \to a}[f(x)g(x)] = \lim_{x \to a}[f(x)] * \lim_{x \to a}[g(x)]$$
##### Quotient Rule
$$\lim_{x \to a}\left[\frac{f(x)}{g(x)}\right] = \frac{\lim_{x \to a}[f(x)]}{\lim_{x \to a}[g(x)]}$$
##### Power Rule
Limit of the power is the power of the limit
$$\lim_{x \to a}[f(x)^{n}]= \lim_{x \to a}[f(x)]^n$$
##### Composition Rule
If $f$ is continuous then
$$\lim_{ x \to a }f(g(x))  = f(\lim_{ x \to a }g(x) ) $$
# Continuities
[[Discontinuities]]
### Continuous
For the function to be continuous at a point, 2 conditions:
1. Limit must exist
2. $$\lim_{ x \to a }f(x) = f(a)$$
### Discontinuous
For the function to be discontinuous at a point, 2 conditions:
$$\\lim_{ x \to a }f(x) \neq f(a)$$
OR 
$$\lim_{ x \to a }f(x) \ \ \ \ DNE $$
OR 
$L = \pm\infty \ \ OR \ \ f(x) = \pm\infty$
# Additional Concepts
- [[Limits Does Not Exist]]
- [[Order Limit Law]]