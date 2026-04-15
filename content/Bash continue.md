---
tags:
  - programming
  - bash
---
Used as a [[Continue]] within bash loops.
```bash
#!/bin/bash

for i in `seq 100`; do
  if [ $i -eq 20 ]; then
    continue
  fi
  echo $i
done

```