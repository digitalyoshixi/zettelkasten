---
tags:
  - calculus
aliases: []
---
A process to integrate when you have one of the following expressions in the integrand: 
- $\sqrt{ a^{2}-x^{2} }$
- $\sqrt{ a^{2} +x^{2}}$
- $\sqrt{ x^{2}-a^{2} }$
Where: $a \in \mathbb{R}$. You will be able to [[Constructing Trigonometric Substitution Triangles|Construct a Trig Substitution Triangle]] to relate each side to the equation.

You are able to use the [[Pythagorean Identities]] to get the following implications:
- $\sqrt{ a^{2}-x^{2} }$. Choosing $x=a \sin \theta$ where $\theta \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ give us $\sqrt{ a^{2}-x^{2} }= a\cos \theta$
- $\sqrt{ a^2 +x^{2}}$. Choosing $x = a\tan \theta$ where $\theta \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ gives us $\sqrt{ a^2 +x^{2}}=a \sec \theta$
- $\sqrt{ x^2 -a^{2}}$. Choosing $x = a\sec \theta$ where $\theta \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ gives us $\sqrt{ x^2 -a^{2}}=a \tan \theta$
Note at the end of the integration, you will get x in terms of $\theta$, so use [[Triangle Method]] to find the final value of $x$
# Process
1. Use a triangle to make a substitution for x
2. Solve with [[Integration by Trigonometric Identities]]
3. Use the triangle to reverse the substitution
# Examples
### Example 1
![[Integration by Trigonometric Identities-20250213231151670.webp]]
![[Integration by Trigonometric Identities-20250213231209097.webp]]

