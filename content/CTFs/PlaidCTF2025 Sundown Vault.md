---
tags:
  - web
  - ctf
---
# Info
![[PlaidCTF2025 Sundown Vault-20250404220002811.webp]]
https://plaidctf.com/files/sundown-vault.e484da5a3343211207e4ee933fa9284206678cdefbba57d4cbc7ff9a0f3b477b.tgz
# What the Docker File Creates
We find that there is a docker-file creating:

# Findings
- There is a update to postgres database's table with a specific ID holding the value of the flag.
![[PlaidCTF2025 Sundown Vault-20250404220130127.webp]]
- `db.js` is being used within `api.js`
![[PlaidCTF2025 Sundown Vault-20250404220341474.webp]]