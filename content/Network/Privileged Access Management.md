---
tags:
  - security
aliases:
  - PAM
---
The protocol to allow for temporary administrative priviledges.
Administrators create ephemeral roles with just enough priviledges for a user to do their job.
# Process
![[Privileged Access Management-20250809214949889.webp]]
1. A user goes through [[Identity Manager|IM]] to request a ticket for PAM
2. Administrator creates ephemeral role in the Bastion Forest
3. Administrator gives credentials over PAM TRUST
4. User recieves ticket
5. Administrator closes PAM session
# PAM Tools
- [[Just In Time Permissions]]