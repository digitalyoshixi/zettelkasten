---
tags:
  - security
  - web
---
A vulnerability against [[Javascript Prototype]] that allows you to add arbitrary properties to `Object` to be automatically be inherited by children [[JSON]]. 
If a child uses this property somewhere dangerously, it can execute any code.

```javascript
`{ existingProperty1: 'foo', existingProperty2: 'bar', __proto__: { evilProperty: 'payload' } }`
```
# Requirement
- Source to insert new fields (URL, Json input, Web messages)
- Sink to abuse new properties (document.write, innerHTML, eval, outerHTML)
- Gadget that allows unsage usage
# Tools
- [[DOM Invader]]
# Testing for Sources
### Blind Test
- For the source set prototype as key (e.g `mysite.com/?__proto__[foo]=bar` as variable value)
- Check  `Object.prototype` in the browser console
- Try `?__proto__.foo=bar` if it didn't work
- Repeat for each potential source
### Javascript Intercept Method
1. Intercept the javascript coming in with burp
2. Add a `debugger` statement at the start of the script
3. Once script is paused, go to console and add following command:
```
Object.defineProperty(Object.prototype, 'YOUR-PROPERTY', {
    get() {
        console.trace();
        return 'polluted';
    }
})
```
or for a function:
```
Object.prototype.YOUR-FUNCTION = function(){
    
}
```
4. If the polluted object is used, the browser will log a stack trace to the console whenever it is accessed
# Attacking
1. Find the sync that you can use to overwrite `Object` or any other high level prototype
2. Find the field that you want to overwrite. Whether it is a function or a attribute. This field must be used by a [[XSS Sink]]
# Concepts
- [[Prototype Pollution via URL]]
- [[Prototype Pollution via JSON]]
- [[Prototype Pollution via Constructor]]
- [[Prototype Pollution via Flawed Sanitiziation]]
- [[XSS Sink]]