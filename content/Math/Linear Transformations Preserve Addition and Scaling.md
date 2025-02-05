---
tags:
  - linalg
  - math
---
### Proving $\implies$
Suppose $T:V\to W$ is linear
$T((a \boxdot \overrightarrow{u}) \boxplus (b \boxdot \overrightarrow{v}))$
$= T(a \boxdot \overrightarrow{u}) \oplus T(b \boxdot \overrightarrow{v})$ As $T$ preserves adding
$= (a \odot T(u)) \oplus (b \odot T(\overrightarrow{v}))$ as $T$ preseves scaling
### Proving $\Leftarrow$
Suppose $T$ satisfies
$T((a \boxdot \overrightarrow{u})) \boxplus (b \boxdot \overrightarrow{v})$
$=(a \odot T(\overrightarrow{u})) \oplus (b \odot T(\overrightarrow{v}))$
For all $a,b \in F$ and $\overrightarrow{u}, \overrightarrow{v} \in V$
We check $T$ preserves addition
Suppose $a=b=1 \in F$, this gives:
$T((1 \boxdot \overrightarrow{u})) \boxplus(1 \boxdot \overrightarrow{v})$
$=(1 \boxdot T(\overrightarrow{u})) \boxplus (1 \odot T(\overrightarrow{v}))$
$\Longleftrightarrow T(\overrightarrow{u} \boxplus \overrightarrow{v}) = T(\overrightarrow{u}) + T(\overrightarrow{v})$ 
Thus, we have shown both sides