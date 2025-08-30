---
tags:
  - programming
---
```python
SCOPES = ["https://mail.google.com/"]

def main():
  flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json", SCOPES
  )
  creds = flow.run_local_server(port=0)
  # Save the credentials for the next run
  with open("token.json", "w") as token:
    token.write(creds.to_json())

if __name__ == "__main__":
  main()
```