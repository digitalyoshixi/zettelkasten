---
tags:
  - os
  - synchronization
---

Software solution to the critical section problem. It is restricted to only 2 processes. 2 data items to be shared: a turn integer to dictate whose turn it is to enter the critical section and flag boolean to say, I am ready to enter the critical section.

The cool thing about this algorithm is that it is generous. When a process is ready, it will NOT enter the critical section first, instead, it will open the door for the other process to enter.

This generosity allows the process to enter the critical section, only if another opens the door for it first

Example: Process A, Process B

Process can only enter critical state if flag is True and turn is theirs

|Event|Process A flag|Process B flag|Turn|
|-|-|-|-|
|Initialization|False|False|nil|
|Process A is ready|True|False|B|
|Process B is ready|True|True|A|
|Process A executes|yay|yay|Yay|


