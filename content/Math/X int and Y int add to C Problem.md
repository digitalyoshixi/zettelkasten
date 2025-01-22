---
tags:
  - math
  - calculus
---
# Question
Let $c > 0$ and let $L$ be tangent to the curve $\sqrt{ x } + \sqrt{ y } = \sqrt{ c }$.
Show that the sum of the x-int of $L$ and the y-int of $L$ is equal to $c$
# Solution
First get the tangent line of L.
Get the derivative first.
- $0.5(x^{-0.5}) + 0.5(y^{-0.5}) \frac{dy}{dx} = 0$
- $\frac{dy}{dx} = \frac{-0.5(x^{-0.5})}{0.5(y^{-0.5})}$
- $\frac{dy}{dx} = \frac{-(\frac{1}{\sqrt{ x }})}{\frac{1}{\sqrt{ y }}}$
- $\frac{dy}{dx} = -\frac{\sqrt{ y }}{\sqrt{ x }}$

Then substitute x and y as $a,b$ so $\sqrt{ a } + \sqrt{ b } = \sqrt{ c }$

Tangent line $y - b = -\frac{\sqrt{ b }}{\sqrt{ a }}(x-a)$
So now. to get the x-int, take $y=0$
 - $0 - b = -\frac{\sqrt{ b }}{\sqrt{ a }}(x-a)$
 - $x=a+\sqrt{ ab }$
For the y-int, take $x=0$
- $y - b = -\frac{\sqrt{ b }}{\sqrt{ a }}(0-a)$
- $y=b+\sqrt{ ab }$
Then $x+y=a+\sqrt{ ab } + b + \sqrt{ ab }$
- $= a + b + 2\sqrt{ ab }$
- $= (\sqrt{ a } + \sqrt{ b })^2$
- $= (\sqrt{ c })^2$
- $= c$
$$\square$$
