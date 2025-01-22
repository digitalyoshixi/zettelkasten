---
tags:
  - ASMTutor
  - x86
---
### Lesson 18 Fizzbuzz

This is a programmer interview question that goes something like this. Remark “fizz” is a number is divisible by 3, remark “buzz” if a number is divisible by 5, remark “fizzbuzz” if a number is divisible by both 3 and 5.

Since if, else, elsif dont exist, in order for the else statement to know that all other comparisons failed, you will need to make flags of them succeeding and compare each flag to determine the else condition.

So structuring if, elsif and else statements will require you for each conditional of if and elsif to have these properties:

1. The comparisson inside the if/elsif function
    
2. The action inside the if/elsif function
    
3. Ticking a flag is the action was performed
    
4. Checking the flag inside of the else function(you can push to stack if registers in use)
    

For the else function, we must compare each flag with true. If the flag is true, then jump to the finishing segment of code, if all flags are false, then execute the else statement code.