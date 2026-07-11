---
tags:
  - verification
---
A [[Passive Automata Learning]] algorithm described in [[Learning Moore Machines from Input Output Pairs|LMoIO]].
- Builds a [[Moore Machine Prefix Tree Acceptor|PTAP]] represented by $N$ [[Trie|PTA]]
- Custom merging phase
- Synchronous product of all $N$ DFAs is formed
- Add self-loops for missing input symbols
# Merge Function
```
def MooreMI ( trace set , ΣI , ΣO ):
2
3 ( list of pos example sets ,
4 list of neg example sets ,
5 bits to output func )
6 := preprocess moore traces( trace set )
7
8 N := ceil( log2 ( |ΣO | ) )
9
10 DFA list := build pref ix tree acceptor product(
11 list of pos example sets , ΣI , ΣO )
12
13 red = { q }
14 blue = { qa for a in ΣI } ∩ DFA list [0].Q
15
16 while blue 6 = ∅:
17
18 q blue = pick next(blue)
19 blue := blue − {q blue}
10
20
21 merge accepted := false
22
23 for q red ∈ red:
24
25 for i ∈ {0, ..., N − 1}:
26 new DFA list [i] :=
27 merge( DFA list [i], q red , q blue )
28
29 if ∀ i ∈ {0, ..., N − 1}:
30 is consistent(
31 new DFA list [i],
32 list of neg example sets [i]):
33 merge accepted := true
34 break
35
36 if merge accepted :
37 DFA list := new DFA list
38 blue := blue ∪ ( { one−letter
39 successors of red states }
40 ∩ DFA list [0].Q )
41 else:
42 red := red ∪ {q blue}
43 blue := blue ∪ ( { one−letter
44 successors of q blue }
45 ∩ DFA list [0].Q )
46
47 return product(
48 DFA list ,
49 bits to output func ).make complete()
50
51 def merge(DFA , q red , q blue ):
52
53 q u := unique parent of ( q blue )
54 a u := unique input f rom to( q u , q blue )
55
56 DFA.δ( q u , a u ) := q red
57
58 merge stack := [( q red , q blue )]
59
60 while merge stack 6 = []:
61
62 ( q 1 , q 2 ) := pop( merge stack )
63
64 if q 1 = q 2 : continue
65
66 if ( q 1 , q 2 ) 6 = ( q red , q blue )
67 and q 2 < q 1 :
68 q 1 , q 2 := q 2 , q 1
69
70 DFA.Q := DFA.Q − {q 2}
11
71
72 if q 2 ∈ DFA.F :
73 DFA.F := DFA.F ∪ {q 1}
74
75 for a ∈ DFA.Σ:
76 if is def ined(DFA.δ( q 2 , a)):
77 if is def ined(DFA.δ( q 1 , a)):
78
79 push( merge stack ,
80 DFA.δ( q 1 , a),
81 DFA.δ( q 2 , a)))
82 else:
83 DFA.δ( q 1 , a) := DFA.δ( q 2 , a)
84
85 return DFA
```
# Paper
https://arxiv.org/pdf/1605.07805