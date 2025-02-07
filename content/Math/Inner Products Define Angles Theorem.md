---
tags:
  - math
  - linalg
---
If $u, v$ are non-zero [[Vectors]] in $\mathbb{R}^{n}$
Then, the angle $\theta$ between $u,v$ satisfies:
$$\cos(\theta) = \frac{\langle u,v \rangle}{\mid\mid u\mid\mid \mid\mid v\mid\mid}$$

# Intuition
![[Drawing 2025-02-07 11.20.25.excalidraw]]
By applying the law of cosines:
$$\mid\mid u - v \mid \mid ^{2} = \mid \mid u \mid \mid^{2} + \mid \mid v \mid \mid ^{2} - 2 \mid \mid u \mid \mid  \mid \mid v \mid \mid \cos(\theta)$$
in a plane containing u and v

We have:
$$\mid \mid u- v \mid \mid ^{2} - \langle u - v, u - v \rangle - \langle u - v, u \rangle - \langle u = v , v \rangle$$
$$ = \langle u, v \rangle - \langle v, u \rangle - \langle u, v \rangle + \langle v, v \rangle$$
as they are linear
$$= \mid \mid u \mid \mid ^{2} - 2 \langle u, v \rangle + \mid \mid v \mid \mid ^{2}$$
by defn of || ||
$$= \mid \mid u \mid \mid ^{2} + \mid \mid v \mid \mid ^{2} - 2 \mid \mid u \mid \mid \mid \mid v \mid \mid \cos(\theta)$$ by [[Physics/Law Of Cosines|Law Of Cosines]]

$$\implies -2 \langle u, v \rangle = - 2 \mid \mid v \mid \mid  \mid \mid v \mid \mid \cos(\theta) \implies \cos(\theta) = \frac{\langle u,v \rangle }{\mid \mid u\mid\mid\mid\mid v\mid\mid}$$
This also requires: $\overrightarrow{u}, \overrightarrow{v} \neq 0$