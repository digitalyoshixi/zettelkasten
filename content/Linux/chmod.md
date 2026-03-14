---
tags:
  - linux
---
Setting permissions for files.
# Set Write for user
```
chmod u+w ./file
```
# Set Read for Group
```
chmod g+r ./file
```
# Set Executable for All
```
chmod a+x ./file
```
# Set All Perms With Octal Mode
```
chmod 777 ./file
```
# Set [[suid]]
Anything with a 4 at the start.
```
chmod 4755 ./file
```