---
tags:
  - verilog
  - programming
  - hardware
---
A [[Queue]].
`<datatype> <queue_name> [$];`
# Example
```verilog
bit q_1[$]; //unbounded queue of bit
int q_2[$:9]; // bounded queue of qsize 10
int q_3[$] = {5,6,7};

q1.push_back(10);
q1.pop_front();
$display("queue printed: %p", q);
```