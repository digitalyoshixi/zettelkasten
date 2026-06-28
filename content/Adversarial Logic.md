---
tags:
  - security
---
A type of [[Incorrectness Logic]] has three fragments:
- Core rules same as incorrectness logic with $\epsilon$ symmetry
- Communication rules for protocol
- Knowledge rules for adversaries to infer new knolwedge
# Structure
$$
\{ ok:P \} c_{p} \{ ok:Q \} \\
\{ ad:A \} c_{a} \{ ad:B \} \\
\{ \epsilon:X \} c \{ \epsilon:Y \}\\
\{ ok:P \} \{ ad:A \} p || a \{ ok:Q \} \{ ad:B \}
$$
with $\epsilon \in \{ ok,ad \}$
# Blogs
- https://langsec.org/spw23/slides/Vanegue.pdf