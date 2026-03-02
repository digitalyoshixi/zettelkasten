---
tags:
  - programming
  - java
---
```java
int result = numbers.stream().reduce(0, Integer::sum);
assertThat(result).isEqualTo(21);

// alternative function call with binary functions
BiFunction<Boolean, BooleanExpression, Boolean> acc = (x, y) -> x && y.evaluate(context);
expressions.stream().reduce(true, acc, (x,y) -> x && y); // returns a boolean
```
- Calls a [[Reducer Function]] that is a binary function
- First argument is the identity for the reducer