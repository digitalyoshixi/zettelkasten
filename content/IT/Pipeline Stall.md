---
tags:
  - hardware
  - computer_organization
---
An issue in [[Central Processing Unit|CPU Pipelining]] that occurs when it takes multiple clock cycles to complete a task. 
![[Pipeline Stall-20240519211033351.webp]]
This will create a bottleneck, where prior and subsequent tasks must wait for the current task to finish. 
The subsequent tasks will perform 'bubble tasks' in which they do NOTHING
# Solutions
CPUs offer multiple pipelines so that if one pipeline is stalled, the operation goes to another pipeline.
I know, its not an eloquent solution, but its what we got.