---
tags:
  - programming
  - c
---
```
int fscanf(FILE *stream, const char *format, ...)
```
[[scanf()]], but we can read from any [[File Descriptor]]

```c
FILE *inp_file = fopen("myfile.txt", "r");
int error, total;
while (fscanf(inp_file, "%80s %d", name, &total) == 2){
	printf("Name: %s. Score: %d.\n", name, total);
}
```