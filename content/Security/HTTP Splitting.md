---
tags:
  - security
  - web
---
An attack against the parsing of a [[Rest API|HTTP Request]] that allows smuggling of a seperate malicious request.
Often occurs when you can input `\r\n` [[Carriage Return Line Feed]] to create new lines through user input.