---
tags:
  - security
  - web
---
An attack that involves using the alias feature to send multiple requests to be processed in a [[GraphQL Query]]
```
{
  user1: user(id: "123") { name }
  user2: user(id: "123") { name }
  user3: user(id: "123") { name }
  // ...repeated hundreds of times
}
```