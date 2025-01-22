There are different methods to writing operations.

### Prefix

In prefix notation, operations come before the operand. In our infix example of the equation 2 + 5 * 3, in prefix it would be + 2 * 5 3 which is wack af, but it works yknow

  
  

### Postfix

In postfix notation, you list all operands come before operations. Again using the infix example. In postfix, it is: 2 5 3 + * again crazy to think about!

  

### Infix to Prefix/Postfix

the goal is to isolate into pairs of 2 then apply the rule for prefix

7 * 3 – 6 / 2 + 4 ^ 2

(* 7 3) – (/ 6 2) + (^ 4 2)

(– * 7 3 / 6 2) + (^ 4 2)

+ – * 7 3 / 6 2 ^ 4 2

For postfix:

7 * 3 – 6 / 2 + 4 ^ 2

(7 3 *) – (6 2 /) + (4 2 ^)

(7 3 * 6 2 / –) + (4 2 ^)

7 3 * 6 2 / – 4 2 ^ +

  

### Calculate from Prefix/Postfix

Just remember the rules, operator first for prefix, operator post for postfix.

For prefix:

+ – * 7 3 / 6 2 ^ 4 2

+ – (7 * 3) (6 / 2) (4 ^ 2)

+ – 21 3 16

+ (21 – 3) 16

+ 18 16

18 + 16 = 34

For postfix:

(7 * 3) (6 / 2) – (4 ^ 2) +

21 3 – 16 +

(21 – 3) 16 +

18 16 +

18 + 16 = 34