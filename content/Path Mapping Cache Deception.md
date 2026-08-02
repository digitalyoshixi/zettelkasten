---
tags:
  - web
  - security
---
A [[Web Cache Deception]] technique that involves discrepancies between the origin and cache server for [[Path Mapping]] API types.
# Example
```
http://example.com/user/123/profile/wcd.css
```
- [[Rest API]] Origin server only cares about `/user/123/profile`, ignores `wcd.css` as it is a non-significant parameters
- URL mapping cache server interprets `wcd.css` as a static item, caches this page as if it were a CSS file
# Testing
1. Check if adding an arbitrary parameter to the end still returns the same sensitive content
2. Add `.css`, `.js`, `.ico`, `.exe` (Fuzz this to see if any caches)