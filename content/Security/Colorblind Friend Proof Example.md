---
tags:
  - math
  - logic
  - security
---
A example scenario of a [[Interactive Proof]].
# Scenario
![[Colorblind Friend Proofs-20250613124508969.webp]]
We attempt to prove to our colorblind friend that two balls are different colors.
1. Friend $(V)$ takes the balls, and hides them behind their back
2. Friend shows you a ball. now you seen this
3. Friend shuffles the balls in some sense, chooses one of the balls and shows you it
   ![[Colorblind Friend Proofs-20250613124626879.webp]]
4. Friend asks "Have i switched the balls?"
5. Because we can tell the balls from color, we can always answer this question
6. Repeat 128 times, this is to validate that guessing is [[Negligible Function|Negligible]].
# Properties
1. [[Designated Verifier]] : This proof only convinces your friend
2. [[Zero Knowledge]] : Your friend learns nothing except that the balls are different (they dont learn which ball was red, and which was green)