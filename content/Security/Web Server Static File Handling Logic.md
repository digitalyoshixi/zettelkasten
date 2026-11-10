---
tags:
  - web
  - security
---
# Logic
- If file type is non-executable, server sends file content directly to client
- If filetype is executable, server assigns variables based on headers in the HTTP request
- If file is executable, but server is not configured to execute files of this type, it will respond with an error