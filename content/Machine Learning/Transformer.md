---
tags:
  - machine_learning
---
These are [[Statistical Model|Models]] that exist to take an input token, and generate a distribution of output tokens that can be repeatedly sampled to continue generation.
# Structure
1. The [[Feature Encoding|Encoder]] will distill the input into its essential features
2. The input is interpreted as a sequence that attempts to generate the next few tokens. 
3. The model has attention which will be able to view the sequence at previous positions to assist in its generation.
4. The token is picked and the model continues through [[Causal Attention]]. This processing will occur in paralell with other sequences
5. The [[Feature Decoder|Decoder]] will expand the outputs into generative data
