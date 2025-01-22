---
tags:
  - os
---
1. A PC boots up
2. A current is sent through a 'power good' wire to awaken the CPU
3. [[Preboot Execution Environment|PXE]] loads if it is enabled
4. The CPU, then accesses the first line of the [[Power-On Self-Test|POST Program]] on the [[Read Only Memory|ROM]]
5. After POST diagnostic finishes, the CPU loads its [[Bootstrap Loader]]
