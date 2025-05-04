---
tags:
  - ctf
---
This challenge requires us to patch some code in app.
semgrep says that there is an instance of blocking warning.
![[BirthdayCTF2025 Simple Fix-20250504193003006.webp]]
If we look at the code, we see the final line that there is a debug=True statement, which should not be in production, so we remove that in the online editor, and the commit again. Then, we run the pipeline and get the flag!
`punk_{35MZKE9CJF9TZ9OW}`