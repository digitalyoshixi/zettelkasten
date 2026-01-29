---
tags:
  - programming
  - lisp
---
A [[Racket List]] is defined like
```
(cons 1 (cons 2 (cons 3 '())))
```
Similar to how fold works with function `f` and identity `id`
```
(f 1(f 2(f 3 id)))
```