---
tags:
  - cloud
---
Creating templates for your infrastructure in [[YAML]] or [[JSON]]
![[AWS Cloud Formation-20241125050821432.webp]]
# Stacks
Collection of AWS resources managed by a single AWS unit.
They allow you to version-control your infrastructure making it easier to replicate AWS resource configurations.
### Nested Stacks
Smaller functionalities that can be configured. These include:
- APIs
- Authentication
![[AWS Cloud Formation-20241129051137475.webp]]
You can see in my stacks, I have an API and a amplify project