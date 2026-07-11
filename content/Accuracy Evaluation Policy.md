---
tags:
  - verification
aliases:
  - AEP
---
A function when given a [[IO Traces]] and a [[Moore Machine]] returns a real number $[0,1]$ for the accuracy of the machine.
- $(p_{I},p_{O} = (x_{1}x_{2}\dots x_{n}, y_{1}y_{2}\dots y_{n})$ and $z_{1}z_{2}\dots z_{n} = \lambda^{*}(q_{0},p_{I})$
- Strong $\lambda^{*}(q_{0},p_{I}) = p_{O} \in \{ 0, 1 \}$
	- Returns next output of the machine $M$ that matches the output in the test set
- Medium if $\frac{1}{1+n} \cdot |\{ i | y_{1}y_{2}\dots y_{n} = z_{1}z_{2}\dots z_{n} \}|$
	- Returns proportion of largest output prefix that matches
- Weak if $\frac{1}{1+n} \cdot |\{  i|y_{i} = z_{i}\}|$
	- Returns number of output symbols that match
- Accuracy defined as averaged accuracy of $M$ over all traces in $R_{test}$:
$$
\frac{\Sigma_{(p_{I},p_{O}) \in R_{test}}f((p_{I},p_{O}),M)}{|R_{test}|}
$$
When $R_{test}$ is the [[Characteristic Sample Requirement|CSR]], the moore should always be trained perfectly