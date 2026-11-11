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
# GraphQL Endpoints
- `/graphql`
- `/api`
- `/api/graphql`
- `/graphql/api`
- `/graphql/graphql`
- `/graphql/v1`
- `/api/v1`
- `/api/v1/graphql`
- `/graphql/api/v1`
- `/graphql/graphql/v1`
# Concepts
- [[GraphQL Query]]
- [[GraphQL Mutation]]
- [[GraphQL Subscription]]
- [[GraphQL Schema]]
- [[GraphQL Resolvers]]
- [[GraphQL Voyager]]
- [[GraphQL Threat Matrix]]
- [[GraphQL Introspection]]
- [[GraphQL Universal Query]]
- [[GraphQL Suggestions]]
# Tools
- [[Altair]]
- [[Clairvoyance]]
# Security
### Vulnerabiities
- [[GraphQL Circular Queries]]
- [[GraphQL Circular Fragments]]
- [[GraphQL Field Duplication]]
- [[GraphQL Alias Overloading]]
- [[GraphQL Directive Overloading]]
- [[GraphQL Array-Based Query Batching]]
- [[GraphQL Object-Limit Overriding in API Pagination]]
- [[GraphQL Field Stuffing]]
### Tools
- [[GraphQL Threat Matrix]]
- [[GraphQL Voyager]]
