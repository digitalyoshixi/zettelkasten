---
tags:
  - web
  - programming
aliases:
  - XPE
---
A parameter that can be used elsewhere in the [[Document Type Definition|DTD]].
- Denoted by `%`
```
<!ENTITY % myparameterentity "my value" >
```
Referenced by:
```
%myparameterentity;
```