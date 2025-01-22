---
tags:
  - cpp
---
`# define` [[Preprocessor Directives|Preprocessor Directive]] used to create macros.
There are 2 types of directives:
- Object-like Macros <- *variables are better*
- Function-like Macros <- *ill advised use case. use normal functions instead*

# Object-like Macros
### Without Substitution Text
```cpp
#define identifier
```
Any further occurrence of the identifier is removed and replaced by nothing!
### With subsitution Text
```cpp
#define identifier substitution_text
```
example:
```cpp
#define MY_NAME "Alex"

int main()
{
    std::cout << "My name is: " << MY_NAME << '\n';

    return 0;
}
```
# Function Macros
I love these, but apparently theyre bad practice.
```cpp
//MAKE THE MACRO. '\' are to distinguish between lines
#define process_button(b,vk)\ 
case vk: {\
input.buttons[b].is_down = is_down;\
input.buttons[b].changed = true;\
} break;

process_button(BUTTON_UP,VK_UP)
```
