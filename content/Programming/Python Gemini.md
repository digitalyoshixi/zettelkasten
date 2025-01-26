---
tags:
  - python
  - machine_learning
---
# Installation
```python
pip install -U google-generativeai
```
2. Get a gemini API key https://aistudio.google.com/app/apikey
3. [[Python dotenv]]
# Utilization
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("The opposite of hot is")
print(response.text)
```