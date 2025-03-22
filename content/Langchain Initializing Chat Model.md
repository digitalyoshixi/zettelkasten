---
tags:
  - python
---
```python
import getpass
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
result = llm.invoke("hello who is this?")
print(result)
```