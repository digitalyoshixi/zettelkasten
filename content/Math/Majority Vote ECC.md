---
tags:
  - cryptography
aliases:
  - One ECC
---
A method for fixing [[Error Correcting Codes|ECC]] by finding the most common similarities between several sent messages.
Can only fix 1-bit of error.
# Process
- Alice are sent in triplets. $010 \to 000, 111, 000$
- If an error occurs, we can see it on Bob's end ($000, 101, 000$) Note that $101$ is not in triplets, we fix this by seeing that $1$ is the majority item
# Flaws
- This method fails if 2 bits fail, $000,111,000 \to 000,001,000$ is not recoverable!