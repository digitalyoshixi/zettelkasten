---
tags:
  - programming
  - java
---
A function that runs for all elements of a stream (element-wise).

```java
Stream<Integer> stream = Stream.of(1,2,3,4,5,6,7,8,9);
stream.forEach(p -> System.out.println(p));
```