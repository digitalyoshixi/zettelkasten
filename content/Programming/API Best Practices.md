---
tags:
  - networking
  - software
---
# Best Practices
- Name API endpoints `/api/products`
- `GET` requests should be [[Idempotence|Idempotent]]
- APIs should be versioned to allow for backwards compatibility `/api/v1/...` and `/api/v2/...` For [[GraphQL]], `products` and `products_v2`
- Set [[Rate Limitting]]
- Set [[Cross Origin Resource Sharing|CORS]]