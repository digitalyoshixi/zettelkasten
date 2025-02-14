---
tags:
  - math
  - linalg
---
- If $V, W$ are finite dimensional vector spaces
- With $dim(V) = n$
- If $V = span \{  u_{1}, \dots,u_{k}, v_{k+1}, \dots, v_{n}\}$ s.t: 
	- $ker(T) = span\{ u_{1},\dots,u_{k} \}$
- Then: $Image(T) = span\{ T(v_{k+1}),\dots,T(v_{n}) \}$
# Proof
1. Pick a basis for $ker(T) = \{ u_{1},\dots,u_{k} \}$
2. We know that $V$ is finitely dimensional, and that $dim(V) = n$
3. Thus, we can extend to a basis $V = span \{ u_{1},\dots,u_{k},v_{k+1},\dots,v_{n} \}$
4. We want to verify tat $Image(T) = span \{ T(v_{k+1}) ,\dots,T(v_{n})\}$
	1. Proving $span \{ T(v_{k+1}),\dots,T(v_{n}) \} \subset Image(T)$
	2. $span \{ T(v_{k+1}),\dots,T(v_{n}) \} \in Image(T)$ is straight forward
	3. Pick $w \in span \{ T(v_{k+1}) ,\dots,T(v_{n})\}$, then we have:
	4. $w = a_{k+1}T(v_{k+1}) + \dots + a_{n}T(v_{n})$ by definition of $span$
	5. $w=T(a_{k+1}v_{k+1} + \dots + a_{n}v_{n})$ by [[Linearity]]
	6. Thus, $w \in Image(T)$
	7. Proving $Image(T) \subset span \{ v_{k+1}, \dots, v_{n} \}$
	8. Pick $w \in Image(T)$
	9. Then, we have $w = T(v)$ for some $v \in V$
	10. Thus, $w = T(a_{1}u_{1} + \dots +a_{k}u_{k} + v_{k+1}u_{k+1}+\dots+a_{n}v_{n})$
	11. $= a_{1}T(u_{1}) + \dots + a_{k}T(u_{k}) + a_{k+1}T(v_{k+1}) + \dots +a_{n}T(v_{n})$ by [[Linearity]]
	12. As $u_{1},\dots u_{k} \in ker(T) \implies T(u_{1}),\dots,T(u_{k}) = 0$
	13. $= 0 + \dots + 0 + a_{k+1}T(v_{k+1}) + \dots +T(v_{n})$
	14. $\in span \{ T(v_{k}+1) , \dots, T(v_{n})\}$