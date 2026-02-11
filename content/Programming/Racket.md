---
tags:
  - programming
  - lisp
---
A descendant of [[Scheme]]
It is a [[Imperative Programming|Imperative Language]] with a [[Functional Programming]] core.
- Static scoping
- Dynamic typing
- Uniform treatment of program and data
- Proper [[Tail Recursion]]
- Functions are values
- Pass by value
# Installation
```
sudo pacman -S racket
```
# Running File
```
racket myfile.rkt
```
Or:
```
racket -f myfile.rkt -i
```
# Boilerplate
```
#lang racket

(provide export1 export2)

; body
```
# Concepts
### Fundamental
- [[Racket Expression]]
- [[Racket Definitions]]
- [[Racket Datatypes]]
- [[Racket Symbol]]
- [[Racket Boolean]]
- [[Racket Pair]]
- [[Racket List]]
- [[Racket String]]
- [[Racket Vector]]
- [[Racket Lookup Table]]
- [[Racket Hash Table]]
- [[Read-eval-print-loop]]
- [[Racket Procedure]]
- [[Racket Higher Order Procedure]]
- [[Racket Parameter List]]
- [[Racket Scope]]
- [[Racket Closure]]
- [[Racket Full Function Definition]]
- [[Racket Evaluation]]
	- [[Evaluation by Substitution]]
	- [[Racket Special Forms]]
	- [[Racket Continuation]]
- [[Reducible Expression]]
- [[Continuation]]
- [[Racket Comment]]
- [[Racket provide]]
- [[Racket require]]
### Procedures
- [[Racket add]]
- [[Racket subtract]]
- [[Racket multiply]]
- [[Racket divide]]
- [[Racket remainder]]
- [[Racket =]]
- [[Racket quote]]
- [[Racket equal?]]
- [[Racket not]]
- [[Racket and]]
- [[Racket or]]
- [[Racket if]]
- [[Racket cond]]
- [[Racket lambda]]
- [[Racket map]]
- [[Racket fold]]
- [[Racket apply]]
- [[Racket first]]
- [[Racket rest]]
- [[Racket append]]
- [[Racket list-ref]]
- [[Racket length]]
- [[Racket member]]
- [[Racket reverse]]
# Libraries
- [[Racket Tests]]
- [[Racket trace]]
# Guides
- [[Racket Style Guide]]
- [[Racket Early Exit]]
- [[Racket Print Debugging]]