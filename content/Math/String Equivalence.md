---
tags:
  - programming
  - math
---
Two strings $x, y$ are equal if:
- $|x| = |y|$
- $x_{i} = y_{i}, \forall i$
# FSA Equivalence
Two strings $u,u'$ are equivalence for state machine $P$ iff all continuations $v \in \Sigma^{*}$, concatenated words $u'v$ and $uv$ map to the same output by $P$
- $u \equiv_{P} v' \Longleftrightarrow (\forall v \in \Sigma^{*}, P(uv) = P(u'v))$