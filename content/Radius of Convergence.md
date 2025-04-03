---
tags:
  - math
  - calculus
---
# Definition
- Given $\sum_{n=1}^{\infty}C_{n}(x = a)^{n}$
- The largest $R \in \mathbb{R}^{\geq 0} \cup \{ \infty \}$ s.t increasing power series
- We [[Absolute Convergence]] when $|x - a| < R$
- We Diverge when $|x - a| > R$
This $R$ is called the radius of convergence for the power series
# Example
Find the radius of convergence of
$$\sum_{n=1}^{\infty} \frac{a(x+2)^{n}}{3^{n+1}}$$
### Soln
##### Step 1
Find $I$
- With $a = -2$, $C_{n} = \frac{n}{3^{n+1}}$
Find $R$
- $\lim_{ n \to \infty }| \frac{C_{n+1}(x-a)^{n+1}}{C_{n}(x-a)^{n}}|$
- $= \lim_{ n \to \infty }| \frac{n-1}{3^{n+2}}(x+2)^{n+1}| |\frac{n(x+2)^{n}}{3^{n+1}}|$
- $= \lim_{ n \to \infty } \frac{n+1}{n} * \frac{3^{n+1}}{3^{n+2}} * | \frac{(x+2)^{n+1}}{(x+2)^{n}}|$
- $= \lim_{ n \to \infty }(1 + \frac{1}{n}) ( \frac{1}{3})(x+2)$
- $= \frac{1}{3}|x+2|$
By [[Ratio Test]], our [[Power Series]]:
- Will [[Absolute Convergence|AC]] when $\frac{1}{3}|x+2| < 1$
- $\implies |x+2| < 3$
- Will [[Series Divergence|Diverge]] when $\frac{1}{3}|x+2| > 1$
- $\implies |x+2| > 3$
By definition of $R$, we get $R = 3$
##### Step 2
For step 2, we check the endpoints for $x = a \pm R$ . Plug them into the power series, and get a numerical series
- Check $x = a \pm R = -5, 1$
- For $x = -5$:
	- We get $\sum_{n=1}^{\infty}\frac{(n)(-5+2)^{n}}{3^{n+1}}$
	- $= \sum_{n=1}^{\infty} \frac{(n)(-3)^{n}}{3 * 3^n}$
	- $= \sum_{n=1}^{\infty} \frac{(n)(-1)^{n}(3)^{n}}{3 * 3^n}$
	- $= \sum_{n=1}^{\infty} \frac{(n)(-1)^{n}}{3}$
	- Applying div-test for $\lim_{ n \to \infty } \frac{(-1)^{n}(n)}{3} = \pm \infty \neq 0$
	- Thus, by [[Series Divergence|Div Test]], our power series diverges at $x = -5$
- For $x = 1$
	- We get $\sum_{n=1}^{\infty}\frac{(n)(1+2)^{n}}{3^{n+1}}$
	- $= \sum_{n=1}^{\infty} \frac{(n)(3)^{n}}{3 * 3^n}$
	- $= \sum_{n=1}^{\infty} \frac{(n)}{3}$
	- Applying div-test for $\lim_{ n \to \infty } \frac{n}{3}$, our power series diverges.
Thus, our final interval $I = (-5,1)$
- We have [[Absolute Convergence]] (and by proxy, [[Series Convergence|Convergence]] between those values
- We have [[Series Divergence|Divergence]] outside that interval