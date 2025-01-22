---
tags:
  - ASMTutor
  - x86
---
### Lesson 16 ATOI(ascii to integer)

Does not require heavy math like itoa. Know that ascii is stored over the span of multiple address spaces and each will hold one character. What we can do with this knowledge is parse through all address spaces which we know contain the number and check if its a number(between 48 to 57).

If it is in fact a valid integer, then we add it to eax and multiply eax by 10. The reason we do this is because this is decimal numbering system. We know the first number we pop out will be the largest digit. Here follow this logic:

8 is first digit we get

2 is second digit we get

1 is last digit we get

Eax = 0

Eax = 8

Eax = 80

Eax = 82

Eax = 820

Eax = 821

Eax = 8210

At the end, we divide by 10. This leads us to find the correct digit here: 821.