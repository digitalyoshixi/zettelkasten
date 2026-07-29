---
tags:
  - verification
---
A usage of [[Data Mining]] to infer the formal specification of softwares.
- Take from API docs
- Take from comments
- Take from unit tests
https://homes.cs.washington.edu/~bodik/ucb/spec_mining/
# Process
1. Collect traces with a [[Tracer]], ensure you filter with [[Filtering Block]] 
2. Annotate with a [[Flow Dependence Annotator]]
3. Extract scenarios with a [[Scenario Extractor]]
4. Learn automata with [[Automata Learning]]
![[Specification Mining-20260729220352407.webp]]
# Tools
- [[Specification Mining Architecture with Trace fIltering and Clustering|SMArTIC]]