---
tags:
  - reverse_engineering
---
Primary interface in angr for performing execution.
```python
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)
```
# Attributes
These are statuses of states that we can monitor concurrently
### simgr.active
A simulation stash corresponding to the active status.
This is the default status that we should be on after simgr initialization.
![[angr Simulation Manager-20240714181925437.webp]]
The value of this would be the current address our eip is on. 
At intialization, this should be the same value as the entry point.
[proof](https://rentry.org/branr7oz)
### simgr.found
Returns an array of all found inputs that match the criteria in `simgr.explore()`.
- `simgr.found[0].posix.dumps(1)` returns the first input we need to get to the criteria
- `simgr.found[0].posix.dumps(0)` returns the stdout reply for the first input that we would get
# Methods
### simgr.step()
Stepping forwards one [[Basic Block]]'s worth of execution.
The:
- active stash changes value
- registers change values (hopefully)
### simgr.explore()
Using constaint finders to search for a specific criteria that could be:"
- Reaching a certain address
- Matching a certain string in output
[[angr Simulation Manager Explore Routes]]