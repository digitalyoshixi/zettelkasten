---
tags:
  - math
aliases:
  - First Principles
---
# Difference Quotient
Slope of tangent at a given point **x** can be modeled with:
$$m=\lim_{ h \to 0 } \frac{f(x+h) - f(x)}{h}$$
# Proof
This is essentially a rise/run where we try to reduce the run distance to 0 and get tangent. Get the value as h(the run distance) approaches 0.
# Example
$f(x) = \sqrt{ x }$
what is slope at x = 9?
### Solution
$\lim_{ h \to 0 }\frac{f(x+h)-f(x)}{h}$
$\lim_{ h \to 0 }\frac{\sqrt{ 9+h }-\sqrt{ 9 }}{h}$
$\lim_{ h \to 0 }\frac{\sqrt{ 9+h }-3}{h}*\frac{\sqrt{ 9+h }+3}{\sqrt{ 9+h }+3}$
$\lim_{ h \to 0 }\frac{ 9+h - 9 }{h(\sqrt{ 9+h }+3)}$
$\lim_{ h \to 0 }\frac{h }{h(\sqrt{ 9+h }+3)}$
$\lim_{ h \to 0 }\frac{1}{\sqrt{ 9+h }+3}$
$\frac{1}{\sqrt{ 9 }+3}$
$\frac{1}{6}$
