---
tags:
  - javascript
  - react
---
`app/profile/[name]/page.js`
The `[name]` signifies a wildcard, that can be filled in by another request.
# Wildcard Routes
![[NextJS Dynamic Route-20241128030606265.webp|408]]
Theses are directories
`[anything]/`
Translates to:
`example.com/{anything}`
### Grabbing Route ID
If you named the route folder as `[id]/`
```ts
export default function GetID({ params }){
	return (
	<div> {params.id} </div>
	)
}
```
# Ignored Routes
`(group)/`
It will be ignored by the url routing. Good if you want to put a file and not have it affect the URL structure.