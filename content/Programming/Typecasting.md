---
tags:
  - datatype
---
https://www.w3schools.com/java/java_type_casting.asp
Is a method used to convert data types to other datatypes. Similar to [[Parsing]] and [[Serialization]]

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
done automatically when you 
```java
Person p;
p = new Student("hink",19231); // casted to Person
```
Casts to parent, so calling child methods are not possible.
# Downcasting(Manual)
When you cast a parent object into a child object
```java
Person s;
Student q = (Student)s; // turn Person into Student
```