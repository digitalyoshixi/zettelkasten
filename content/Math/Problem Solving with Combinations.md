---
tags:
  - math
---
Depending on your sample size, with your duplicates, you will have different [[Combinations]]

# Coins Example
How many sums of money can you create with: 
1 penny. 1 nickel. - **3 combinations**
1 penny, 1 nickel, 1 dime. - **7 combinations**
2 penny, 1 dime. - **5 combinations**
3 penny, 1 dime. - **7 combinations**

### Case 1:
For each coin, we either chose to include it in the sum, or not include it in the sum. 
For 1 penny, 1 nickel. 2 choices \* 2 choices = 4. but, we cannot have a sum of 0, so subtract 1 = 3.

### Case 3:
There are 2 pennies and 1 dime.
![[Pasted image 20230927133803.png]]
For the 2 pennies, group them and calculate the combinations.
Either we pick 2, we pick none or we pick one.
Then, with the combinations of the dime, there are only 2.
3 \* 2 - 1 = 5

Use [[Combination Subset Formula]]
