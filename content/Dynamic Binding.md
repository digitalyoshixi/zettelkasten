---
tags:
  - java
aliases:
  - Dynamic Binding
---
A part of [[Polymorphism]].

Used at [[Runtime]] when a [[Method]] is called to look up the appropriate method to call for [[Dynamic Dispatch]] to run.
# JVM Binding Process
[[Java Virtual Machine|JVM]] will first check the existing class for implementation, then check subsequent [[super]] classes if the implementation does not exist.