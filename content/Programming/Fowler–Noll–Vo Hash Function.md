---
tags:
  - programming
aliases:
  - FNV
---
A hash function that is non-cryptographic
# Pseudocode
```
algorithm fnv-1 is
    hash := FNV_offset_basis

    for each byte_of_data to be hashed do
        hash := hash × FNV_prime
        hash := hash XOR byte_of_data

    return hash 
```