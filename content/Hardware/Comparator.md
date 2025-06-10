---
tags:
  - hardware
aliases:
  - General Comparators
---
Hardware [[Component]] that allow for comparing if a input vector is larger than another.
# Basic Comparators
- [[1-Bit Comparator]]
- [[2-Bit Comparator]]
# General Comparator
### $A==B$
For $n$ bit digits:
$$A==B = A_{1}*B_{1}+ \overline A_{1} * \overline B_{1} +\dots +A_{n}*B_{n}+ \overline A_{n} * \overline B_{n}$$
### $A>B$
$$A > B = A_{n} * \overline B_{n} + (A_{n}*B_{n}+ \overline A_{n} * \overline B_{n}) * A_{n-1} * \overline B_{n-1} + \dots + A_{0} * \overline B_{0} * \pi_{k=1}^{n}(A_{k}*B_{k} + \overline A_{k} * \overline B_{k})$$
### $A<B$
$$A < B = \overline A_{n} * B_{n} + (A_{n}*B_{n}+ \overline A_{n} * \overline B_{n}) * \overline A_{n-1} * B_{n-1} + \dots + \overline A_{0} * B_{0} * \pi_{k=1}^{n}(A_{k}*B_{k} + \overline A_{k} * \overline B_{k})$$

