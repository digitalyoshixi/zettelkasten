---
tags:
  - cloud
---
A [[Function As A Service|Serverless]] architecture which allows you to have:
- Functions
- Events to dictate when functions should be called
![[AWS Lambda-20241125043956927.webp]]

# Lambda Testing
In `backend/function/<myapi>/event.json`, change the tests
![[AWS Lambda-20241129052315415.webp]]
Afterwards, run the command `amplify mock function <myapi>`