---
tags:
  - programming
  - machine_learning
---
A fast batch processing model for question answering with confidence scores on its [[Logit]] attribution.
- Used for [[Model Context Protocol|MCP]] tools
User sends Jev:
- State JSON describing current situation
- Question decisions about the state
# Question Types
- `Noul`: Binary yes/no questions (`0.0` - `1.0`)
- `Choice`: Pick one option from a list you define (up to 255 options)
- `Score`: Output in an ordered list 