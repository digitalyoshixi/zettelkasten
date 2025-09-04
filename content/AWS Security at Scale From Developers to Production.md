---
tags:
  - security
---
A talk by Luis pastor by [[Amazon Web Services|AWS]]
# Notes
- Clients want security posture to be more focused on innovation, older security practice was more about 'No', we move to a new mentality of innovation
- No client thinks they have the right-size team, Cyber teams are always very small
- Customers see the growing pains of expanding to cloud
- We have to implement a lot of automation for larger environments
- We require end-to-end security
- [[Shared Responsibility Model]]
- AWS believes security by design. Any new service must be secure
- Oftentimes we work with compliance frameworks across the globe
- Security by design from the silicon level
	- [[Pointer Authentication]]
	- [[Branch Target Identification]]
	- [[No Simultaneous Multithreading]]
- [[AWS Nitro]]
- AWS processes over 1 trillion requests a day
- Analyzes 1m domains a day
- [[Amazon GuardDuty]]
- 2.7 scans to probe open [[AWS Simple Storage Service|AWS S3]] buckets
- [[Access Control Model|ACL]] is still important 
- [[AWS Shield]]