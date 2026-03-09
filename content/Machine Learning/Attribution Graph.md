---
tags:
  - machine_learning
---
A method that involves attached [[Transcoder]] to [[Transformer]] layers to view intermediate results of a neural network.
# Method
1. Use a [[Cross-Layer Transencoder|CLT]] or a a [[Simultaneous Authentication of Equals|SAE]] to remove [[Neuron Superposition|Polysemanticity]] for a local prompt (model will have to change for different prompts)
   ![[Attribution Graph-20260309195859933.webp]]
	1. Error nodes represent discrepancy between two models, but we cant interpret error nodes
2. Create an attribution graph comprised of:
	1. Nodes being the active features, [[Embeddings]] from the prompt, errors and output [[Logit]]
	2. Edges being the linear effects between nodes, activity of each features is the sum of its input edges
3. Use [[Transcoder]] to achieve linear attribution between features
4. Prune the attribution graph to most important components by removing nodes and edges not contributing to model output
5. Group related nodes (nodes with similar meaning) into super-nodes 
   ![[Attribution Graph-20260309200827974.webp]]