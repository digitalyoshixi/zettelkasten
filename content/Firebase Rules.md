---
tags:
  - security
aliases:
  - CEL
---
The rules regarding how firebase will authorize access to database resources
# Types


The declarative language for writing firebase rules that manage database authorization.
Involves assigning permissions for each database route
# Boilerplate
```c
service cloud.firestore{
	match /databases/{database}/documents {
		match /users/{myuser} {
			allow read
			allow write: if request.auth.uid == "daniel"
		}
	}
}
```
# Syntax
- `{variable}` allows arbitrary data in the route, referenced by variable name