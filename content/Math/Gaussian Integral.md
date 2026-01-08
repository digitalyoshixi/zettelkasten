---
tags:
  - math
  - calculus
---
$$
\int_{-\infty}^{\infty} e^{-x^{2}}dx = \sqrt{ \pi }
$$
# Proof
$$
\int_{-\infty}^{\infty} e^{-x^{2}} dx\int_{-\infty}^{\infty} e^{-y^{2}} dx = \int_{-\infty}^{\infty} e^{-x^{2}-y^{2}} dx
$$
We convert to polar coordinates. So,
$(x,y) = (r\cos \theta, r\sin \theta)$
Note that the jacobian
$$
|\frac{\partial(x,y)}{\partial(r, \theta)}| = r
$$
$$
\implies \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-x^{2}-y^{2}}dxdy
= 
\int_{0}^{2\pi} \int_{0}^{\infty} e^{-1[(r \sin \theta)^{2} + (r \cos \theta)^{2}]}dxdy
$$
$$
= 
\int_{0}^{2\pi} \int_{0}^{\infty} e^{-r^{2} }dxdy
= \pi
$$

