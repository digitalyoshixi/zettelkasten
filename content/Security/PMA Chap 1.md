---
tags:
  - malware
  - books
---

This chapter covers basic static malware analysis techniques. These techniques involve analyzing common malware signatures using signatures or heuristic means. Most antiviruses find malware using common signatures.


### [[Hashing]]

The signature for these malwares is created from a special hash. Through a hashing program, feed it your malware and then it generates a hash for it. This is the fingerprint for malware


### [[Special strings]]

Certain strings like URLS that lead to malicious domains, copy files or print messages can be used to determine if it is malware or not. Usually seen in ascii or unicode, and both ascii and unicode terminate the end of string with a null character.

Windows function names usually start with a capital letter and follow PascalCase

DLLs are libraries many windows processes use.
 

### [[Obfuscation]] and [[Packing]]

Obfuscation is the practice of hiding your code and execution behavior, Packing is the practice of compressing your program. Most real software will not use these techniques, and are loaded with strings. If you find a program with very few strings, it is probably malware. Common DLLs used in obfuscated/packed code is GetProcAddress and LoadLibrary to load additional functions.

Packed files can be detected using PEiD. PEiD is old now, and better software exists: [https://github.com/horsicq/Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy)



### [[Portable Executable]] 

Pe files are dangerous files for windows systems. Contains information for the OS loader to manage the executable code. These files can be exe,dll,screensaver and drivers. They all begin with a header that includes type of application, library functions, space requirements. The PE header is very important to learn information about the code.

  

### [[Linked Libraries]] 

Importing functions from another program is done through linking code libraries.

Static linking links functions at the start of the code. All code from a library is copied into the executable. It is common on linux/unix programs. Linked code and executable code is indifferentiable in programs that use it

Runtime linking is very popular in malware programs. Program only connects to libraries when the function is needed. Uses GetProcAddress. LdrGetProcAddress, LdrLoadDLL, LoadLibrary.

Dynamic linking is the most common in all programs. The functions are declared at the start, but the os only loads the libraries when the program requires that library.

The PE file header is human readable and tells you what libraries are going to be linked. The names of these libraries are often self explanatory aswell

### Imported functions

Located in the PE header of a file. These functions in windows are gathered from the win32 api
### Exported functions

Certain dll or exe files will also export functions for other programs to use. In dlls this is normal, but with exes this is a often rare event. Certain malware authors tend to disguise exported functions as windows functions. With these naming conventions, they fly under the radar. To check if it is legitimate, use window’s dependency walker program.