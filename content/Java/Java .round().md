---
tags:
  - math
aliases:
  - Rounding
---
using the .round() method will return simple a integer representation of your rounded number. And this is important. It will round to integer WHOLE NUMBER. Unlike python, you are unable to set the decimal places to round to.
so, if you want the decimal places, you will have to do a hacky solution.
![[Pasted image 20230907182734.png]]
Multiply the float first by the 10^decimal places you want. then you divide by the same 10^decimal places after rounding.
