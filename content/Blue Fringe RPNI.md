---
tags:
  - verification
---
A [[Passive Automata Learning]] algorithm. It is a revised [[Regular Positive and Negative Inference|RPNI]] that delays merging. 
# Algorithm
![[Blue Fringe RPNI-20260705213931875.webp]]
- States are either red,white,blue
	- Tree starts red
	- Immediate successors by transitions are blue
	- All other states are white
- Red states form stable part of current DFA $w.r.t$ mergings
- Second stage tries to merge blue states with all red states, if unmergable then make this blue a red state