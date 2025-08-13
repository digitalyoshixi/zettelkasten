---
tags:
  - datatype
aliases:
  - Java Upcasting
  - Java Downcasting
---
https://www.w3schools.com/java/java_type_casting.asp
Is a method used to convert data types to other datatypes. Similar to [[Java Parsing]] and [[Serialization]]
# Widening(Implicit/Automatic)
```java
int y = 0;
double x = y; // implicit casting
```
when you just reinitialize the variable
# Narrowing(Explicit/Manual)
```java
double x = 10.5;
int y = (int)x;
```
you manually type the data point before the variable
# Upcasting(Automatic)
When you turn a Child object into a Parent object
done automatically when you attempt to cast.
```java
Person p;
p = new Student("hink",19231); // casted to Person
```
Casts to parent.
- Keep's childs overwritten methods
- Removes child's specific attributes
The child is referred to as the [[Running Type]]
# Downcasting(Manual)
When you cast a parent object into a child object. Not always possible
```java
Person s;
Student q = (Student)s; // turn Person into Student
```