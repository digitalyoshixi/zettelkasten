---
tags:
  - python
  - web
---
A backend/frontend [[Web Framework]] for python webapps.
It is considered a micro-framework because it is very minimalistic. You can build an entire project in one file.
# Installation
```
pip install flask flask-sqlalchemy
```
# Boilerplate Code
```python
from flask import Flask 

app = Flask(__name__) # designates this script as the root apth

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__": # if running this file directly
    app.run(debug=True, port=3000) # run the app
    #app.run(host="0.0.0.0", debug=True, port=3000) # expose to all ips
```
# Concepts
- [[Jinja Template]]
- [[Flask Route]]
- [[Flask URL Parameters]]
- [[Flask Response]]
- [[Flask Secret Key]]
- [[Flask Run]]
- [[Flask CORS]]
- [[Flask Session Cookie]]
# Web Dev Concepts
- [[Application Endpoints]]
- [[Curl]]
- [[Web/Session]]
- [[Cookies]]