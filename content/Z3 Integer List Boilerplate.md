---
tags:
  - reverse_engineering
  - security
---
```python
from z3 import *


# Create array of 39 integer variables (chars !! 0 through chars !! 38)
chars = [Int(f'chars_{i}') for i in range(39)]

# Add constraints based on the Haskell code
constraints = [
    (chars[37] * chars[15] == 3366),
    (chars[8] + chars[21] == 197),
    (chars[8] * chars[13] == 9215),
    (chars[0] * chars[3] == 2714),
    (chars[3] + chars[21] == 159),
    (chars[1] * chars[20] == 5723),
    (chars[11] * chars[7] == 11990),
    (chars[21] + chars[20] == 197),
    (chars[20] - chars[6] == -8),
    (chars[2] + chars[36] == 77),
    (chars[35] * chars[11] == 3630),
    (chars[4] * chars[3] == 2714),
    (chars[25] + chars[24] == 221),
    (chars[14] * chars[36] == 3465),
    ((chars[15] - chars[11]) - 148 == -156),
    (chars[37] + chars[17] == 138),
    (chars[9] + chars[29] == 212),
    (chars[30] - chars[10] == 7),
    (chars[10] + chars[33] == 206),
    (chars[7] * chars[15] == 11118),
    ((chars[28] * chars[14]) * 55 == 641025),
    (chars[24] + chars[4] == 151),
    (chars[2] * chars[30] == 4928),
    (chars[5] + chars[22] == 224),
    (chars[13] + chars[34] == 195),
    (chars[12] * chars[9] == 10403),
    (chars[18] + chars[31] == 200),
    (chars[17] + chars[32] == 213),
    (chars[2] * chars[12] == 4444),
    (chars[24] * chars[31] == 11025),
    (chars[5] * chars[0] == 5658),
    ((chars[10] + chars[32]) + 228 == 441),
    (chars[35] * chars[0] == 1518),
    (chars[28] - chars[34] == 11),
    (chars[26] * chars[14] == 9975),
    (chars[31] * chars[22] == 10605),
    ((chars[26] * chars[32]) * 239 == 2452140),
    (chars[28] * chars[38] == 13875),
    (chars[18] + chars[16] == 190),
    ((chars[27] + chars[26]) + 96 == 290),
    (chars[22] - chars[38] == -24),
    (chars[33] + chars[5] == 224),
    (chars[19] * chars[16] == 10355),
    (chars[27] + chars[1] == 158),
    (chars[33] + chars[12] == 202),
    (chars[19] * chars[23] == 10355),
    (BV2Int(Int2BV(chars[6], 32) | Int2BV(chars[37], 32)) == 105),
    (BV2Int(Int2BV(chars[29], 32) & Int2BV(chars[25], 32)) == 100),
    (BV2Int(Int2BV(chars[16], 32) | Int2BV(chars[29], 32)) == 127),
    (BV2Int(Int2BV(chars[35], 32) ^ Int2BV(chars[6], 32)) == 72),
    (BV2Int(Int2BV(chars[1], 32) ^ Int2BV(chars[38], 32)) == 70),
    (BV2Int(Int2BV(chars[7], 32) | Int2BV(chars[4], 32)) == 255),
    (BV2Int(Int2BV(chars[18], 32) | Int2BV(chars[36], 32)) == 127),
    (BV2Int(Int2BV(chars[9], 32) | Int2BV(chars[17], 32)) == 111),
    (BV2Int(Int2BV(chars[25], 32) ^ Int2BV(chars[27], 32)) == 23),
    (BV2Int(Int2BV(chars[13], 32) ^ Int2BV(chars[34], 32)) == 59),
    (BV2Int(Int2BV(chars[30], 32) | Int2BV(chars[8], 32)) == 113),
    ]

for i in range(len(constraints)):
    solver = Solver()
    for v in range(i):
        solver.add(constraints[v])
    
    # Check if the constraints are satisfiable
    print(f"Solving constraints... {i}")
    if solver.check() == sat:
        # Get the model (solution)
        model = solver.model()
        print("Solution found!")
        
        # Print all values in order
        solution = []
        for i in range(39):
            value = model[chars[i]]
            if value is not None:
                solution.append(int(str(value)))
                print(f"chars[{i}] = {value}")
            else:
                print(f"chars[{i}] = [unconstrained]")
        
        # Convert to characters if they're in ASCII range
        print("\nAs characters (if in printable ASCII range 32-126):")
        char_string = ""
        for i, val in enumerate(solution):
            if 32 <= val <= 126:
                char_string += chr(val)
                print(f"chars[{i}] = {val} = '{chr(val)}'")
            else:
                print(f"chars[{i}] = {val} (not printable ASCII)")
        
        if char_string:
            print(f"\nPossible flag: {char_string}")
        
    else:
        print('No solution found')

```