---
tags:
  - security
  - verification
---
A method of [[Fuzzing]] for structured data.
- Apply random mutation to a set of valid inputs.
- More likely to produce interesting invalid inputs than just randomness
- Good for semi-structured data
	- [[Waveform Audio File Format|wav]]
# Mutation Techniques
- Swapping bytes
- Deleting bytes
- Bit flipping
- Byte flipping
- SImple arithmetic
- AOverwriting values with interesting integers
- Adding/Deleting portions of test cases
- Splicing two distinct input files at random locations