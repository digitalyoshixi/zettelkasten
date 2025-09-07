---
tags:
  - cpp
aliases:
  - __unwind
---
A [[IDA]] shorthand used to encompass [[C++ Try Catch Blocks]].
```cpp
void may_throw_transformed() 
{
  if ( rand() % 2 )
    throw -1;

  string s0 = "0";

  // Implicit tryMaking C++ Exception Handling Smaller on x64
  __wind {
    if ( rand() % 2 )
      throw 0;

    string s1 = "1";

    // Implicit try
    __wind 
    {
      if ( rand() % 2 )
        throw 1;

      printf("%s %sn",
        s0.c_str(),
        s1.c_str());
    }

    // Implicit catch
    __unwind
    {
      s1.~string();
    }
    s1.~string();
  }

  // Implicit catch
  __unwind 
  {
    s0.~string();
  }
  s0.~string();
}
```