---
tags:
  - cloud
---
Provides [[Software Development Kit|SDK]]s that can connect from different frameworks.
It also has [[Firebase]]
https://www.youtube.com/watch?v=T4MQrRDo20w
# Installation
1. [[AWS IAM User Creation]]
2. `npm i @aws-amplify/cli`
3. `amplify configure`
	1. us-east-1
	2. Create a new user profile
	3. Create a new access key
4. `amplify init`
	1. Gen 1
	2. `default` profile
5. There should now an amplify folder in your project
6. `amplify add API` > `REST`
   ![[AWS Amplify-20241129045613462.webp|712]]
After you make changes to your file, make sure you `amplify push` so the cloud is updated.

### Amplify + React
1. `npm install react@^18.0 react-dom@^18.0`
2. `npm i aws-amplify`
3. in your main page.tsx, add:
   ![[AWS Amplify-20241129053043830.webp]]
# Post-Installation Files
### `amplify/backend/function/amplify/src/index.js`
This is your lambda function you created
![[AWS Amplify-20241129045811957.webp]]
### `amplify/backend/function/amplify/src/event.json`
These are code tests for your lambda function
![[AWS Amplify-20241129045918172.webp]]
