---
tags:
  - programming
---
A principle in [[Data-Oriented Programming|DOP]].
*Seperate code from data in a way that the code resides in functions whose behavior does not depend on data encapsulated in the function's context*
# Example in [[Object Oriented Programming|OOP]]
Original:
```java
class Author {
  constructor(firstName, lastName, books) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.books = books;
  }
  fullName() {
    return this.firstName + " " + this.lastName;
  }
  isProlific() {
    return this.books > 100;
  }
}

var obj = new Author("Isaac", "Asimov", 500); // (1)
obj.fullName();
```
DOP revisions:
```java
class AuthorData {
  constructor(firstName, lastName, books) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.books = books;
  }
}

class NameCalculation {
  static fullName(data) {
    return data.firstName + " " + data.lastName;
  }
}

class AuthorRating {
  static isProlific (data) {
    return data.books > 100;
  }
}

var data = new AuthorData("Isaac", "Asimov", 500); 
NameCalculation.fullName(data);
```