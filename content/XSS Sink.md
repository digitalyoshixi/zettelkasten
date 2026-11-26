---
tags:
  - web
  - security
---
# List
- https://github.com/Sivnerof/Sources-And-Sinks-Cheatsheet
# eval Sink
```javascript
eval(alert(1))
```
# innerHTML Sink
```javascript
document.getElementById('tt').innerHTML = `<img onerror='alert(1)' src='x'/>`;
```
# script.src Sink
```js
script.src = data:text/javascript,alert(1)
```
# child_process.execSync()
Acts similar to `eval()`
```

```


```html
<svg><animate onbegin=alert(1) attributeName=x dur=1s>
```