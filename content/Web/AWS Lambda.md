---
tags:
  - cloud
---
A [[Function As A Service|Serverless]] architecture which allows you to have:
- Functions
- Events to dictate when functions should be called
![[AWS Lambda-20241125043956927.webp]]
# Boilerplate Function
```js
export const handler = async (event) => {
	// TODO implement
	const response = {
		statusCode: 200,
		body: JSON.stringify('Hello from Lambda!'),
	};
	return response;
};
```
# Guides
- [[AWS Lambda Serverless Function Creation]]
- [[AWS Lambda Testing]]
# Resources
- https://invidious.yoshixi.net/watch?v=4AgWKVBOjVc&listen=false