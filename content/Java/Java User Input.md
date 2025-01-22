---
tags:
  - java
aliases:
  - Java Input
---
How to grabs every string from your user's cursor to the next linebreak character.
![[Pasted image 20230907193116.png]]
You will need to import java.util.Scanner
Then, instantiate a scanner object.
When you want a user input, then you will do variable = scannervariablename.nextLine() or nextInt().
lastly, you want to close the scanner, so sysin can be used again.
### Edge case: Reading a number before a string
![[Pasted image 20230907193700.png]]
For some reason, nextInt() will not read in the escaped character newline. so, it leads to the next scan being a blank input.

The fix is to read as a string first, then convert it to number.
![[Pasted image 20230907194531.png]]
Consult [[Parsing]] For more details