---
tags:
  - machine_learning
---
These are [[Statistical Model|Models]] that exist to take an input token, and generate a distribution of output tokens that can be repeatedly sampled to continue generation.
# Structure
1. The [[Feature Encoding|Encoder]] will distill the input into its essential features
2. The input is interpreted as a sequence that attempts to generate the next few tokens. 
3. The token is picked and the model continues through [[Causal Attention]]
4. The [[Feature Decoder|Decoder]] will expand the outputs into generative data
