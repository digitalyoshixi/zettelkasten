---
tags:
  - cpp
---
Strings imported with 
`#include <string>`
Create a string like:
```cpp
std::string mystring {"david"};
```
Strings can adapt their length on the spot.
```cpp
std::string mystring {"jajo"};
mystring = "jajoy"; // it is allowed
mystring = "jja"; // also allowed
```
# .length()
this method returns the length as a unsigned integer
If you want, you can typecast this uint
```cpp
static_cast<int>(name.length()) 
```
Alternatively, you can use `.ssize()` to get the length of string as signed integer

# The Expense of Strings
Strings are expensive. You should avoid making copies of strings and should always pass by reference to the variable rather than passing by value.

# String Literal Suffix
If you need to do quick literal typecasting(to avoid C-style strings) 
```cpp
using namespace std::string_literals; // easy access to the s suffix
std::cout << "goo\n"s;  
```
# Constexpr
There is no constexpr for strings

# std::string view
a read-only string.
Saves on memory required, rather than an entire string
Implicitly typecasted from string
```cpp
#include <iostream>
#include <string_view>
#include <string>

void readstr(std::string_view str){
    std::cout << str;
}

int main(){
    std::string mystr {"david"};
    readstr(mystr);
    return 0;
}
```
string views have the suffix sv
you can use constexpr on string views
