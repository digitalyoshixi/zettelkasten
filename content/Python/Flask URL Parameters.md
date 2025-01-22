---
tags:
  - python
  - web
---
```python
from flask import Flask, request
app = Flask(__name__)

print(request.args) # print request arguments
usersname = request.args.get('username') # get a specific argument value
# usersname = request.args['username'] # also the same
```
# Sending URL Parameters
`127.0.0.1:5000/?name=Mike&greeting=Hello`
![[Flask URL Parameters-20241004031422878.webp]]