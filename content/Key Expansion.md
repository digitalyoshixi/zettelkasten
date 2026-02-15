---
tags:
  - cryptography
  - math
aliases:
  - Key Schedule
---
A step in [[Advanced Encryption Standard|AES]], creates $n$ round keys
- $n = 11$ if AES-128
- $n = 13$ if AES-192
- $n = 15$ if AES-256
# Process
![[Key Expansion-20260215202355878.webp]]
The round key expansion is a recursive process.
1. We split our initial key into 32-bit (4-byte) length vectors
	1. 4 vectors for AES-128
	2. 6 vectors for AES-192
	3. 8 vectors for AES-256
2. We take the last vector, run it through:
	1. [[RotWord]]
	2. [[SubWord]]
	3. [[RCon]]
3. We [[Exclusive Or|XOR]] the result of RCon with the previous vector of the last key to get the next round-key vector in the series, until you get all 4 round key vectors for the round
4. Repeat until you get all $n$ keys
# Implementation
```python
def expand_key(master_key):
    """
    Expands and returns a list of key matrices for the given master_key.
    """

    # Round constants https://en.wikipedia.org/wiki/AES_key_schedule#Round_constants
    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    # Initialize round keys with raw key material.
    key_columns = bytes2matrix(master_key)
    iteration_size = len(master_key) // 4

    # Each iteration has exactly as many columns as the key material.
    i = 1
    while len(key_columns) < (N_ROUNDS + 1) * 4:
        # Copy previous word.
        word = list(key_columns[-1])

        # Perform schedule_core once every "row".
        if len(key_columns) % iteration_size == 0:
            # Circular shift.
            word.append(word.pop(0))
            # Map to S-BOX.
            word = [s_box[b] for b in word]
            # XOR with first byte of R-CON, since the others bytes of R-CON are 0.
            word[0] ^= r_con[i]
            i += 1
        elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
            # Run word through S-box in the fourth iteration when using a
            # 256-bit key.
            word = [s_box[b] for b in word]

        # XOR with equivalent word from previous iteration.
        word = bytes(i^j for i, j in zip(word, key_columns[-iteration_size]))
        key_columns.append(word)

    # Group key words in 4x4 byte matrices.
    return [key_columns[4*i : 4*(i+1)] for i in range(len(key_columns) // 4)]
```