---
tags:
  - math
---
# Problem
Say we have a $\frac{x^2}{e^x}$
How do we know what it approaches, when $x\to \infty$?

# Measuring Infinities
You must find when one function is bigger than another function. 
Equate the 2 functions together, then find critical values.
$x^2 = e^x$
$x^2 - e^x = 0$ This will =be the function for finding if $x^2$ is bigger than $e^x$.
$x=-0.703$
Now check intervals

| Test      | $x<-0.703$ | $x > -0.703$ |
| --------- | ---------- | ------------ |
| $x^2-e^x$ | +          | -            |
So, $x^2 > e^x$ when $x<-0.703$
$x^2 < e^x$ when $x>-0.703$

$\lim_{x \to \infty} f(x)$ will follow $x>-0.703$
so, $e^x$ will be bigger. $e^x$ is the bigger infinity. $\frac{small\infty}{big\infty}$ = 0.
$\lim_{x \to \infty} f(x)=0$

$\lim_{x \to -\infty} f(x)$ will follow $x<-0.703$
so, $x^2$ will be bigger. $\frac{big\infty}{small\infty}$ = $\infty$.
$\lim_{x \to -\infty} f(x)=\infty$
