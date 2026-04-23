---
tags:
  - security
  - programming
---
A [[Hashing|Hash Function]] $h$ has independent uniform hashing property:
- Uniform: any key is equally likely to hash into any of $m$ [[Bucket]]
	- Sample space of keys $U$
	- $\forall 1 \leq i \leq m, \forall k \in U, Pr(h(k)=i)=\frac{1}{m}$
- Independent: any key is hashed independently of where other keys have hashed to. Formally:
	- $k_{1},k_{2} \in U$ with $k_{1} \neq k_{2}$ $Pr(h(k_{1})=h(k_{2})=i)=Pr(h(k_{1})=i) \times Pr(h(k_{2})=i)$ ([[Independent Events|Independent Event]])