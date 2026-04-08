---
tags:
  - programming
  - java
---
A sequence of elements from a source like:
- [[Java Collection]]
- [[Java Arrays]]
Created to allow:
- Operations of stream to return a stream ([[Stream Pipeline]])
- New data to be computed on demand (Allows for [[Producer Consumer Relationship]])
- Usage with [[Java Lambda Function]]
# Creating Stream
```java
Stream<Integer> stream = Stream.of(1,2,3,4,5,6,7,8,9);
stream.forEach(p -> System.out.println(p));

// stream from list
List<String> list = Arrays.asList("myst", "tone", "wavers");
Stream<String> stream = list.stream();

// convert back to list
List<String> backtolist = stream.toList();
```
# Running Functions on Stream
- [[Java Stream map]]
- [[Java Stream filter]]
- [[Java Stream reduce]]
- [[Java Stream sorted]]
- [[Java Stream forEach]]