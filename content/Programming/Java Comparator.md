---
tags:
  - programming
  - java
---
A [[Java Interface]] used to sort array order with custom sorting logic.
# Example
```java
//NameSorter.java
import java.util.Comparator;
public class NameSorter implements Comparator<Employee>
{
    @Override
    public int compare(Employee e1, Employee e2) {
        return e1.getName().compareToIgnoreCase( e2.getName() );
    }
}
```
# Difference between [[Java Comparable]]
https://www.geeksforgeeks.org/java/comparable-vs-comparator-in-java/