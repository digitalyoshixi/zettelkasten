---
tags:
  - math
  - linalg
---
# Process (Direct Proof)
1. Assume two objects have the same property
2. Show that the two are equal
### Alternate Process (Contradiction)
1. Assume there exists a $y \neq x$ and that $y$ has the same property
2. Derive a contradiction
# Example
Assume $\overrightarrow{0}$ and $\overrightarrow{0'}$ are both zero vectors.
This means $\overrightarrow{0} \boxplus \overrightarrow{x} = \overrightarrow{x}$ for all $\overrightarrow{x}$
$\overrightarrow{0'} + \overrightarrow{x} = \overrightarrow{x}$ for all x
- Then, $\overrightarrow{0} = \overrightarrow{0'} \boxplus \overrightarrow{0}$
- Then, $\overrightarrow{0} = \overrightarrow{0} \boxplus \overrightarrow{0'}$ by [[Vector Space]] axiom 2 (commutative)
- $\overrightarrow{0} = \overrightarrow{0'}$ by hypothesis on $\overrightarrow{0}$
$$\square$$
