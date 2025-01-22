---
tags:
  - obsidian
  - javascript
---
Mermaid js is a javascript library that allows markdown generation of diagrams like flowcharts and trees.
Obsidian natively supports mermaid.js, so we can generate diagrams very easily using code blocks \`\`\` 

# Tree diagrams
```mermaid
graph TD;
id1((2)) --> id2((7));
id1((2)) --> id3((5));
id2((7)) --> id4((2));
id2((7)) --> id5((10));
id2((7)) --> id6((6));
id3((5)) --> id7((9));
id7((9)) --> id8((4));
id6((6)) --> id9((5));
id6((6)) --> id10((11));
```

```mermaid
graph TD;
Start-->Y
Start-->N
Y-->YY
Y-->YN
N-->NY
N-->NN
```

# Flow charts
```mermaid
graph TD;
A(Make Bed)
B(Spend 17 hours trying to tuck the corner of the sheet in)
C(End)
D(Well what else are you going to do?)

A-->|Yes|B
B-->C
A-->|Leave|C
A-->|No|D
D-->B
```
