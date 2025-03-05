---
tags:
  - programming
---
A programming standard used to explicitly state when checking variables with constant values.

Usually a conditional statement would be written as:
```
if (value == 42) { /* ... */ }
// Reads like: "If the value equals 42..."
```
Yoda conditions describe the same expression, but reversed:
```
if (42 == value) { /* ... */ }
// Reads like: "If 42 equals the value..."
```