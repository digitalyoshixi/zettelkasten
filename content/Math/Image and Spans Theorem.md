---
tags:
  - math
  - linalg
---
# Theorem
- if $\{ v_{1},\dots,v_{n} \}$ is a [[Spanning Set]] for $V$ 
- If $T:V\to W$ is [[Linear Transform|Linear Transformation]]
- then, $\{ T(v_{1}),\dots,T(v_{2}) \}$ is a spanning set for $Image(T)$
# Proof
### Proving $span \{ T(v_{1}),\dots,T(v_{n}) \} \subset Image(T)$
1. Pick $w \in span\{ T(v_{1}) ,\dots,T(v_{n})\}$
2. Then, $w = a_{1}T(v_{1}) + \dots + a_{n}T(v_{n})$
3. $= T(a_{1}v_{1} +\dots+a_{n}v_{n})$ by [[Linearity]]
4. $\in Image(T)$
### Proving $Image(T) \subset span\{ T(v_{1}),\dots,T(v_{n}) \}$
1. Pick $\overrightarrow{w} \in Image(T)$
2. We can express $\overrightarrow{w}=T(\overrightarrow{v})$
3. $= T(a_{1}v_{1}+\dots a_{n}v_{n})$ as $\{ v_{1},\dots,v_{n} \}$ is a spanning set
4. $=a_{1}T(v_{1}) + \dots + a_{n}T(v_{n})$ by [[Linearity]]
5. $\in span\{ T(v_{1}),\dots,T(v_{n}) \}$ by defn of span
