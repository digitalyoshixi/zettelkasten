---
tags:
  - programming
  - math
---
# Installation
```
git clone https://github.com/Semyazi/language-verifier
```
# Example
Create a regex to match the language
$$ \{  x \in \Sigma^{*} : \#_{111}(x) = 2 , \#_{01}(x) = 0 \} $$
```python
import utils
import lang
import dfsa
import cfg
import reg

# Creating language matcher
class L(lang.BaseLanguage):
    a111 = utils.PrefixAutomaton('111')
    a01 = utils.PrefixAutomaton('01')
    def has(self,x):
        o1111 = self.a111.occur(x)
        o01 = self.a01.occur(x)
        return o1111 == 2 and o01 == 0
l = L()
r = reg.RegexLanguage("11110*")
#lang.comp(l, r)

# Creating DFSA
d = dfsa.DFSALanguage(0)
d.r(0,1,1)
d.r(1,1,2)
d.r(2,1,3)
d.r(3,1,4)
d.r(4,0,4)
d.a(4)
#lang.comp(d, r)

c = cfg.CFGLanguage("""
Z > e, 0[Z]
S > 1111[Z]
""")

lang.comp(l,c)
```