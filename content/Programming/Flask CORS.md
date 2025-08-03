---
tags:
  - python
  - web
---
# Installation
```
pip install flask-cors
```
# Boilerplate
```python
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return "hello world"

```
