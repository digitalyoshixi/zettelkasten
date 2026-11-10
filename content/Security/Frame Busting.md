---
tags:
  - security
  - web
---
A script that is used to prevent [[Clickjacking]]. Enforces all [[IFrame]] be:
- Current application is main window or top-most window
- Make all iframes visible
- Prevent clicking on low opacity iframes
- Intercept and flag potential clickjacking attacks.