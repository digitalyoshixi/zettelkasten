---
tags:
  - programming
  - prolog
---
# Direct Query
```verilog
male(charlie).
female(charlie).
?- male(charlie).
true
?- male(eve).
false
```
# Query Search Multiple
```verilog
?- female(Person).
Person = alice;
Person = eve;
false
```
# Query Join Query
```verilog
?- female(Person),parent(Person).
Person = eve;
false
```