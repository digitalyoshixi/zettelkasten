---
tags:
  - verification
---
A [[Random Oracle|Oracle]] used to test if an item is part of a set
# Formal Definition
For a given string $w \in \Sigma^{*}$ return whether $w$ is accepted by target language in mealy machine setting
# LearnLib
```
MembershipOracle<I,O>
```
- `I` is input type
- `O` is output type`