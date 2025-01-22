---
tags:
  - math
---
# Table of Contents
```table-of-contents
```
# Graphing Trig Functions
### [[Graphing Sine Graphs|Sine]]
| x                | y   |
| ---------------- | --- |
| 0                | 0   |
| $\frac{\pi}{2}$  | 1   |
| $\pi$            | 0   |
| $\frac{3\pi}{2}$ | -1  |
| $2\pi$           | 0    |
![[Graphing Sine Graphs-20231210194237148.webp|265]]
### [[Graphing Cosine Graphs|Cosine]]
| x                | y   |
| ---------------- | --- |
| 0                | 1   |
| $\frac{\pi}{2}$  | 0   |
| $\pi$            | -1   |
| $\frac{3\pi}{2}$ | 0  |
| $2\pi$           | 1    |
![[Graphing Cosine Graphs-20231210194335167.webp|268]]
### [[Graphing Tangent Graphs|Tangent]]
| x                | y   |
| ---------------- | --- |
| $-\frac{\pi}{2}$  | undef   |
| $0$            | 0   |
| $\frac{\pi}{2}$ | undef  |
![[Graphing Tangent Graphs-20231210195021112.webp|177]]
# [[Trigonometric Function Transformation Guide]]
**Amplitude:** Half the total range of the y axis the function holds
![[Trigonometric Function Equations-20231112033209925.webp|142]]
**Vertical Shift**: The shift from y=0 to the middle of the function
![[Trigonometric Function Equations-20231111221557991.webp|144]]
**Phase Shift**: The shift from x = 0 to the 'first point' of the function
![[Trigonometric Function Equations-20231111221939513.webp|338]]
**Period:** The total range of a cycle of the function
![[Trigonometric Function Equations-20231111222037381.webp|279]]
### Formula 
y = $a\sin(k(cos-d))+c$
*this applies to all trig functions. not just sin functions*
**a:** amplitude
**k:** k is $\frac{2\pi}{period}$
**d** is the phase shift. if d is positive, go left. if d is negative, go right
**c** is the vertical shift. if c is positive, go up. if c is negative, go down.

### Mapping rule
##### Y Transform
depends on `a` and `c`
stretch with a factor of `a`
vertical shift at `c`
(*x*, ay + c)
##### X Transform
period stretch of `1/k`
phase shift of `-d`
(x/k-d,*y*)

### [[Cos to SIn & Sin to Cos]]
$\cos x = \sin(x+\frac{period}{4})$
$\sin(x) = \cos(x-\frac{period}{4})$

# [[Inverse Trigonometric Functions]]
### Arcsin
![[Trigonometric Function Inverses-20231114023413732.webp|548]]
### Arccos
![[Trigonometric Function Inverses-20231114023640559.webp|358]]
### Arctan
![[Trigonometric Function Inverses-20231114023745110.webp|574]]

# Reciprocal Trigonometric Functions
### Graph From Table Of Values
First, write the table for the original function, then find the reciprocals of all the values.
##### Sine -> Cosecant function
| x or y | 0     | $\frac{\pi}{6}$ | $\frac{\pi}{3}$        | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$       | $\frac{5\pi}{6}$ | $\pi$ | $\frac{7\pi}{6}$ | $\frac{4\pi}{3}$        | $\frac{3\pi}{2}$ | $\frac{5\pi}{3}$        | $\frac{11\pi}{6}$ | $2\pi$ |
| ------ | ----- | --------------- | ---------------------- | --------------- | ---------------------- | ---------------- | ----- | ---------------- | ----------------------- | ---------------- | ----------------------- | ----------------- | ------ |
| y=sinx | 0     | 1/2             | $\frac{\sqrt{ 3 }}{2}$ | 1               | $\frac{\sqrt{ 3 }}{2}$ | 1/2              | 0     | -1/2             | $\frac{-\sqrt{ 3 }}{2}$ | -1               | $\frac{-\sqrt{ 3 }}{2}$ | -1/2              | 0      |
| y=cscx | undef | 2               | $\frac{2}{\sqrt{ 3 }}$ | 1               | $\frac{2}{\sqrt{ 3 }}$ | 2                | undef | -2               | $\frac{-2}{\sqrt{ 3 }}$ | -1               | $\frac{-2}{\sqrt{ 3 }}$ | -2                | undef  |

notice how the table is intervals with unit circle, but there is no xpi/4 ratios
##### Cosine -> Secant function
| x or y | 0   | $\frac{\pi}{6}$        | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{5\pi}{6}$        | $\pi$ | $\frac{7\pi}{6}$        | $\frac{4\pi}{3}$ | $\frac{3\pi}{2}$ | $\frac{5\pi}{3}$ | $\frac{11\pi}{6}$      | $2\pi$ |     |     |
| ------ | --- | ---------------------- | --------------- | --------------- | ---------------- | ----------------------- | ----- | ----------------------- | ---------------- | ---------------- | ---------------- | ---------------------- | ------ | --- | --- |
| y=cosx | 1   | $\frac{\sqrt{ 3 }}{2}$ | 1/2             | 0               | -1/2             | $\frac{-\sqrt{ 3 }}{2}$ | -1    | $\frac{-\sqrt{ 3 }}{2}$ | -1/2             | 0                | 1/2              | $\frac{\sqrt{ 3 }}{2}$ | 1      |     |     |
| y=secx | 1   | $\frac{2}{\sqrt{ 3 }}$ | 2               | undef           | -2               | $\frac{-2}{\sqrt{ 3 }}$ | -1    | $\frac{-2}{\sqrt{ 3 }}$ | -2               | undef            | 2                | $\frac{2}{\sqrt{ 3 }}$ | 1      |     |     |

##### Tangent -> Cotangent function
| x or y   | 0     | $\frac{\pi}{4}$ | $\frac{\pi}{2}$ | $\frac{3\pi}{2}$ | $\pi$ | $\frac{5\pi}{4}$ | $\frac{3\pi}{2}$ | $\frac{7\pi}{4}$ | $2\pi$ |     |     |     |     |     |
| -------- | ----- | --------------- | --------------- | ---------------- | ----- | ---------------- | ---------------- | ---------------- | ------ | --- | --- | --- | --- | --- |
| y = tanx | 0     | 1               | undef           | -1               | 0     | 1                | undef            | -1               | 0      |     |     |     |     |     |
| y = cotx | undef | 1               | 0               | -1               | undef | 1                | 0                | -1               | undef  |     |     |     |     |     |
# Memorizing Reciprocal Trig Functions
### Cosecant
![[Memorizing Reciprocal Trig Functions-20231114230138547.webp|297]]
They opposites.
Local minimas are 1. Local maximas are -1
### Secant
Sad face.
![[Memorizing Reciprocal Trig Functions-20231114230010550.webp|204]]
Local minmas are 1. Local maximas are -1
### Cotangent
![[Memorizing Reciprocal Trig Functions-20231114230454364.webp|327]]
Like a flipped tangent graph that starts at 0 and ends at 2pi.
