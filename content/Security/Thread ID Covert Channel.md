---
tags:
  - security
  - os
---
Thread IDs can allow processes to probe and infer system state of other processes.
- Thread IDs grow sequentially
- Process A can communicate with process B with process B making a thread, process A creating many threads, process B making another thread and checking its thread ID
Was replaced in [[Secure Embedded L4|seL4]] with [[IPC Endpoint]]