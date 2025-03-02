---
tags:
  - programming
---
# O(log n)
Very very efficient.
Most of the time it is base 2
O(8) -> 3 as an example.
less lines for every value.
# Example
- [[Binary Search|Binary Search]]
- [[Binary Search Tree]]
### Example Program
```java
public int reverseLog(int n){
int result = n;
int power = 0;
while (result > 1){
	result /= 2;
	power++;
}
return power;
```
dependant on which power of 2. for example, if our argument is 69, the program would follow a process like this:

| result | power |     |
| ------ | ----- | --- |
| 69     | 1     |     |
| 34     | 2     |     |
| 17     | 3     |     |
| 8      | 4     |     |
| 4      | 5     |     |
| 2      | 6     |     |
| 1      | 7     |     |