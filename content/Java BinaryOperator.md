---
tags:
  - programming
  - java
---
Creating a custom binary operator that can be applied to functions
# Example
```java
BinaryOperator<Boolean> myand = (x,y) -> x && y;

myand.apply([true, false]); // false
```