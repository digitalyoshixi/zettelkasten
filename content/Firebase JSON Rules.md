---
tags:
  - security
---
These are [[Firebase Rules]] written in [[JSON]]
# Boilerplate
```js
{
  "rules": {
    "files": {
      "$fileId": {
        ".read": "auth != null",
        ".write": "auth != null && (!data.exists() || data.child('uploadedBy').val() == auth.uid)"
      }
    }
    
  }
}
```
