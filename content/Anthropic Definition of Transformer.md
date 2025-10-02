---
tags:
  - machine_learning
---
# Antropic Defn
![[Transformer-20250628151644118.webp]]
1. Input text is [[Tokenizer|Tokenized]]. Often through [[Byte Pair Encoding|BPE]].
2. Tokenized input then [[Positional Encoding]]
3. The [[Feature Encoding|Encoder]] will distill the input into its essential features. Often through [[One Hot Encoding]]
4. The encoded text is [[Text Embeddings|Embedded]] through a [[Look Up Table Matrix]]
5. The encoded text is sent into the [[Residual Stream]]
	1. Each layer in the stream is stored as a [[Transformer Block]] (Which includes an [[Attention Layer]], )
6. The token is picked and the model continues through [[Causal Attention]] and [[Self Attention Layer]]. This processing will occur in paralell with other sequences
7. The [[Feature Decoder|Decoder]] will expand the outputs into generative data