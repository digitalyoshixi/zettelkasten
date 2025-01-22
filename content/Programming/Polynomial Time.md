---
tags:
  - programming
---
Quadratic algorithms
# Examples
- [[Strassen's Matrix Multiplication]]
- [[Bubble Sort]]
- [[Selection Sort]]
- [[Insertion Sort]]
- [[Bucket Sort]]
### Example Program O(n^2)
We run n^2 lines
```java
int n = 100;
for (int i = 0; i<n;i++){
	for (int i = 0; i<n;i++){
		System.out.println("hi");
	}
}
```
$f(n) = n^2$
```java
int n = 100;
for (int i = 0; i<n;i++){
	for (int i = 0; i<n;i++){
		System.out.println("hi");
		System.out.println("hi");
	}
}
```
### Alternate Example
$f(n) = 2n^2 + 3n + 1$
```java
int n = 100;
for (int i = 0; i<n;i++){
	for (int i = 0; i<n;i++){
		System.out.println("hi");
		System.out.println("hi");
	}
}
for (int i = 0; i<n;i++){
		System.out.println("hi");
		System.out.println("hi");
		System.out.println("hi");
}
System.out.println("hi");
```

We denote all of these as O(n^2) even if there are multiple terms. its dictated with the highest order. O(n^2)