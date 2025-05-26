---
tags:
  - java
---
This is a operator to check the instance of a certain object in [[Java]].
# Checking Instance
```java
public class Ring extends Round {
    // implementation details
}
...
Ring ring = new Ring();
assertTrue(ring instanceof Round);
```