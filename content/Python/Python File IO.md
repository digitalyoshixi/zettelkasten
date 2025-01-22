---
tags:
  - python
  - os
---
[https://www.youtube.com/watch?v=cIaOisyd7lE](https://www.youtube.com/watch?v=cIaOisyd7lE)
IO is input and output. STDIN and STOUT are special files on the computer.
# Opening File
### Open/Close
You must manually open/close the file
```python
file = open("file.txt", 'r')
contents = file.read()
file.close()
```
### With Open
This automatically closes the file afterwards
```python
with open("file.txt", 'r') as file:
	# operations
```
# Reading File
```python
singleline = file.readline() # returns just one line as a string
lineslist = file.readlines() # returns alist of all lines
contents = file.read() # returns the entire file as a string
# parse through each line
for line in file:
	print(line)
```
### readline()
```python
readline(size=-1, /)
```
##### Read entire file with readline()
```python
    currentline = data_file.readline()
    while currentline:
        print(currentline.rstrip())
        currentline = data_file.readline()
    data_file.close()
```
### readlines()
```python
readlines(size=-1, /)
```
### read()
```python
read(size=-1, /)
```
### tell()
Prints the file position pointer. 
By default it is at position 0.
Everytime you:
- readline, pointer increases by current line's character count
### seek()
Change the value of the file position pointer.