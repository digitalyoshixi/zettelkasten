---
tags:
  - web
  - security
---
These are vulnerabilities in the logic of an application.
- Limits of an action
- Validation of an action
- Order of steps in action
- Application specific rules
# Testing Process
1. Find the application flows & series of requests sent
2. Define the rules (limits, validation, order, app specific)
### Example
Sign up:
- Limit: cant register twice
- Validation: email must be verified
- Workflow: after sign up, user complete questionaire
- Application: employees cannot sign up