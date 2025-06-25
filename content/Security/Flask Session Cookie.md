---
tags:
  - web
---
A special cookie for sessions similar to a [[JSON Web Token|JWT Token]] but with different structure
# Brute Forcing or Decoding Flask Cookie
https://github.com/mprunet/flask_util (decoding)
### Decoding
```
python decode.py eyJhZG1pbiI6ZmFsc2UsImF1dGgiOmZhbHNlLCJ0b2tlbiI6InhKbVA5YUpKVUJma3BTQTdkOXlacExubFMwcVJkd2hyYmo2clhXOTVuSVNfSU9aUUxZYTFZV1NPSF9BQ0JwMS0wdXJvdmxEVFhhVkZ5YVhVNFhxS3hBIn0.aFwwtQ.tSwoZKSSVqSkr0Er3xwyJY76y60
```
### Brute Force
### Flask Unsign
https://pypi.org/project/flask-unsign/ (brute force)
1. Check which wordlists you have with 
   `ls /home/yoshixi/.pyenv/versions/3.12.4/lib/python3.12/site-packages/flask_unsign_wordlist/wordlists/rockyou.txt%`
2. Add a wordlist `cp /usr/share/wordlists/rockyou.txt ~/.pyenv/versions/3.12.4/lib/python3.12/site-packages/flask_unsign_wordlist/wordlists/rockyou.txt`
3. Unsign 
```
flask-unsign --no-literal-eval --wordlist /usr/share/wordlists/jwtsecrets.txt --unsign --cookie "eyJhZG1pbiI6ZmFsc2UsImF1dGgiOmZhbHNlLCJ0b2tlbiI6InhKbVA5YUpKVUJma3BTQTdkOXlacExubFMwcVJkd2hyYmo2clhXOTVuSVNfSU9aUUxZYTFZV1NPSF9BQ0JwMS0wdXJvdmxEVFhhVkZ5YVhVNFhxS3hBIn0.aFwwtQ.tSwoZKSSVqSkr0Er3xwyJY76y60"
```