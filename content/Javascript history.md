---
tags:
  - programming
  - javascript
---
# Adding New Session History
```
history.pushState("", "", "/?aa=20")
```
- Adds current page with the argument aa=20 to session history
- Causes `Referer` header to contain this entry