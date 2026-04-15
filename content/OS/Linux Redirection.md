---
tags:
  - os
aliases:
  - Linux Output Redirection
  - Linux Input Redirection
  - Stream Redirection
  - Bash Redirection
  - Append Redirection
---
Changing the standard input and standard output from the command line.
# Input Redirection
Provides hello as input
```
./program < "hello"
```
# Output Redirection
Outputs the results into a file.
Overwrites entire file
```
./program > result.txt
```
### Redirection with [[File Descriptor]]
```
./somethingthatprintstostderr 2> output.txt
```
- Pipes [[Standard Error|stderr]] ([[File Descriptor|FD]] 2) to output.txt
# Append Redirection
Outputs results by appending into file
```
./program >> result.txt
```