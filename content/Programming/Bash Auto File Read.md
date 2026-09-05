---
tags:
  - programming
  - bash
aliases:
  - Bash Auto Script
---
```bash
#!/bin/bash

# Configuration
INPUT_FILE="ips.txt"
CMD="dig +short MX"

while IFS= read -r ip || [[ -n "$ip" ]]; do
    [[ -z "$ip" ]] && continue
    echo "Querying: $ip"
    $CMD "$ip"
    echo "-------------------"
done < "$INPUT_FILE"
```