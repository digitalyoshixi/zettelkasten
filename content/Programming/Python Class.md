---
tags:
  - python
---
```python
class Template(object):

    def __init__(self):
        self.value = "hello"
        self.other_value = "bonjour"
        self.constant_value = 42
        current_class = self.__class__
        inits = []
        while (current_class.__name__ != "Template"):
            inits.append(current_class.init)
            current_class = current_class.__bases__[0]
        for i in reversed(inits):
            i(self)

    def init(self):
        pass

    def info(self):
        print self.value
        print self.other_value
        print self.constant_value
        print ""
        
    def __repr__(self):
	    return "my serialized string representation here"
```