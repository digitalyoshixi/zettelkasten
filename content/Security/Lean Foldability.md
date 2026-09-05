---
tags:
  - verification
  - programming
---
Outlines the limit to unfolding (substituting names with definitions).
- `@[reducible]` : Unfold eagerly everywhere
- `@[semireducible]` : Unfold during [[Unification]] and [[Type Checking]]
- `@[irreducible]` : Never unfold the definition, treat it fully opaque