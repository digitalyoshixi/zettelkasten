---
tags:
  - proofs
  - programming
  - math
aliases:
  - Proving Language Is Not Regular
  - PL
  - P.L
---
Used to prove a language is not regular.
![[Pumping Lemma-20250930005403986.webp|335]]
# Lemma
- Given $L$ as a [[Regular Language]]
- $\forall$ [[String]] $s \in L$, $\exists$ $s'$ comprised of $s$ and a subsequence in $s$ that can be repeated/pumped forever s.t $s' \in L$
# Alternative Lemma
1. If $L$ is a [[Regular Language]]
2. Then, there is an integer $n > 0$ with the property that:
   $(*)$ for any stirng $x \in L$ where $|x| \geq n$, there are strings $u,v,w$ s.t:
	1. $x = uvw$
	2. $v \neq \epsilon$
	3. $|uv| \leq n$
	4. $uv^{k}w \in L, \forall k \in \mathbb{N}$
# Disproof Structure
1. Suppose $L$ is [[Regular Language]]
2. Since $L$ is regular, we apply [[Pumping Lemma]] and assert there is a $n > 0$ that satisfies $(*)$
3. Give a particular string $x$ s.t
	1. $x \in L$
	2. $|x| > n$
4. By pumping lemma, there are strings $u,v,w$. Pick specific $k \in \mathbb{N}$ s.t $uv^{k}w \not \in L$ 
5. Then, we have proved that this language is not regular.
# Examples
- [[Pumping Lemma Disproving Regular Language Example]]
# Proof of P.L
1. Suppose $L$ is regular
2. Then, let $M$ be a [[Deterministic Finite Automaton|DFSA]] s.t $\mathcal{L}(M) = L$ by [[Big Result|The Big Result]]
3. Let $n$ be the number of states in $M$
4. Then, $x = a_{1} a_{2}, \dots, a_{n}$
5. The states include $q_{0}, q_{1}, q_{2}, .., q_{n}$
6. $q_{i} = \delta^{*}(s_{1}, x[:i])$ This is the state you get to after reading the first $i$ symbols.
7. Denote $u = a_{1}a_{2}\dots a_{i}$
8. Denote $v = a_{i+1}\dots a_j$
9. Denote $w = a_{j+1}\dots a_{n}$
10. Then, $a_{|x|} \in L$
11. Then $q_{|x|} \in F$
12. Then, we get that every repeated $v$ allows $uvw$ to be in the language