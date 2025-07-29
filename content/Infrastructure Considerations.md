---
tags:
  - IT
---
# Considerations
### Availability
Consider if you need a specific [[Datacenter]], [[Cloud Computing]] or [[High Availability]]
### Resilience
Measured by amount of time it takes to recover from critical failure.
Consider a [[Load Balancer]] or storing backup data in different regions
### Cost
Consider the cost of each purchase. Look at the [[Service Level Agreement|SLA]]
### Responsiveness
Ensure user experience is fast.
Consider a [[Load Balancer]] with auto-scaling
### Scalability
The rate at which you can scale your app
### Ease of Deployment
The documented writing and ease to deploy things
### Risk Transference
Setting up a [[Service Level Agreement|SLA]] to negotiate risk transferrence.
Example could be a SLA guaranteeing that in case a SQL database crashes, the service provider will fix it within 2 hours.
### Ease of Recovery
Finding how easy it is to recover data incase one data center goes offline
### Patch Availability
Find that your [[Cloud Service Provider|CSP]] will maintain the most recent copies of patches.
[[Microsoft Intune]] is an endpoint that offers patch management of windows devices