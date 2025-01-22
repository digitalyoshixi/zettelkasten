---
tags:
  - programming
aliases:
  - .env
---
These are `.env` files located in the current folder.
# Python get .env
```python
import os
from dotenv import load_dotenv
load_dotenv()
MY_ENV_VAR = os.getenv('MY_ENV_VAR')
print(MY_ENV_VAR)
```