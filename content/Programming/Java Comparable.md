---
tags:
  - java
---
This is a class modifier that allows for the class to be compared to other classes (or itself). 
A `compareTo(class_name arg)` method is provided that returns an integer that represents how much greater the current object is than the calling object.
# Boilerplate
```java
// comparable with other class
public class myClass Comparable<otherClass> {
    int compareTo(otherClass obj);
}
// comparable with itself class
public class myClass Comparable<myClass> {
    int compareTo(otherClass obj);
}
```