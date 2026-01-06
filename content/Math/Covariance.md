---
tags:
  - math
  - statistics
  - probability
---
# Definition
- For [[Random Variable|RV]] $X$ with [[Expectation|Mean]] $\mu_{x} = E(X)$ and [[Variance]] $\sigma^{2}_{X}= V(X)$
- For [[Random Variable|RV]] $Y$ with [[Expectation|Mean]] $\mu_{Y} = E(Y)$ and [[Variance]] $\sigma_{Y}^{2} = V(Y)$
- The covariance of $X$ and $Y$ defined as $Cov(X,Y) = E[(X-\mu_{X})(Y-\mu_{Y})] = E(XY)-E(X)E(Y)$
# Properties
- $Cov(aX,bY) = abCov(X,Y)$
- $Cov(X,X) = V(X)$
- $Cov(X,Y) = E(XY)- \mu_{X}\mu_{Y}$
- If $X \perp Y \implies Cov(X,Y) = 0$
- Variance of linear combinations: $V(X+Y) = V(X)+V(Y)+2Cov(X,Y)$
- [[Linearity]] of covariances $Cov(\Sigma_{i=1}^{n}a_{i}X_{i}, \Sigma_{j=1}^{m}b_{j}Y_{j}) = \Sigma_{i=1}^{n}\Sigma_{j=1}^{m}a_{i}b_{j}Cov(X_{i},Y_{j})$
- $Cov(aX-bY, cW-dZ) = acCov(X,W)-adCov(X,z)-bzCov(Y,W)+bdCov(Y,z)$
