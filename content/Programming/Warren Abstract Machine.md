---
tags:
  - programming
aliases:
  - WAM
---
A [[Abstract Machine]] for the execution of [[Prolog]] programs.
# Structure
- Has a global [[Stack]] to store compound terms
- Has a local [[OS Stack|Stack]] to store choice-points
- Has a [[Trail]] to record which variable bindings must be undone on backtracking