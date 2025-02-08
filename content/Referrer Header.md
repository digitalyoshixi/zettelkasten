---
tags:
  - web
  - security
---
A solution to [[Cross Site Request Forgery]] that includes the requests source address as a header to the message for the site to verify.

This however. does not work well because if a user has an adblocker or privacy tooling, this request source will be different.