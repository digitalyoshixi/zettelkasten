---
tags:
  - programming
  - prolog
---
# Query on [[Prolog Atom]]
```verilog male(charlie).
female(charlie).
?- male(charlie).
true
?- male(eve).
false
```
# Query Against [[Prolog Variable]]
```verilog
?- female(Person).
Person = alice;
Person = eve;
false
```
# Query Joined Query
```verilog
?- female(Person),parent(Person).
Person = eve;
false
```