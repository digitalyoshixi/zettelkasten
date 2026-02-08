---
tags:
  - java
---
This is a [[Java Interface]] that allows for the class to be compared to other classes (or itself). Branched off from [[Java Comparator]]
# Making a Class Comparable
1. Allow the class to `implements Comparable` (See [[Java Interface]])
2. Create a `compareTo(class_name arg)` that returns an integer that represents how much greater the current object is than the calling object.
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