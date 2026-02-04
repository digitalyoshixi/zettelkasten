---
tags:
  - machine_learning
  - math
---
# Definition
Value function $V_{v}^{\pi} : \mathcal{H} \to [0,1]$ with:
- A [[Security/Policy]] $\pi$ 
- In [[Environment]] $v$
- A [[Discount Factor]] $y$
- A history $a_{1}o_{1}r_{1}\dots a_{t-1}o_{t-1}r_{t-1} = h_{<t} \in \mathcal{H}$
Is defined as:
$$V_{v}$\pi(h_{<t}) := \mathbb{E}_{v}^{\pi} [ \sum_{k=1}^{\infty}y^{k-t}r_{k} | h_{<t}]
$$
- The optimal value is defined as $V_{v}^{*}(h_{<t}) := sup_{\pi}V_{v}^{\pi}(h_{<t})$