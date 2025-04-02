---
tags:
  - cpp
  - programming
---
This is a new feature, not required as it is done by default.
`override`
Allows for child classes [[Function Overwriting]]

```cpp
class Parent {
        // overridden function
        int name_of_the_function() {
	        // some logic
        }
};

class child : public Parent {
        // overriding function
        int name_of_the_function() override {
	        //some logic
        }
};
```