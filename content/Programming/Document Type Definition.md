---
tags:
  - programming
aliases:
  - DTD
---
A specification file that contains markup declarations defining a document type.
- Defines valid building blocks of [[eXtensive Markup Language|XML]] document
Based off [[Context Free Grammar|CFG]].
```xml
<!DOCTYPE element DTD identifier [
declararion 1
declararion 2
...
declaration n
] >
```
# Example
```xml
<!DOCTYPE library [  
  <!ELEMENT library (book+)>  
  <!ELEMENT book (title, author, genre)>  
  <!ELEMENT title (#PCDATA)>  
  <!ELEMENT author (#PCDATA)>  
  <!ELEMENT genre (#PCDATA)>  
]>
```