---
tags:
  - programming
aliases:
  - PDF
---
A file-format for documents that can be viewed on a web-browser.
# Structure
### Header
Specifies the version number of a pdf
```
%PDF-2.0
```
### Body
Comprised of objects:
- Comments - `%comment` ends at `\n`
- Booleans
- Real Numbers
- Integers
- Names – `/name` 
- Strings – `(text)` 
- Arrays – `([...])`
- Dictionaries – `(<<...>>)`. The key is a name object and the value can be any other object. 
- Streams – contains data, images or code. Often compressed. Represented by a dictionary that set the stream’s length with the key `/Length` and encoding `/Filters`. starts with `stream` ends with `endstream`
- Indirect object – object that has a unique ID, the object starts with the keyboard `obj` and ends with `endobj` other objects can reference the object using its ID. For example a reference to object with ID 3 we would look like this: `3 0 R`
- Null objects
### Footer
##### Index Table
- Contains byte offset from start of file for each indirect object 