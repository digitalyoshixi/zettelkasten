---
tags:
  - OOP
---
![[Pasted image 20231129144713.png]]
YOU REALLY SHOULD NOT MAKE YOUR CLASSES PUBLIC!
PUBLIC ALLOWS YOU TO DO THINGS LIKE DIRECTLY MODIFY ATTRIBUTES
LIKE 
```java
Fraction myman = new Fraction();
myman.num = 10; // BAD PRACTICE!!. DIRECT MODIFICATION
```

Instead you should use [[Accessors and Mutators]] 
