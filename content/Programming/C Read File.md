---
tags:
  - programming
  - c
---
# Boilerplate
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    FILE *input_stream = fopen(filename, "rb");
    if (input_stream == NULL) {
        perror(filename);
    } 

    char plaintext[16] = {0};
    while (fread(plaintext, 16, 1, input_stream) != 0) {
        fwrite(shift_encrypt(plaintext, password), 16, 1, output_stream);
    }

    fclose(output_stream)
    // Character that store the read
    // character
    char ch;
    // Opening file in reading mode
    FILE *fptr = fopen("file.txt", "r");
    // Reading file character by character
    while ((ch = fgetc(fptr)) != EOF)
        printf("%c", ch);
    // Closing the file
    fclose(fptr);
    return 0;
}
```