---
tags:
  - math
  - linalg
---
# Theorem
1. With set $\beta = \{ \beta_{1}, \dots, \beta_{n} \}$
2. Then set $S = \{ \frac{\beta_{1}}{|| \beta _{1} || } , \dots, \frac{\beta_{n}}{|| \beta_{n}||} \}$ is [[Orthonormal Set]]
# Proof
Using [[Proof by Strong Induction|Strong Induction]]
1. Firstly note that $|| \alpha_{i} || \neq 0$
2. We can define $\beta$ as follows
### Proving All Units are [[Unit Vector]]
1. First, we prove every vector is a [[Unit Vector]]
2. $\left\langle  \frac{\alpha_{i} }{|| \alpha_{i} ||} | \frac{\alpha_{i} }{|| \alpha_{i} ||} \right\rangle = \frac{1}{||\alpha_{i}|| \cdot || \alpha_{i}||} \cdot \langle \alpha_{i} | \alpha_{i} \rangle = \frac{|| \alpha_{i} || ^{2}}{ || \alpha_{i}||^{2}} = 1$
### Proving $\beta$ is an [[Orthogonal Set]]
1. We show that $\langle \frac{\alpha_{i}}{||\alpha_{i}||} | \frac{\alpha_{j}}{|| \alpha_{j}||} \rangle = 0 \Longleftrightarrow i \neq j$
2. Note that $\langle \frac{\alpha_{i}}{||\alpha_{i}||} | \frac{\alpha_{j}}{|| \alpha_{j}||} \rangle = \frac{1}{|| \alpha_{i} || * ||\alpha_{j}||}\langle \alpha_{i} | \alpha_{j}\rangle = 0\Longleftrightarrow \langle\alpha_{i} | \alpha_{j}\rangle = 0$
3. Now we show $\langle\alpha_{i} | \alpha_{j} \rangle = 0 \Longleftrightarrow i \neq j$
4. Proof with strong induction:
##### Base Case
1. Base case $n = 2$
2. Then, $\langle\alpha_{2} | \alpha_{1}\rangle = \left\langle \beta_{2} - \frac{\langle \beta_{2} - \alpha_{1} \rangle}{\langle \alpha_{1} | \alpha_{1} \rangle} * \alpha_{1}| \alpha_{1} \right\rangle$
3. $= \langle \beta_{2} | \alpha_{1} \rangle - \frac{\langle\beta_{2} | \alpha_{1} \rangle}{\langle\alpha_{1} | \alpha_{1} \rangle} \cdot \langle\alpha_{1} | \alpha_{1}\rangle$
4. $= 0$
### $n+1$ case
1. Assume the set $\{ \alpha_{1},\dots,\alpha_{n} \}$ is [[Orthogonal Set]]
2. Then, this means $\langle \alpha_{i} | \alpha_{j} \rangle = 0, \forall i \neq j \in \{ 1,\dots,n \}$
3. Consider $\langle \alpha_{n+1} | \alpha_{k} \rangle$ where $k \in \{ 1,\dots,n \}$
4. $\langle \alpha_{n+1} | \alpha_{k} \rangle = \langle \beta_{n+1} - \sum_{i=1}^{n} \frac{ \langle \beta_{n+1} | \alpha_{i} \rangle}{ \langle\alpha_{i} | \alpha_{i} \rangle} \cdot \alpha_{i} | \alpha_{k} \rangle$
5. $= \langle \beta_{n+1} | \alpha_{k} - \rangle - \sum_{i=1}^{n} \frac{ \langle\beta_{n+1} | \alpha_{i} \rangle}{ \langle \alpha_{i} | \alpha_{k} \rangle} \langle\alpha_{i} | \alpha_{k}\rangle - \frac{ \langle \beta_{n+1} | \alpha_{k}}{ \langle \alpha_{k} | \alpha_{k} \rangle} \langle \alpha_{k} | \alpha_{k} \rangle - \sum_{i=1}^{n} \frac{\langle\beta _{n+1} | \alpha_{i} \rangle}{ \langle \alpha_{i} | \alpha_{i} \rangle} \langle\alpha_{i} | \alpha_{k} \rangle$