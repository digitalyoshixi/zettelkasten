---
tags:
  - web
  - security
---
An attack against OpenID providers that accept a URL for the scope data rather than directly reading it from the request.
Often this URL's page includes data like:
```
{
	client_id : ...,
	redirect_uri : ...,
	response_type : token,
	scope : openid_profile,
	state : ...
}
```
This is passed to the OAuth application that will read from the URI
```
GET /authorization?request_uri=https://mysite/my_oauthscope.json
```
- The OpenID provider will visit request_uri to get the list of scopes
This can be abused for [[Server Side Request Forgery|SSRF]]
```
GET /authorization?request_uri=https://localhost
```
# Fingerprinting
- See if `request_uri_parameter_supported` exists in the config file or documentation