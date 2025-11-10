---
tags:
  - math
  - calculus
---
A method for evaluating limits in two dimensions.
For $\lim_{ (x,y)  \to (0,0)}f(x,y)$
Substitute $x = r \cos \theta$, $y = r \sin \theta$ 
Then, you get $\lim_{ r \to 0 }f(r\cos \theta, r\sin \theta)$
# Example
$\lim_{ (x,y) \to (0,0) } \frac{3x^{2}y}{x^{2} + y^{2}} = \lim_{ r \to 0 } \frac{3 r^{2}\cos^{2}\theta r \sin \theta}{r^{2}\cos^{2} \theta + r^{2} \sin^{2} \theta} =  \lim_{ r \to 0 }\frac{3r^{3}\cos \theta \sin \theta}{r^{2}} = 0$