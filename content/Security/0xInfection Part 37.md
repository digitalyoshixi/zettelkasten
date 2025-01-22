### Part 37 CMOV instruction

CMOV is is a less resource intensive method for the processor to execute jump.

 
|Action|explanation|
|-|-|
|CMOVA or CMOVNBE|above(carry flag or zero flag is 0)|
|CMOVAE or CMOVNB|Above or equal(carry flag = 0)|
|CMOVNC|Not carry(carry flag = 0)|
|CMOVB or CMOVNAE|below(carry flag = 1)|
|CMOVC|carry(carry flag = 1)|
|CMOVBE or CMOVNA|Below or equal(carry flag or zero flag is 1)|
|CMOVE or CMOVZ|equal(zero flag = 1)|
|CMOVNE or CMOVNZ|Not equal(parity flag = 1)|
|CMOVP or CMOVPE|parity(parity flag = 1)|
|CMOVNP or CMOVPO|Not parity(parity flag = 0)|
|CMOVGE or CMOVNL|Greater or equal sign(sign flag xor Overflow flag = 0)|
|CMOVL or CMOVNGE|less(sign flag xor overflow flag =1)|
|CMOVLE or CMOVING|Less or equal(sign flag xor overflow flag or ZF = 1)|
|CMOVO|overflow(overflow flag = 1)|
|CMOVNO|Not overflow(overflow flag = 0)|
|CMOVS|Sign NEGATIVE(sign flag = 1)|
|CMOVNS|Not sign positive(sign flag = 0)|