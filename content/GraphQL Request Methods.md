---
tags:
  - web
  - security
---
Common methods to request data on a [[GraphQL]] endpoint.
- All POST requests should have content-type of `application/json`
- GET requests may accept `x-www-form-urlencoded`
# Example Post Query
```
{"query":"\n    query getBlogPost($id: Int!) {\n        getBlogPost(id: $id) {\n            image\n            title\n            author\n            date\n            paragraphs\n        postPassword\n        }\n    }","operationName":"getBlogPost","variables":{"id":03}}
```
# Example Post Mutation
```
{"query":"\n    mutation login($input: LoginInput!) {\n        login(input: $input) {\n            token\n            success\n        }\n    }","operationName":"login","variables":{"input":{"username":"aa","password":"aa"}}}
```
# Example GET Mutation
```
GET /api?query=mutation+deleteOrganizationUser($input:+DeleteOrganizationUserInput!){deleteOrganizationUser(input:$input){user{id}}}&variables={"input":{"id":3}} HTTP/2
```