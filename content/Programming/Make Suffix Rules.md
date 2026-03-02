---
tags:
  - programming
  - c
---
Target names in the form `.FROM.TO` used to launch actions based on extension
```c
.SUFFIXES: .txt .html
# from html to txt
.html.txt:
	lynx -dump $c > $@
```