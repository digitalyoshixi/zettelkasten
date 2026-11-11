---
tags:
  - web
---
These are structures for specific [[GraphQL]] queries.
- Used for reading
![[GraphQL Query-20250912010745604.webp]]
# Get All Products
```
query {
    products {
        id
        name
        listed
    }
}
```
# Get Specific Product that Matches Condition
```
query {
    product(id: 3) {
        id
        name
        listed
    }
}
```