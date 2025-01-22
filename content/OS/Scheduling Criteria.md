---
tags:
  - os
  - scheduling
---
## Scheduling criteria:

### CPU utilization

To keep the CPU as busy as possible, we want it to use between 40% to 90%

### Throughput

The measure of work being done by the processor. # of processes completed/time

### Turnaround time

How long it takes to execute that process. From submission to completion. We find this from the sum of periods spent waiting in the memory, waiting in ready, executing on CPU and doing I/O

### Waiting time

Sum of periods spend waiting in the ready queue

### Response time

Time it takes to start responding. Different than turnaround time in the fact that it does not include the time it takes to output the response.