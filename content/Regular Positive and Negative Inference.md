---
tags:
  - verification
  - programming
aliases:
  - RPNI
---
An [[Passive Automata Learning]] algorithm to learn specification from positive and negative samples.
# Algorithm
Construct a [[Prefix Tree Acceptor]] to try and merge each state pair and check DFA against negative samples to verify DFA is not overgeneralizing.