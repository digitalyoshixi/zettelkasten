---
tags:
  - security
  - programming
---
# Strings
### Allocate Strings
```js
Memory.allocAnsiString(mystr); // Allocate ANSI string (windows only)
Memory.allocUtf8String(mystr); // Allocate UTF8 Strings
Memory.allocUtf16String(mystr); // Allocate UTF16 Strings

const myTestString = Memory.allocAnsiString("Hello World");
```
### Read Strings
```js
stringptr.readCString();
stringptr.readAnsiString();
stringptr.readUtf8String();
stringptr.readUtf16String();

stringptr.readCString(1024);
```
# Numbers
### Converting to Integer
```js
number.toInt32() // already a number
numptr.readInt() // read int from given address
numptr.readUInt() // read int from given address
numptr.S8() // read int from given address
```
### Converting 