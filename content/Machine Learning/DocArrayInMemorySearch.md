---
tags:
  - python
  - machine_learning
---
# Installation
```
pip install docarray
```
# Example
```python
import getpass
import os
from dotenv import load_dotenv
import google.generativeai as genai
# langchain libraries
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch

# -- loading env for api keys ---
load_dotenv()

# --- fetch the google gemini ---
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
#result = llm.invoke("hello who is this?")
#print(result.text)

#  ------ setup RAG -----

embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
vectorstore = DocArrayInMemorySearch.from_texts(
        ["The answer to life, universe and everything is 43"],
        embedding=embeddings
)

# making the RAG
retriever = vectorstore.as_retriever()
print(retriever.get_relevant_documents("What is the answer to life universe and everything?"))
```