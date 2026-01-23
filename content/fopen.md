---
tags:
  - programming
  - c
---
A C function used to open a file.
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