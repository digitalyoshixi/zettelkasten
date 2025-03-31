---
tags:
  - cloud
aliases:
  - AWS S3
---
Allows storage of any file-type and object.
Good for general purpose file storage
# .env setup
1. Create a [[AWS IAM]] user, and an access key. Ensure you write down the access key
2. In your .env file, write:
```
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
```
3. With a python file:
```python
from dotenv import load_dotenv
import os
load_dotenv()
import boto3
import hashlib 

s3 = boto3.resource('s3')
```
# Upload File
```python
...
s3 = boto3.resource('s3')
with open('slavetoambition.png', 'rb') as data:
	s3.Bucket('ownlytest').put_object(Key='slavetoambition.png', Body=data)
```
# Download File
