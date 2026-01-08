---
tags:
  - math
  - programming
---
The ability to bound the runtime of a proram under a existing function.
# Example
With a runtime of: $an^2+bn+c \to 12n^{2}+10n+10$
Then,
$$
12n^{2}+10n+10 \leq 12n^{2}+10n^{2}+10
\implies 12n^{2}+10n+10<12n^{2}+10n^{2}+10 = 22n^{2}+10
$$
For all $n \geq 10$
$22n^{2}+10 \leq 22n^{2}+n \leq 22n^{2}+n^{2}+23n^{2}$
Then, for all $n>10$, the function is bounded below $23n^{2}$