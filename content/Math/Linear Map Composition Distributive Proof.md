---
tags:
  - math
  - linalg
---
# Proof
1. Suppose we have $U \xrightarrow{R} V \xrightarrow{T,S} W$ linear
2. Check left side:
	1. $(T+S)R$
	2. $= TR+SR$
	3. Picking $u  \in U$, calculate:
	4. $[(T+S)R](u) = (T+S)R(u)$ by applying $R$
	5. $= S(R(u))$ by defn of $T+S$
3. Check right side:
	1. $[TR + SR](u)$
	2. $= TR(u) + SR(u)$ by defn of $TR + SR$
	3. $= T(R(u)) + S(R(u))$ by applying $TR$ and $SR$
4. Note that L.S = R.S, thus compositions are distributive