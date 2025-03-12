---
tags:
  - reverse_engineering
---
Binary analysis suite that includes tools for:
- [[Symbolic Execution]]
- CFG generation
- ROP gadget finder
# angr
angr is a python library that automates this process of finding input constraints.
The default searching algorithm it uses is the [[Breadth First Search Algorithm]]
# Installation
the blackarch version does not work.
It is best to make a [[Python Virtual Environment]] where you `pip install angr` automatically
### Example Venv
```
python -m venv angrproj
cd angrproj && source /bin/activate
pip install angr monkeyhex setuptools wheel pip ipython
```
# angr Process
![[angr-20240719013906505.webp]]
1. [[CLE]] loads the binary
2. [[archinfo]] provides information to SimEngine and SimOS about the architecture the binary is running on
3. [[pyvex]] turns assembly instructions into [[VEX IR]] 
4. SimEngine created to emulate the execution of [[VEX IR]] instructions
5. SimOS created to emulate the execution environment - whether its [[IT/Windows]] or [[Linux]]
6. [[claripy]] turns [[VEX IR]] into [[Bitvector|Bitvectors]]
7. [[z3]] uses the [[Bitvector|Bitvectors]] to solve for constraints with its [[Satisfiability Modulo Theories Solver|SMT Solver]]
# Angr Script Anatomy
1. Loading binary
2. Translating binary into [[Intermediate Representation|IR]]
3. Performing the analysis:
	- Partial or full program analysis 
		- [[Dependency Analysis]]
		- [[Program Slicing]]
	- [[Symbolic Execution]]
### Boilerplate Script
```python
import angr
import claripy

proj = angr.Project("./binaryName") # load binary into an angr project

state = proj.factory.entry_state() # create a generic SimState

simgr = proj.factory.simulation_manager(state) # set the intial state of the simulation to state
simgr.explore(find = lambda newState: b"String in correct output" in newState.posix.dumps(1)) # search for the constraints that result in a string in the correct output

simgr.found[0] # will give us the state

print(simgr.found[0].posix.dumps(0)) # stdin that gives us the correct stdout
```
# Concepts 
- [[angr Project]]
- [[angr Loaded Object]]
- [[angr Object]]
- [[angr Factory]]
	- [[angr Block]]
	- [[angr SimState]]
	- [[angr Registers]]
	- [[angr Memory Space]]
- [[angr Symbol]]
- [[angr Simulation Manager]]
	- [[angr Simulation Manager Explore Routes]]
- [[angr Manual Constraints]]
- [[angr Symbolic Variable]]
- [[angr Analysis Tools]]
