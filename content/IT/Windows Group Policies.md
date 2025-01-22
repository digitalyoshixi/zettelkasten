---
tags:
  - windows
---
Windows feature that sets up account permissions.
![[Windows Group Policies-20240705012957086.webp]]
You can:
- Limit the time users in a specific group can log on (Login time restrictions)
- Limit applications users can install
- Require users to make complex passwords
- Prevent remote logins
- Configure user's operating system
- Configure user applications
You can use [[Windows Group Policy Editor]] or [[Windows Local Security Policy]].
# Policy Hierarchy
1. [[Windows Active Directory]] with [[Windows Group Policy Editor|gpedit.msc]]
2. [[Windows Local Security Policy]]
Active directory policies will supersede local security policy, so if a local security policy allows write access, but active directory forbids writing, then the user will not be able to write.
Group policies will only be updated after login. You can manually update them with [[Windows gpupdate]]