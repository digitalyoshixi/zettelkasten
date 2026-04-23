---
tags:
  - programming
  - bash
---
Used as a [[Break]] to exit out of loops.
```bash
#!/bin/bash

for i in `seq 100`; do
  if [ $i -eq 20 ]; then
    break
  fi
  echo $i
done
```