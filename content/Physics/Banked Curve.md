---
tags:
  - physics
---
# Table Of Contents
```table-of-contents
```
# Banked Curve
A banked curve looks something like such:
![[Banked Curve-20240309233550127.webp|502]]
It is incline at 3 axis, which makes this only truly 
visualized with 3D.
### Visualization
How we tend to visualize this is by making 2 views.
![[Banked Curve-20240310153054328.webp]]
# Assumptions
- No rotated set of axis in FBDs
# Banked Curve Without Friction([[UCM]])
![[Banked Curve-20240310162807516.webp]]
![[Banked Curve-20240310163412348.webp]]
# Key Concepts
- Normal force is what allows the car to turn
- $F_{Norm}$ > $F_{g}$
- If you are undergoing [[Uniform Circular Motion|UCM]], you don't need friction to turn
# Banked Curve With Friction
The friction acting on the banked curve is static friction $F_{s}$ and uses $\mu_{s}$
![[Banked Curve-20240310160444684.webp|694]]
Friction will only act to assist in turning if the car moves quicker or faster than $v_{ideal}$ which is the speed required for UCM ($v=\sqrt{ rg\tan \theta }$)
![[Banked Curve-20240310161824608.webp]]
### Analysis
[[Banked Curve Bigger Velocity Proofs]]
[[Banked Curve Smaller Velocity Proofs]]
# Formulas
### Angle Of Banking
##### $v > v_{ideal}$
$\frac{v^2}{rg}=\frac{\mu \cos \theta+\sin \theta}{\cos \theta-\mu \sin \theta}$
##### $v<v_{ideal}$
$\frac{v^2}{rg} = \frac{\sin \theta - \mu \cos \theta}{\cos \theta+\mu \sin \theta}$
##### UCM
where $\mu=0$, 
$\frac{v^2}{rg}= \tan \theta$
### Acceleration
$$a_{c}=g\tan \theta$$
### Velocity 
$v = \sqrt{ rg\tan \theta }$
### Radius
$r = \frac{v^2}{g\tan \theta}$
