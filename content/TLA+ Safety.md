---
tags:
  - verification
---
A [[TLA+ Property]] $P$ is safe if for all [[TLA+ Behavior]] $b$, $b \models P \Longleftrightarrow s \models P, \forall s \text{ where s is a prefix of b}$
- In other words, b satisfies $P$ iff every prefix of $b$ satisfies $P$
- $b \models P$ is false iff there is a prefix that is false