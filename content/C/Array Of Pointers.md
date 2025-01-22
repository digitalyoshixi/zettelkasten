---
tags:
  - c
---
Its simply an array of pointers.
Its an array that holds several pointers.

For example, if you wanted to store the pointers of a few ints, then it may look like:
```c
int a,b,c;
a = 10; b = 20; c = 30;
int *ptr[3] - {&a, &b, &c};
```
# Array Of Pointers For Strings
If the string value is literally just a pointer to the char array, then its logical that and array of strings is equivalent to an array of pointers.
```c
char *name[] = {"Aby", "abe", "bongo"};
for (int i = 0; i < 3; i++) {
      printf("Value of names[%d] = %s\n", i, names[i] );
}
```