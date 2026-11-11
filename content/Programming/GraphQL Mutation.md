---
tags:
  - programming
  - web
---
A graphql request for modifying/updating data.
```
{"query":"
    mutation login($input: LoginInput!) {
        login(input: {
          "username":"aa",
          "password":"aa"
          }) {
            token
            success
        }
    }"
}
```