---
tags:
  - programming
  - os
  - graphics
aliases:
  - OpenCL Command Queue
---
A single queue that manages and schedules commands in a [[OpenCL Context]].
Command queues are unique to a given [[OpenCL Context]].
# Example
```
Context (the workspace)
├── Device 1 (GPU)
│   ├── Command Queue A → [copy data, run kernel, copy results]
│   └── Command Queue B → [different operations...]
├── Device 2 (CPU)
│   └── Command Queue C → [other operations...]
└── Shared Memory Objects (visible to all devices in context)
```