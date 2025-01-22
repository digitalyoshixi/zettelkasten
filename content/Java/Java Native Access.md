---
tags:
  - java
aliases:
  - JNA
---
a [[Java]] library that allows you java programs to access native libraries like the [[Win32 API]]
or [[X11]] features.
It is the more simplified version of inline native language: [[Java Native Interface|JNI]]

# Installation
Java does not have a traditional package manager like python does with [[pip]]
rather, java libraries are [[jar]] files to contain class files which are the java libraries.
1. Download the .jar file. https://github.com/java-native-access/jna
2. Run `java -cp /path/to/your/file.jar YourMainClass`
3. Example: ![[Java Native Access-20231007233350171.webp]]
You must also install jna platform.
