---
tags:
  - python
  - webcrawler
---
A [[Webcrawler]] library for [[Python]].
# Parsing A URL
```python
from bs4 import BeautifulSoup
import requests

html = requests.get("https://arstechnica.com/gadgets") # returns a reponse object
soup = BeautifulSoup(html.text, 'html')
```
### Prettifying
Returns a prettier version of the html 
```python
soup.prettify() #makes the output look nicer
```
### Finding Tags
```python
atags = soup.findAll('a', class_="relative block aspect-square h-auto")
```