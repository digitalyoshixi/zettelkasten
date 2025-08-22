---
tags:
  - programming
  - ruby
---
# Arithmetic Operators
|Operator|Description| Example                             |
| -------- | -------------------------------------------------------------------------------- | ----------------------------------- |
|&plus;|Addition − Adds values on either side of the operator.| a &plus; b will give 30             |
|−|Subtraction − Subtracts right hand operand from left hand operand.| a - b will give -10                 |
|*|Multiplication − Multiplies values on either side of the operator.| a * b will give 200                 |
|/|Division − Divides left hand operand by right hand operand.| b / a will give 2                   |
|%|Modulus − Divides left hand operand by right hand operand and returns remainder.| b % a will give 0                   |
|**|Exponent − Performs exponential (power) calculation on operators.| a\*\*b will give 10 to the power 20 |
# Comparison Operator
|Operator|Description|Example|
|---|---|---|
|==|Checks if the value of two operands are equal or not, if yes then condition becomes true.|(a == b) is not true.|
|!=|Checks if the value of two operands are equal or not, if values are not equal then condition becomes true.|(a != b) is true.|
|>|Checks if the value of left operand is greater than the value of right operand, if yes then condition becomes true.|(a > b) is not true.|
|<|Checks if the value of left operand is less than the value of right operand, if yes then condition becomes true.|(a < b) is true.|
|>=|Checks if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true.|(a >= b) is not true.|
|<=|Checks if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true.|(a <= b) is true.|
|<=>|Combined comparison operator. Returns 0 if first operand equals second, 1 if first operand is greater than the second and -1 if first operand is less than the second.|(a <=> b) returns -1.|
|===|Used to test equality within a when clause of a _case_ statement.|(1...10) === 5 returns true.|
|.eql?|True if the receiver and argument have both the same type and equal values.|1 == 1.0 returns true, but 1.eql?(1.0) is false.|
|equal?|True if the receiver and argument have the same object id.|if aObj is duplicate of bObj then aObj == bObj is true, a.equal?bObj is false but a.equal?aObj is true.|
# Assignment Operator
| Operator | Description                                                                                                                   | Example                                                   |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| =        | Simple assignment operator, assigns values from right side operands to left side operand.                                     | c = a &plus; b will assign the value of a &plus; b into c |
| &plus;=  | Add AND assignment operator, adds right operand to the left operand and assign the result to left operand.                    | c &plus;= a is equivalent to c = c &plus; a               |
| -=       | Subtract AND assignment operator, subtracts right operand from the left operand and assign the result to left operand.        | c -= a is equivalent to c = c - a                         |
| *=       | Multiply AND assignment operator, multiplies right operand with the left operand and assign the result to left operand.       | c *= a is equivalent to c = c * a                         |
| /=       | Divide AND assignment operator, divides left operand with the right operand and assign the result to left operand.            | c /= a is equivalent to c = c / a                         |
| %=       | Modulus AND assignment operator, takes modulus using two operands and assign the result to left operand.                      | c %= a is equivalent to c = c % a                         |
| **=      | Exponent AND assignment operator, performs exponential (power) calculation on operators and assign value to the left operand. | c \*\*= a is equivalent to c = c \*\* a                   |
# Bitwise Operator
|Operator|Description|Example|
|---|---|---|
|&|Binary AND Operator copies a bit to the result if it exists in both operands.|(a & b) will give 12, which is 0000 1100|
|\||Binary OR Operator copies a bit if it exists in either operand.|(a \| b) will give 61, which is 0011 1101|
|^|Binary XOR Operator copies the bit if it is set in one operand but not both.|(a ^ b) will give 49, which is 0011 0001|
|~|Binary Ones Complement Operator is unary and has the effect of 'flipping' bits.|(~a ) will give -61, which is 1100 0011 in 2's complement form due to a signed binary number.|
|<<|Binary Left Shift Operator. The left operands value is moved left by the number of bits specified by the right operand.|a << 2 will give 240, which is 1111 0000|
|>>|Binary Right Shift Operator. The left operands value is moved right by the number of bits specified by the right operand.|a >> 2 will give 15, which is 0000 1111|
# Logical Operator
| Operator | Description                                                                                                                                       | Example               |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| and      | Called Logical AND operator. If both the operands are true, then the condition becomes true.                                                      | (a and b) is true.    |
| or       | Called Logical OR Operator. If any of the two operands are non zero, then the condition becomes true.                                             | (a or b) is true.     |
| &&       | Called Logical AND operator. If both the operands are non zero, then the condition becomes true.                                                  | (a && b) is true.     |
| \|       | Called Logical OR Operator. If any of the two operands are non zero, then the condition becomes true.                                             | (a \| b) is true.     |
| !        | Called Logical NOT Operator. Use to reverses the logical state of its operand. If a condition is true, then Logical NOT operator will make false. | !(a && b) is false.   |
| not      | Called Logical NOT Operator. Use to reverses the logical state of its operand. If a condition is true, then Logical NOT operator will make false. | not(a && b) is false. |
# Ternary Operator
|Operator|Description|Example|
|---|---|---|
|? :|Conditional Expression|If Condition is true ? Then value X : Otherwise value Y|
# Range Operators
|Operator|Description|Example|
|---|---|---|
|..|Creates a range from start point to end point inclusive.|1..10 Creates a range from 1 to 10 inclusive.|
|...|Creates a range from start point to end point exclusive.|1...10 Creates a range from 1 to 9.|
# [[Ruby defined?]] Operator
```ruby
defined? method_call # True if a method is defined
```
# :: and .
- `.` to reference a method in a [[Ruby Module]]
- `::` to reference a constant in a [[Ruby Module]]