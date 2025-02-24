---
tags:
  - ctf
---
# Recon
1. Running the program on x86-64 will yield a invalid instruction detected. This is the instruction:
![[MagpieCTF2025 Binary Betrayl-20250223002542524.webp]]
1. Looks like this binary is ran with [[Pyinstaller]]
![[MagpieCTF2025 Binary Betrayl-20250223003723680.webp]]
1. Research reverse engineering pyinstaller files: https://reverseengineering.stackexchange.com/questions/160/how-do-you-reverse-engineer-an-exe-compiled-with-pyinstaller
2. https://github.com/pyinstxtractor/pyinstxtractor-ng
   ![[MagpieCTF2025 Binary Betrayl-20250223005551253.webp]]
3. Using pylingual, we get the following decompilation: https://www.pylingual.io/view_chimera?identifier=b21051f9f6c3d84999c6a4fe674227675c9b657715c7eb56b748c4b0369d18b3
```python
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Which.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import math
import random

def main():
    Legal_troubles()

def competitor_file(a, b):
    result = 0
    str = 'magpieCTF{Ro+_7hir+een}'
    for i in range(1, 50):
        result += a * i % b
    return result

def operations_planning():
    x = random.randint(1, 100)
    y = random.randint(1, 50)
    for _ in range(25):
        str = 'magpieCTF{Rever5e_7he_[ode}'
        z = competitor_file(x, y)
        if z % 2 == 0:
            x = z * 3 % 50
        else:
            y = (z + x) % 75

def Legal_troubles():
    anflag = 'purpx_svanapvny_erpbeqf'
    str = 'magpieCTF{D3c0d1ng_FuN}'
    aflag = f'flag-{anflag}'
    output_lines = ['running?{' + aflag + '}', 'about{' + aflag + '}', 'anything{' + aflag + '}', 'said{' + aflag + '}', 'Who{' + aflag + '}']
    for line in output_lines:
        print(line)
    financial_records(str)

def operational_costs(x):
    for i in range(1, 37):
        x ^= i * (x % 7) + (i << 2)
    return x * 3 % 12345

def financial_records(data):
    temp = [ord(char) for char in data]
    for _ in range(5):
        temp = [(val * 7 >> 3) % 256 for val in temp]
    str = 'magpieCTF{Rich_3nou9h_7o_$+@y_C1e@n}'
    print(''.join([chr(val) for val in temp]))
    return ''.join([chr(val) for val in temp])

def resolution_notes(a, b, c):
    result = 0
    for i in range(1, 13):
        temp = math.sqrt(a * i % b + c)
        if int(temp) % 2 == 0:
            str = 'magpieCTF{N0t_Th3_R34L_Fl4g}'
            result += int(temp)
        else:
            result ^= i
    return result

def data_warehousing(n):
    arr = [n]
    for i in range(1, 256):
        arr.append(arr[-1] * i % 10007)
    while len(arr) > 1:
        arr = [arr[i] + arr[i + 1] for i in range(0, len(arr) - 1, 2)]
    return arr[0]

def confusing_money_drain(data):
    return ''.join([chr(ord(char) * 3 % 256 ^ 7) for char in data])

def distraction_toys():
    noise = [random.randint(0, 100) for _ in range(50)]
    for i in range(len(noise)):
        noise[i] = (noise[i] * 17 + i) % 256
        if noise[i] % 3 == 0:
            noise[i] ^= i * 7
    return sum(noise)
if __name__ == '__main__':
    str = 'magpieCTF{N07_57_3n0ugh}'
    main()

def hidden_Stash(data):
    key = 42
    for char in data:
        key = key * ord(char) % 98765
    return key

def family_mess(encoded):
    intermediate = ''.join([chr((ord(char) - 7) // 3 % 256) for char in encoded])
    str = 'magpieCTF{C0d3_3xp0s3d}'
    return ''.join(reversed(intermediate))

def directors_removed(x, y, z):
    if z % 3 == 0:
        return x * y - z
    return x ^ y ^ z

def other_business(data):
    output = ''
    for char in data:
        output += chr((ord(char) + 47) % 256 ^ 89)
    return output

def legal_business(a, b):
    c = 'irrelevant'
    str = 'magpieCTF{R3v3r53_3v3ryth1ng}'
    return directors_removed(a, b, len(c))
```
- ![[MagpieCTF2025 Binary Betrayl-20250223015103327.webp]]
So, just do as it says, check financial records!
```
magpieCTF{Rich_3nou9h_7o_$+@y_C1e@n}
```
