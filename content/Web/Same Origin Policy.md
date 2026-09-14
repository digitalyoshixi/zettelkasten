---
tags:
  - web
  - security
aliases:
  - SOP
---
A policy part of the [[Browser Origin Policy]] that prevents webpages from reading/writing the contents of other webpages in a browser.
- If a website has no [[Cross-Origin-Policy]], then [[Standard Operating Procedures|SOP]] is default.
- All sites can send requests, but SOP prevents responses
![[Same Origin Policy-20250208012937735.webp]]
It checks that the:
- Protocol
- Host
- Port
Are the same between two origins.
# Same Origin vs Same Site
![[Same Origin Policy-20260903005412269.webp]]