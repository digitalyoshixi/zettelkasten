---
tags:
  - math
---
Really large quotient. Expressions that have x in the base and x in the exponent
# Example
Find general derivative:
$$y = x^x$$
We rearrange
$$\ln y=\ln x^x$$
$$\ln y=x\ln x$$
Derivative of both sides
$$\frac{1}{y}\frac{dy}{dx}=\ln x+x \frac{1}{x}$$
Multiply both sides b $y$
$$\frac{dy}{dx}=y(\ln x+1)$$
$$\frac{dy}{dx}=x^x(\ln x+1)$$
# Use Cases of Logarithmic Differentiation
### Quotient Rule Replacement
$$h(x)=\frac{(5x-3)^2}{(3x+2)^4(2x+1)^3}$$
$\ln$ both sides and use logarithm rules
$$\ln h(x) = \ln(5x-3)^{2}- \ln(3x+2)^4-\ln(2x+1)^3$$
More log rules
$$\ln h(x) = 2\ln(5x-3)-4\ln(3x+2)-3\ln(2x+1)$$
Now derive
$$\frac{1}{h(x)}h'(x) = 2(\frac{1}{5x-3}*5)- 4(\frac{1}{3x+2}*3)-3(\frac{1}{2x+1}*2)$$
$$h'(x) = \frac{(5x-3)^2}{(3x+2)^4(2x+1)^{3}}*(\frac{10}{5x-3}-\frac{12}{3x+2}-\frac{6}{2x+1})$$
This works for all quotients 
