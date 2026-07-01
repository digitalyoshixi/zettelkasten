---
tags:
  - verification
  - programming
aliases:
  - RPNI
---
An [[Passive Automata Learning]] algorithm to learn specification from positive and negative samples.
# Complexity
$$
O(p^{3}n)
$$
- $p$ is the sum all positive strings
- $n$ is the size of negative data
# Algorithm
1. Construct a [[Trie|Prefix Tree]] accepting all the positive samples
2. [[State Merge]] each state pair to generalize the [[Deterministic Finite Automaton|DFA]] state (Note that this will make it a [[Non-Deterministic Finite Automaton|NFA]])
3. check [[Deterministic Finite Automaton|DFA]] against negative samples to verify [[Deterministic Finite Automaton|DFA]] is not overgeneralizing.