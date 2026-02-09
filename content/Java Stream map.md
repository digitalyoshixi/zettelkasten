---
tags:
  - programming
  - java
---
```java
memberNames.stream().filter((s) -> s.startsWith("A"))
                  .map(String::toUpperCase)
                  .forEach(System.out::println);
```