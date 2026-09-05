---
tags:
  - security
  - programming
aliases:
  - Frida Hexdump
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
### Writing Numbers
```js
addr.writeInt() // write integer to given address
addr.writeUInt() // write unsigned integer to given address
addr.writeS8() // write signed 8-bit integer to given address
addr.writeShort() // write short integer to given address
addr.writeFloat() // write float to address
addr.writeDouble() // write double to address
addr.writeLong() // write long to address
addr.writeULong() // write unsigned long to address
addr.writeUShort() // write unsigned short to address
addr.writeUs8() // write unsigned 8-bit to address
```
### Converting to Integer
```js
number.toInt32() // already a number
numptr.readInt() // read int from given address
numptr.readUInt() // read int from given address
numptr.readS8() // read singed 8-bit integer from address
numptr.readShort() // read short integer from given addres
numptr.readFloat() // read float from given addres
numptr.readDouble() // read double from given addres
numptr.readLong() // read long from given addres
numptr.readULong() // read unsigned long from given addres
numptr.readUShort() // read unsigned short from given addres
numptr.readUS8() // read unsigned 8-bit integer from given addres
```
# Pointers
```js
addr.readPointer() // read pointer value
myBaseAddr = Module.findBaseAddress('myLib.so')
Process.enumerateModulesSync()
```
# Hexdump
```
hexdump(address, [,options])
```
Where options can be:
```
{
    offset: number,
    length: number,
    header: true|false,
    ansi: true|false,
}
```
![[Frida API-20260624015045418.webp]]