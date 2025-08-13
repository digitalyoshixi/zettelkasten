---
tags:
  - programming
aliases: []
---
`super()` bypasses [[Method Overriding]] if you override a method called the same name.
# Super Constructor
`super()` is called by default, unless you explicitly call it.
Used to call the constructors of the super class
```java
super() // use parent's constructor
```

```java
super(arguments) // use parent's constructor with args
```
# Super Methods
```java
super.methodname(arguments) // use parent's method. only when you have overwritten functions
```
