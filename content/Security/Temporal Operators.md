---
tags:
  - verification
---
# Always
```
[][Event]_invariant
```
Is [[Syntactic Sugar]] for:
```
Event \/ (invariant' = invariant)
```
- Event happens or invariant does change ([[Stuttering Insensitive|Stuttering Step]])
- [[TLA+ Safety]]
# Eventually
```
<>(Event)
```
- Eventually the `Event` becomes true
- [[TLA+ Liveness]]