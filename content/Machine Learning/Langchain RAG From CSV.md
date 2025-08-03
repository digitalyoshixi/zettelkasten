---
tags:
  - python
  - machine_learning
---

```python
import getpass
import os
from dotenv import load_dotenv
import google.generativeai as genai
# langchain libraries
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.schema.runnable import RunnableMap
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- loading env for api keys ---
load_dotenv()

# --- fetch the google gemini ---
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
#result = llm.invoke("hello who is this?")
#print(result.text)

#  ------ setup RAG -----

loader = CSVLoader(file_path="./genai/Food_Production.csv")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(data)
embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
vectorstore = DocArrayInMemorySearch.from_documents(
        docs,
        embedding=embeddings
)

# making the RAG
retriever = vectorstore.as_retriever()
#print(retriever.get_relevant_documents("Who is the current CEO of microsoft?"))
# --- Making chain ---
# setting up the format for output and the specific prompt engineering 
template ="""answer based off this context: {context}
in the json format:
{{"answer"}} : "..."
for this question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()
# creating chain
chain = RunnableMap({
    "context" : lambda x : retriever.get_relevant_documents(x["question"]),
    "question" : lambda x : x["question"]
    }) | prompt | llm | output_parser

print(chain.invoke({"question" : "what is the carbon footprint of eggs"}))
```