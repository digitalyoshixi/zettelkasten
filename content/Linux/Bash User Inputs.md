---
tags:
  - bash
  - IO
  - programming
---
done with the `read` method. You dont even need to [[Initialization]] the variable beforehand

```bash
#!/bin/sh
read a
echo "$a" # use quotations to allow whitespace, stars, etc
```