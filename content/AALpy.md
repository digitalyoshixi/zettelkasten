---
tags:
  - verification
---
A tool for [[Automata Learning]].
# Installation
```
pip install aalpy
```
Also install [[GraphViz]]
# Process
1. Find [[System Under Learning|SUL]] to test with
2. Define input alphabet (all possible actions)
3. Create a AAL SUL class
4. Choose the oracle to use
5. Choose the learning algorithm to use
6. Check results
# Oracles
- [[Random Word Equivalence Oracle]]
- [[Random W-Method]]
# Algorithms
- [[L*]]
- [[Stochastic L*]]
- [[RPNI]]
# Examples
### Active Learning
```python
from aalpy.base import SUL  
from aalpy.learning_algs import run_Lstar  
from aalpy.oracles import RandomWalkEqOracle  
  
# Step 1.  
# wrap the AALpy's SUL interace  
class VendingMachineSUL(SUL):  
    # initialize with the concrete implementation of the vending machine under learning  
    def __init__(self, vending_machine):  
        super().__init__()  
        self.vm = vending_machine  
      
    # define the reset of the system  
    def pre(self):  
        self.vm.reset()  
      
    # sometimes reset can be nicely split in two phases, one that initializes  
    # the SUL, and the other that gracefully shuts it down  
    # We will do it all in one in the pre() method.  
    def post(self):  
        pass  
      
    # define the mapping between the elements of the input alphabet and   
    # return processed output  
    def step(self, letter):  
        # in our input alphabet, each element is a tuple (action, parameter)  
        # so letter[0] determines which action to execute on the vending machine  
        # and letter[1] with which parameter  
        if letter[0] == 'coin':  
            return self.vm.add_coin(letter[1])  
        if letter[0] == 'order':  
            return self.vm.push_button(letter[1])  
        raise RuntimeError('Invalid input')  
  
# actions that can be taken on the SUL  
input_alphabet = [('coin', 1), ('coin', 2), ('order', 'water'),   
                  ('order', 'coke'), ('order', 'peanuts')]  
  
# assume we are given some black-box vending machine implementaiton  
vending_machine_implementation = BlackBoxVendingMachine(max_coins=5)  
  
# wrap the concrete vending machine implementation in SUL interface  
sul = VendingMachineSUL(vending_machine)  
  
# Step 2.  
# define the equivalence oracle used for conformance testing during learning  
eq_oracle = RandomWordEqOracle(input_alphabet, sul, num_walks=1000,   
                               min_walk_len=3, max_walk_len=12)  
# eq_oracle = RandomWMethodEqOracle(input_alphabet, sul,   
#                                   walks_per_state=10, walk_len=8)  
  
# Step 3.  
# learn the mealy machine capturing the input-output behaviour   
# of the vending machine  
learned_model = run_Lstar(input_alphabet, sul, eq_oracle, 'mealy')  
  
# if the system behaves stochastically  
# from aalpy.learning_algs import run_stochastic_Lstar  
# learned_stochastic_model = run_stochastic_Lstar(input_alphabet, sul, eq_oracle, 'mealy')  
  
# visualize the learned model  
learned_model.visualize()
```
### Passive Learning
```python
from aalpy.learning_algs import run_RPNI  
  
# data is in the format (inputSequance, output)  
data = [  
  ([('order', 'water'), ('order', 'coke'), ('coin', 1)], 'coin_added'),  
  ([('order', 'peanuts'), ('order', 'coke'), ('coin', 1), ('coin', 1), ('order', 'coke'), ('order', 'peanuts'), ('coin', 2), ('order', 'water')], 'Water'),  
  ([('order', 'water'), ('coin', 1), ('order', 'water'), ('coin', 2), ('order', 'coke'), ('order', 'water'), ('order', 'coke')], 'No_Action'),  
  ([('order', 'coke'), ('coin', 2), ('coin', 2), ('order', 'water'), ('coin', 2), ('coin', 1), ('order', 'coke')], 'Coke'),  
  ([('order', 'coke'), ('order', 'peanuts'), ('order', 'peanuts'), ('coin', 2), ('order', 'coke'), ('order', 'peanuts')], 'No_Action'),  
  ([('order', 'peanuts'), ('coin', 2), ('order', 'peanuts'), ('coin', 1), ('order', 'water'), ('order', 'coke')], 'Coke'),  
  # ...  
]  
  
# run RPNI passive learning algorithm  
learned_model = run_RPNI(data, automaton_type='moore')  
  
learned_model.visualize()
```
### [[Differential Analysis]]
```python
from aalpy import run_Lstar, bisimilar, compare_automata, RandomWordEqOracle  
  
from VendingMachineLearner import VendingMachineSUL  
from VendingMachinesImpl import VendingMachine, VendingMachineMutant2  
  
vending_machine_1 = VendingMachine(max_coins=5)  
vending_machine_2 = VendingMachineMutant2(max_coins=5)  
  
  
def active_learning(input_alphabet, vending_machine_impl):  
    sul = VendingMachineSUL(vending_machine_impl)  
    eq_oracle = RandomWordEqOracle(input_alphabet, sul, num_walks=1000,  
                                   min_walk_len=3, max_walk_len=12)  
    return run_Lstar(input_alphabet, sul, eq_oracle, 'mealy')  
  
  
# use the same input alphabet and SUL implementation from the previous example  
input_alphabet = [('coin', 1), ('coin', 2), ('order', 'coke'), ('order', 'water'),  
                  ('order', 'peanuts')]  
  
# we learn the complete model of both vending machines  
learned_vm1 = active_learning(input_alphabet, vending_machine_1)  
learned_vm2 = active_learning(input_alphabet, vending_machine_2)  
  
# find a shortest differance between models  
shortest_counterexample = bisimilar(learned_vm1, learned_vm2,  
                                    return_cex=True)  
  
# if a shortest counterexample is found, print the differences  
if shortest_counterexample:  
    shortest_counterexample = tuple(shortest_counterexample)  
    output_vm1 = learned_vm1.execute_sequence(learned_vm1.initial_state, shortest_counterexample)  
    output_vm2 = learned_vm2.execute_sequence(learned_vm2.initial_state, shortest_counterexample)  
  
    print('CEX:', shortest_counterexample)  
    print(f'Vending Machine 1: {output_vm1}')  
    print(f'Vending Machine 2: {output_vm2}')  
  
# if we want more counterexamples we can use following function  
additional_counterexamples = compare_automata(learned_vm1, learned_vm2, num_cex=10)
```