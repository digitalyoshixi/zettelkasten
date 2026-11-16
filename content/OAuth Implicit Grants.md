---
tags:
  - web
  - security
---
A protocol for [[Open Auth|OAuth]] grants.
Once the user accepts OAuth permissions, the OAuth application immediately gives the access token to the application.
- No secure channel between the client application and OAuth service application
![[OAuth Implicit Grants-20261116002123796.webp]]
# Process
### 1. Authorization Request
Client application sends a authorization request to the OAuth service
```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=token&scope=openid%20profile&state=ae13d489bd00e3c24
HTTP/1.1 Host: oauth-authorization-server.com
```
### 2. User login and Consent
User logs into the application and consents
### 3. Access Token Grant
OAuth service causes user to redirect to `redirect_uri` along with access token as a [[Fragment Identifier|URL Fragment]]
```
GET /callback#access_token=z0y9x8w7v6u5&token_type=Bearer&expires_in=5000&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1
Host: client-app.com
```
### 4. API Call
User's browser calls the OAuth resource serve rAPI with the access token.
```
GET /userinfo HTTP/1.1 Host: oauth-resource-server.com Authorization: Bearer z0y9x8w7v6u5
```
### 5. Resource Grant
OAuth resource service returns the valid details
```
{ "username":"carlos", "email":"carlos@carlos-montoya.net" }
```
Frontend client uses this data. 