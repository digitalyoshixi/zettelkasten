---
tags:
  - programming
  - android
aliases:
  - MVP
---
A [[Architectural Design Pattern]] that results in code that is easier to test.
![[Model-View-Presenter-20250623214351071.webp|300]]
# Framework
Consists of:
1. Model (Data)
2. View (UI)
3. Presenter (Business Logic)
# Example : User Signup
1. View has two boxes for username and password
2. Presenter checks if user exists in the database
3. If not, then we write the username and password directly into the database

