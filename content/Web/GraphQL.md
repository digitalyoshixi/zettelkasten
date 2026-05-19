---
tags:
  - database
---
A [[Application Program Interface|API]] that provides hyper-specificity on the data needed. 
![[GraphQL-20240802040352920.webp|255]]
Multiple [[Rest API]] requests can be packed into a single GraphQL request.
- Avoids overfetching/underfetching
- Strongly typed schema based queries
- High levels of privacy for requests sent
- Only POST requests
- Queries can impact server performance
- Always responds with HTTP 200
	- Errors are included in payload
# Installation ([[ExpressJS]])
```
npm i express express-graphql graphql
```
# Concepts
- [[GraphQL Query]]
- [[GraphQL Mutation]]
- [[GraphQL Subscription]]
- [[GraphQL Schema]]
- [[GraphQL Resolvers]]
- [[GraphQL Voyager]]
- [[GraphQL Threat Matrix]]
- [[GraphQL Introspection]]
# Tools
- [[Altair]]