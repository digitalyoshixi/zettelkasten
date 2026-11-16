---
tags:
  - web
  - security
---
A negotiation protocol for client sites to request data from oauth services.
1. Client site has the oauth button
2. User accepts
3. OAuth provides the client site a single-use authorization code
4. Client site uses the authorization code to receive a short lived access token
![[OAuth Authorization Code-20261116000122999.webp]]
# Steps
### 1. Authorization Request
Client sends a request to OAuth service's `/authorization` endpoint
```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=code&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1 Host: oauth-authorization-server.com
```
- `client_id`: ID of the client application
- `redirect_uri`: Callback uri that the user should visit once the client clicks accept
- `response_type`: Response the client application is expecting (i.e Grant type)
- `scope`: Subset of what user data is required ([[OAuth Scope]])
- `state`: A unique value tied to the current session o the client application. OAuth service should return this exact value in the response
### 2. User Approval
User must approve all that is requested in the [[OAuth Scope]]
### 3. Authorization Code Grant
User's browser is redirected to the `redirect_uri` in the original request. The request will contain the authorization code as a query parameter. Sometimes the `state` may also be sent.
```
GET /callback?code=a1b2c3d4e5f6g7h8&state=ae13d489bd00e3c24 HTTP/1.1 Host: client-app.com
```
### 4. Access Token Request
Client application uses the authorization code to get a access token.
```
POST /token HTTP/1.1
Host: oauth-authorization-server.com
…
client_id=12345&client_secret=SECRET&redirect_uri=https://client-app.com/callback&grant_type=authorization_code&code=a1b2c3d4e5f6g7h8
```
- `client_secret` is the client's secret that was registered when the client setup oauth access
- `grant_type` is the grant type the application wants to use
### 5. Access Token Grant
OAuth service valicates client secret and authorization code to return the access token
```
{ "access_token": "z0y9x8w7v6u5", "token_type": "Bearer", "expires_in": 3600, "scope": "openid profile", … }
```

### 6. API Call
Client application can call APIs with this access token
```
GET /userinfo HTTP/1.1
Host: oauth-resource-server.com
Authorization: Bearer z0y9x8w7v6u5
```
### 7. Resource Grant
OAuth resource service returns the responding resources
```
{ "username":"carlos", "email":"carlos@carlos-montoya.net", … }
```