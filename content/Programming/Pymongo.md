---
tags:
  - python
  - database
---
A library to initialize [[MongoDB]] connections
# Installation
```
pip install pymongo
```
# Boilerplate
Ensure that on [[MongoDB Atlas]], you allow your current IP in the whitelist.
```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import certifi
import os
from Medicine import Medicine

ca = certifi.where()
load_dotenv()
ATLAS_URI = os.getenv('ATLAS_URI')
client = MongoClient(ATLAS_URI, server_api=ServerApi('1'), tlsCAFile=ca)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    medicine = Medicine(
        medicationID="ibuprofen",
        dosage="400mg", 
        prescribedDate="2024-01-16"
    )

    client["HealthApp"]["Medications"].insert_one(medicine.model_dump())

except Exception as e:
    print(e)
```