---
tags:
  - security
  - malware
---
A algorithm that adds more YARA rules to an existing YARA rule if it matches to similar conditions as other YARA rules, during scan-time.
Allows deeper scanning to allow rules to match with more similar results.
# Example
1. Scan assist notices that your rule only matches PE files
2. Scan assist will fine-tine you rule to only match PE files going forward
   ![[Scan Assist-20250808014348605.webp|353]]