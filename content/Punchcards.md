---
tags:
  - programming
aliases:
  - Turing Machine Rules
---
These are instructions for [[Turing Machine]]

# Rule Structure
- Each rule is given two types. One for when the head reads 0, and another for when the head reads 1
  ![[Punchcards-20250618133343247.webp]]
- Each rule is structured in the form of `Write|Move|Next_Rule`
  ![[Punchcards-20250618133441873.webp]]

# Instructions
Each Turing machine card is created with 4 operations:
- Check what character is under my head (0 or 1)
- Write a character to the head (0 or 1)
- Move the head left or right (0 for left, 1 for right)
- Go to the next card (Card number. Card 0 is the halt card)
![[Drawing 2025-06-18 09.19.27.excalidraw]]