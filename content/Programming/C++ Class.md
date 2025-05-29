---
tags:
  - programming
  - cpp
---
C++ classes.
# Concepts
- [[C++ Constructor]]
- [[C++ Destructor]]
- [[C++ Private]]
- [[C++ Virtual]]
# Boilerplate
```cpp
#ifndef CLASS_NAME_H
#define CLASS_NAME_H

class ClassName {
public:
    // Constructors
    ClassName();
    ClassName(int value);
    
    // Destructor
    ~ClassName();

    // Member functions
    void someFunction();
    int getValue() const;

private:
    // Member variables
    int someValue;
};

#endif
```