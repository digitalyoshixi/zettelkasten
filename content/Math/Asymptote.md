---
tags:
  - math
aliases:
  - VA
  - HA
---
Asymptotes occur when denominator = 0, and it doesn't cancel.
x/ x+2. asymptote at x = -2

Cancelling however, does not have asymptotes, but they have [[Hole]]
BUT, x/x. = 1, it has a hole at (0,1)

## Vertical Asymptote
Let the denominator equal zero.
This would be when:
- $\lim_{ x \to a } = \infty$
- $\lim_{ x \to a } = -\infty$
- $\lim_{ x \to a^- } = \infty$
- $\lim_{ x \to a^- } = -\infty$
- $\lim_{ x \to a^+ } = \infty$
- $\lim_{ x \to a^+ } = -\infty$
## Horizontal Asymptote
Horizontal asymptotes occur at the extremes.
This would be:
- $\lim_{ x \to \infty } = L$
- $\lim_{ x \to -\infty } = M$
### 3 Trials
You can run 3 tests to find the horizontal asymptote.
with a rational function in standard form:
$\frac{ax^m+\dots}{bx^n+\dots}$
if m < n, **y = 0**
if m > n, **NO HA**. You have a oblique or parabolic depending on the difference in degree
if m = n, y = a/b
### Chart Method
Make a [[Behavior Table Method]] chart
Example with 1/2x-3

| x     | y    |
| ----- | ---- |
| 3/2^+ | inf  |
| 3/2^- | -inf |
| +inf  | 0^+  |
| -inf  | 0^-  |
Vertical asymptote: x = 3/2
Horizontal asymptote: y = 0
X intercept: none
Y intercept: -1/3
domain: x ∈ ℝ, x != 3/2
range: y ∈ ℝ, y ! = 0
##### Shit acronym
BOBO BOTN EATS D/C
Bigger On the Bottom: 0
EATS D/C means "Exponents are the same divide coefficients"
# Slant Asymptote
Let $m,b \in R$.
The line $y=mx+b$ is a slant asymptote to the graph if either:
- $\lim_{ x \to \infty }[f(x)-(mx+b)]=0$
- $\lim_{ x \to -\infty }[f(x)-(mx+b)]=0$
### Finding Slant Asymptote
Example: Find the slant asymptote of $\pi x+7+e^{\frac{1}{x^2}}$
Note that $\lim_{ x \to \pm \infty }e^{\frac{1}{x^2}}=1$
Then consider $\pi x+7+1 = \pi x+8$
Consider $\lim_{ x \to \pm \infty }[f(x)-(\pi x+8)]$
$\lim_{ x \to \pm \infty }[\pi x+7+e^{\frac{1}{x^2}}-(\pi x+8)]$
$= \lim_{ x \to \pm \infty }[-1+e^{\frac{1}{x^2}}]$
$= \lim_{ x \to \pm \infty }[-1] + \lim_{ x \to \pm \infty }[e^{\frac{1}{x^2}}]$
$= -1 + 1$
$= 0$