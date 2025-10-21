---
tags:
  - math
  - statistics
---
A method to find [[Portable Document Format|PDF]] of [[Probability Mass Function|PMF]] of [[Sum of Random Variables]] $Z = X+Y$ directly.
# PDF
The [[Probability Density Function|PDF]] $f_{Z}(z)$ is given by:
$$f_{Z}(z) = \int_{-\infty}^{\infty} f_{X,Y}(x,z-x)dx = \int_{-\infty}^{\infty} f_{X,Y}(z-y,y)dy$$
# PMF
The [[Probability Mass Function|PMF]] $p_{Z}(z)$ is given by:
$$p_{Z}(z) = \sum_{x}p_{X,Y}(x,z-x) = \sum_{y}p_{X,Y}(z-y,y)$$
