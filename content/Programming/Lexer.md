---
tags:
  - c
  - cpp
  - llvm
aliases: []
---
A scanner to break up a code input into [[LLVM Tokens]] though [[Lexical Analysis]]
When you make the lexer, you want to define all:
- Enum for [[Keywords|Reserved Keywords]] (like `def`, `if`, `func`, etc...)
- Enum for [[Identifiers]] (for variables, functions, classnames, etc)
- Enum for [[Literals]] (for numbers, for chars, etc..)
- Enum for [[Whitespace]] (like ` `, `\n`, etc..)
- A variable to store identifier token's name
- A variable to store a literal's value
- A function to grab the next token
```cpp
// The lexer returns tokens [0-255] if it is an unknown character, otherwise one
// of these for known things.
enum Token {
  tok_eof = -1,

  // commands
  tok_def = -2,
  tok_extern = -3,

  // primary
  tok_identifier = -4,
  tok_number = -5,
};

static std::string IdentifierStr; // Filled in if tok_identifier
static double NumVal;             // Filled in if tok_number

// gettok - Return the next token from standard input.
static int gettok() {
  static int LastChar = ' ';
  
  // Skip any whitespace, until you reach the first non-whitespace token
  while (isspace(LastChar))
    LastChar = getchar();

  if (isalpha(LastChar)) { // identifier: [a-zA-Z][a-zA-Z0-9]* 
    // grabbing the entire token string
    IdentifierStr = LastChar;
    while (isalnum((LastChar = getchar())))
      IdentifierStr += LastChar;

    // recognizing token 
    if (IdentifierStr == "def")
      return tok_def;
    if (IdentifierStr == "extern")
      return tok_extern;

    return tok_identifier;
  }
  
  // if we are given a numerical character
  if (isdigit(LastChar) || LastChar == '.') {   // Number: [0-9.]+
    // create a string to hold the number with its decimal places
    std::string NumStr;
    do {
      NumStr += LastChar;
      LastChar = getchar();
    } while (isdigit(LastChar) || LastChar == '.');
  
    NumVal = strtod(NumStr.c_str(), 0);
    return tok_number;
  }
  // If we are given a comment
  if (LastChar == '#') {
  // Comment until end of line.
  do
    LastChar = getchar();
  while (LastChar != EOF && LastChar != '\n' && LastChar != '\r');

  if (LastChar != EOF)
    return gettok();
  }

  // Check for end of file.  Don't eat the EOF.
  if (LastChar == EOF)
    return tok_eof;

  // Otherwise, just return the character as its ascii value.
  int ThisChar = LastChar;
  LastChar = getchar();
  return ThisChar;

}

```
If any token is not defined, the lexer shall return as its ascii code instead.
