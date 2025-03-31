---
tags:
  - web
---
1. Create an [[AWS Elastic Compute Cloud|AWS EC2]] instance.
2. Setup EC2 security rules to be:
   ![[EC2 Flask deployment-20250118123113024.webp]]
3. 
```python
from flask import Flask

app = Flask(__name__) # designates this script as the root apth

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__": # if running this file directly
    app.run(host='0.0.0.0', port=8000) # run the app
```
as the app.py