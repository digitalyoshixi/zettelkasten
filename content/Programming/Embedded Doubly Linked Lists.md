---
tags:
  - programming
---
A data structure specific to [[Windows]].
Embeds a internal `_LIST_ENTRY64` data structure that contains:
- Pointer to successor's embedded `_LIST_ENTRY64` (Flink)
- Pointer to predecessor's embedded `_LIST_ENTRY64` (Blink)
You can calculate the base address of element by subtracting the offset of the embedded `_LIST_ENTRY64` structure within that element.
![[Embedded Doubly Linked Lists-20260323032215991.webp]]