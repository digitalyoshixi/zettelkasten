---
tags:
  - math
  - linalg
---
# Theorem
1. Suppose $S : U \to V$ is a linear map
2. Suppose $T : V \to W$ is a linear map
3. Then, $ker(S) \subset ker(TS)$
4. Then, $Image(TS) \subset Image(T)$
# Proof
### Proving $ker(S) \subset ker(TS)$
1. Pick $v \in Ker(S)$
2. Calculate $TS(v) = T(S(v))$  by defn of $TS$
3. $= T(0_{v})$ as $v \in Ker(S)$
4. $= 0_{w}$ as $T$ is linear
5. Therefore, $v \in Ker(TS)$ as it follows $Ker(S) = Ker(TS)$
### Proving $Image(TS) \subset Image(T)$
1. Pick $w \in Image(TS)$
2. $w = TS(u)$ by defn of Image
3. $= T(S(u))$ by defn of $TS$
4. $= T(v)$ as $S(u) = V$
5. Therefore, $w \in Image(T)$S