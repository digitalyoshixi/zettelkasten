---
tags:
  - math
---
Hex is base 16 number system

Like binary, there are only 8 digits. We still have the routine 0,1,2,3,4,5,6,7,8,9 (10 digits) but, we add A,B,C,D,E,F.

A = 10

B = 11

C = 12

D = 13

E = 14

F = 15

Because hexes use letters, they are often prefaced with an identifier. Common ones include: 0x,#,%

Also like binary, the leftmost digit represents 16^0, the 2nd left is 16^1, 3rd is 16^2 and so on. Now, if you have a number in the column, it represents number*column#. Example is E in the 2nd place. It is 14*16.

2,147,483,647 is the largest number in hex

  

The golden principle to understanding number systems is to know that whatever is in the tenth’s place corresponds to the digit limit of that system. Eg: 10 in decimal = 10, 10 in binary = 2, 10 in hex = 16

Hexadecimals 4 bits long are called a nibble

  

### Hexadecimal addition

Remember these 2 rules for hexadecimal addition

1. If the result is less than 16,write that digit as the sum for that position.
    
2. If it is greater than 16, subtract 16 from it to get the digit and carry 1 to the next digit.
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iva8_tmp_f257f7618e4fe2cb.png)
### Logical shifts

For a hexadecimal, when you logical shift to the left(move all digits left by one and add a 0 place), you end up with double the number you started with. Eg: 1010 shifted is 10100

1010 = 10

10100 = 20

Similarly, a logical shift to the right would halve the number you give it.

1010 = 10

0101 = 5

  

### Rotational shifts

For hexadecimals, a rotational shift is when you move the last/first number to the front/back.

A rotational shift to the right will move the rightmost digit to the front. Eg:

00000101 -> 10000010