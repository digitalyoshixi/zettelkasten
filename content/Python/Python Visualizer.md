---
tags:
  - python
---
https://pythontutor.com/render.html#mode=display
This is a tool used for debugging python code.
# Frames
These represent scope.
### Global Scope
The global scope holds global variables and methods,
Each function scope may also have global variables and methods
![[Python Visualizer-20241010223758923.webp]]
### Function Scope
![[Python Visualizer-20241010224549319.webp]]
Contains all:
- parameters 
- new variables in scope
- the return value
# Objects
### Functions
When a function is defined, it is stored in the global frame and then the function header is saved in an ID
![[Python Visualizer-20241010224103237.webp]]
### Variables
These Ids are stored directly with the value of the variable.
![[Python Visualizer-20241010225516509.webp]]