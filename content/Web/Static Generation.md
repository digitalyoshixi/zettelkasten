---
tags:
  - react
aliases:
  - Pre-rendering
---
Generates all HTML at build-time.
You can store these in storage buckets like [[AWS Simple Storage Service|AWS S3]]
# Issues
- Data may be less tailored to users
- Hard to scale to many pages
# NextJS
```js
export async function getStaticProps({ params }){
	const req = await fetch(`http://localhost:3000/${params.id}.json`);
	const data = await req.json();
	return {
		props : { car : data},
	}
}
```