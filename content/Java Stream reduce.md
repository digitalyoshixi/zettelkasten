---
tags:
  - programming
  - java
---
```java
int result = numbers.stream().reduce(0, Integer::sum);
assertThat(result).isEqualTo(21);
```
- Calls a [[Reducer Function]] that is a binary function
- First argument is the identity for the reducer