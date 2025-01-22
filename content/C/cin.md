---
tags:
  - IO
  - cpp
---
character input reads from system.in from keyboard. you must use the [[Extraction Operator]] to store the variable from input
```cpp
int x{};
std::cin >> x;
```

# Multi Inputs
If you want to have the user input several things on same line seperated by space:
```cpp
int x{};
int y{};
std::cin >> x >> y; // 2 numbers store in x and y respectively
```
`input:7 8`
`x=7, y=8`

the C++ IO library requires us to press *enter* in order to read input. there are other methods of accepting input too with third party libraries
### Unintended Effects
cin ends after whitespace, you previous input is fed into the stream for the next cin to gobble up.

For example: if you enter `John Joe` as the input, and you setup 2 `std::cin >> somevar` 
the solution is to use [[getline()]]

# Input Auto-filter
Sometimes when we have initiated variables like `int x`, and we feed it some numbers and string from input like `99a182`, the reader continues reading memory until it find some block of memory that is not an integer, so it would make the `x=99`
### Input Carry-over
Inputting more than one character when asking for inputted chars, will make the next inputted char carry over from the previous input