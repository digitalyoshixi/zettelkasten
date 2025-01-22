---
tags:
  - cloud
aliases:
  - AWS EC2
---
Creating [[Server]] on the cloud.
- [[Web Server]]
# Connecting to EC2 Server
1. Create a [[RSA]] key on aws console
2. Create a EC2 server on aws console
3. `chmod 600 key.pem`
4. `ssh -i ./key.pem ec2-user@54.234.22.87`
# Concepts
- [[EC2 Flask deployment]]