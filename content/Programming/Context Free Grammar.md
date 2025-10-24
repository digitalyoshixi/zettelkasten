---
tags:
  - programming
  - linguistics
aliases:
  - CFG
---
A finite collection of [[Productions|Production Rules]] which tell us whether certain strings or sentences are grammatical or not.

A grammar is context free if it is in the form of:
$$G \to (V \cup T)^{*}, G \in V$$
- $G$ is the grammar
- $V$ is a variable or [[Non-terminal]]
- $T$ is a [[Terminal]]
# 4-Tuple Definition
A CFG is a 4 tuple:
$G = (V, \Sigma, P, S)$ where:
- $V$ is a finite set of variables
- $\Sigma$ is a finite set of [[Terminal|Terminals]]
- $P$ is a finite set of [[Productions|Production Rules]]
- $S$ is a particular start element $\in V$
# Concepts
- [[Productions]]
- [[Example CFG]]