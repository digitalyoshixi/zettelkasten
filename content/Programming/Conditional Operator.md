---
tags:
  - cpp
aliases:
  - Ternary Operator
---
`c ? x : y`
- If conditional `c` is `true` then evaluate `x`, otherwise evaluate `y`
Its a shorthand [[C Conditional Statements]]
It also counts as an expression, so you can use it with a similar purpose as a lambda function
```cpp
constexpr bool inBigClassroom { false };
    constexpr int classSize { inBigClassroom ? 30 : 20 };
    std::cout << "The class size is: " << classSize << '\n';
```
