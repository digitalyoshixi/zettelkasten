---
tags:
  - security
  - web
---
A way to circumvent [[Frame Busting]] by making IFrames have the attributes:
- `sandbox`
- `allow-forms`
- `allow-scripts`
- `allow-top-navigation` 

```
<iframe id="victim_website" src="https://victim-website.com" sandbox="allow-forms"></iframe>
```