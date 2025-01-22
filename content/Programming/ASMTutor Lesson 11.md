---
tags:
  - ASMTutor
  - x86
---
### Lesson 11 ITOA(integer to ascii)

We will make an algorithm to convert integers into ascii characters.

What we can do is get all digits in a decimal number is to divide the number by 10. Keep the remainder of the division and keep dividing the quotient rounded down of the division. Eventually the remainders we get will be the digits in reverse order. Here is an example for 2706:

2706/10

Quotient RD= 270, remainder = 6

270/10

Quotient RD = 27, remainder = 0

27/10

Quotient RD = 2, remainder = 7

2/10

Quotient RD = 0, remainder = 2

The remainders are 6072 which is reverse of 2706

Now that we know each digit, use the same methodology to convert decimal to ascii. By adding 48 to each of these digits

  

The operand we use for this quotient and remainder division is idiv. It divides eax by whatever register you give it. And stores the quotient in eax and remainder in edx

We want to use the esi register for this second register that divisor eax. esi is a general purpose register but its main use is for source index