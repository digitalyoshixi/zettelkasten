---
tags:
  - c
---
used incredibly similar to [[printf()]].
`scanf("format",pointer)`
# Scan one
```c
int bober;
scanf("%d", &bober); // gives it a value from stdin
printf("%d", &bober); // outputs in stdout
```
### Scan Multiple
```c
int a;
int b;
scanf("%d%d",&a,&b);
```
# scanf() a string including whitespace
```c
char ss[MAX_LEN];
scanf("\n");
scanf("%[^\n]%*c", ss);
```
# scanf() and avoid multiple inputs
```c
scanf(" %c", s);
```