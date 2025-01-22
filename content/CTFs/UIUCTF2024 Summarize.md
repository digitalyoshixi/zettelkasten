---
tags:
  - ctf
  - reverse_engineering
---
# Challenge Details
![[UIUCTF2024 Summarize-20240701012248749.webp]]
https://uiuctf-2024-rctf-challenge-uploads.storage.googleapis.com/uploads/66e8392f3eaaf0ee279369f4bbdb61ca7ede335f802339359e67daaa171b4340/summarize
### Running The Binary
![[UIUCTF2024 Summarize-20240701013210169.webp|596]]
# Solution
https://hst.sh/ijodafimak.py
```python
import sys

import angr
import claripy
import logging

import time


def visualize(*args, **kwargs):
    stashes = args[0].stashes
    for simstate in stashes["active"]:
        state_a = format(simstate.solver.eval(a), 'd')
        state_b = format(simstate.solver.eval(b), 'd')
        state_c = format(simstate.solver.eval(c), 'd')
        state_d = format(simstate.solver.eval(d), 'd')
        state_e = format(simstate.solver.eval(e), 'd')
        state_f = format(simstate.solver.eval(f), 'd')

        state_sol = f"[!] solving: {state_a}, {state_b}, {state_c}, {state_d}, {state_e}, {state_f}"
        print(state_sol)


proj = angr.Project('./summarize', load_options={'auto_load_libs': False})

start_addr = 0x40137B
initial_state = proj.factory.blank_state(addr=start_addr, add_options=angr.options.unicorn | {
    angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY, angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS})


class AddHook(angr.SimProcedure):
    def run(self, p1, p2):
        print('addition', p1 + p2)
        return p1 + p2


class SubtractHook(angr.SimProcedure):
    def run(self, p1, p2):
        print('subtract', p1 + p2)
        return p1 - p2


class MultiplyHook(angr.SimProcedure):
    def run(self, p1, p2):
        print('multiply', p1 + p2)
        return p1 * p2


class AndHook(angr.SimProcedure):
    def run(self, p1, p2):
        print('and', p1 + p2)
        return p1 & p2


class XorHook(angr.SimProcedure):
    def run(self, p1, p2):
        print('xor', p1 + p2)
        return p1 ^ p2


proj.hook_symbol(0x40163d, AddHook())
proj.hook_symbol(0x4016d8, SubtractHook())
proj.hook_symbol(0x4016fe, MultiplyHook())
proj.hook_symbol(0x40174a, XorHook())
proj.hook_symbol(0x4017a9, AndHook())

# logging.getLogger('angr').setLevel('DEBUG')

regs = initial_state.regs

regs.rbp = regs.rsp

size = 4 * 8
a = claripy.BVS('a', size)
b = claripy.BVS('b', size)
c = claripy.BVS('c', size)
d = claripy.BVS('d', size)
e = claripy.BVS('e', size)
f = claripy.BVS('f', size)

simgr = proj.factory.simgr(initial_state)

regs.edi = a
regs.esi = b
regs.edx = c
regs.ecx = d
regs.r8d = e
regs.r9d = f

initial_state.add_constraints(a > 0x5F5E100, a < 0x3B9AC9FF)
initial_state.add_constraints(b > 0x5F5E100, b < 0x3B9AC9FF)
initial_state.add_constraints(c > 0x5F5E100, c < 0x3B9AC9FF)
initial_state.add_constraints(d > 0x5F5E100, d < 0x3B9AC9FF)
initial_state.add_constraints(e > 0x5F5E100, e < 0x3B9AC9FF)
initial_state.add_constraints(f > 0x5F5E100, f < 0x3B9AC9FF)

print("[*] exploring binary")
start = time.time()
simgr.explore(find=0x401628, avoid=[0x4013D2, 0x401412, 0x40162F], step_func=visualize)

if simgr.found:
    solution_state = simgr.found[0]
    solved_a = format(solution_state.solver.eval(a), 'd')
    solved_b = format(solution_state.solver.eval(b), 'd')
    solved_c = format(solution_state.solver.eval(c), 'd')
    solved_d = format(solution_state.solver.eval(d), 'd')
    solved_e = format(solution_state.solver.eval(e), 'd')
    solved_f = format(solution_state.solver.eval(f), 'd')

    solution = f"[*] solution: {solved_a}, {solved_b}, {solved_c}, {solved_d}, {solved_e}, {solved_f}"
    print(solution)
    end = time.time()
    print(f"[*] time elapsed: {end - start}")
else:
    print("[*] no solution")
    print(simgr)
    print(simgr.errored)
```
Running this solution, will give us the following values:
![[UIUCTF2024 Summarize-20240701041819466.webp]]
When, putting it into the binary, we get:
![[UIUCTF2024 Summarize-20240701041840440.webp]]