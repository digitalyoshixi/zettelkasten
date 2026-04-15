---
tags:
  - programming
  - c
aliases:
  - C fopen()
---
A C function used to open a file.
```c
FILE *fopen(const char* path, const char* mode);
```
- `mode` can be:
	- `"r"`: read
	- `"r+"`: read and write
	- `"w"`: write
	- `"w+"`: read and write, file created if doesn't exist
	- `"a"`: append
	- `"a+"`: read and append
# Example
```c
FILE *myfile = fopen("myfile.txt", "w");

if (myfile == NULL){
	fprintf(stderr, "Error opening file\n");
	return 1;
}
printf("file opened!\n");

if (fclose(myfile) != 0) {
	fprintf(stderr, "fclose failed!");
	return 1;
} 
return 0;
```