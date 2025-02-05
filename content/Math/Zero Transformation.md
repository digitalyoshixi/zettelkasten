---
tags:
  - math
  - linalg
---
Guaranteed for all vector spaces $V,W$
# Zero Transformation
$Z : V\to W$ given by $Z(v) = 0w$
# Proof
### Check that $Z$ is linear
So, we check that $Z$ satisfies
$Z((a \boxdot u)\boxplus(b \boxdot v)) = (a \boxdot Z(u)) \oplus (b \odot Z(\overrightarrow{v}))$
By definition of $Z$, we have:
$Z((a \boxdot u) \boxplus (b \boxdot v)) = \hat{0}w$

For the right side, we have:
$(a \boxdot Z(\overrightarrow{u})) \oplus (b \odot Z(v))$
$=(a \odot 0w) \oplus (b \odot 0w)$ by defn of $Z$
$=(0w) \oplus (0w)$ for all $c \in F$, $C \odot 0w = 0w$
$=0w$ by defn of $0w$
We get that both sides are equal, thus we an conclude that is is linear