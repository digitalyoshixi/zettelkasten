---
tags:
  - machine_learning
  - programming
---
Used to convert documents into smaller chunks.
```python
data = "something"
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(data)
```