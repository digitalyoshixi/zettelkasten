---
tags:
  - llvm
---
Similar to [[Javascript assert()]]
Its a developer annotation of expected values.
```llvm
; some code above
; for example, I expect my value in %_2.1 is always true
%1 = call i1 @llvm.expect.i1(i1 %_2.1, i1 true)
```

Not a very useful intrinsic