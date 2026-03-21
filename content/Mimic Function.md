---
tags:
  - security
  - cryptography
  - forensics
---
A mimic function changes a file $A$ s.t that it assumes properties of file $B$.
# Formal Definition
- For some given threshold $n$
- If $p(t,A)$ is the probability of some string $t$ occuring in $A$
- Mimic function $f$ recodes $A$ s.t $p(t, f(A))$ approximates $p(t,B)$ for all strings $t$ with length less than $n$