---
tags:
  - programming
aliases:
  - CMakeLists.txt
---
The configuration file for [[Cross Platform Make|CMake]].
# Single Build Example
```
cmake_minimum_require(VERSION 3.10)

project(hellow)

add_executable(hellow hellow.c)
```
# Linking Example
```
cmake_minimum_require(VERSION 3.10)

project(main)

add_executable(main main.c random.c random.h)

target_link_libraries(main PRIVATE m)
```