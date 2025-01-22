---
tags:
  - llvm
---
Used as labels similar to [[C goto]] structure.
```
; ModuleID = 'example.bc'
@.str = private unnamed_addr constant [3 x i8] c"%d\00", align 1

define i32 @main() nounwind uwtable {
entry:
    %a = alloca i32, align 4
    %1 = call i32 (i8*, ...)* @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8]* @.str, i64 0, i64 0), i32* %a) nounwind
    %2 = load i32* %a, align 4
    %3 = icmp sgt i32 %2, 3
    br i1 %3, label %then, label %else

then:
    %4 = shl nsw i32 %2, 1
    store i32 %4, i32* %a, align 4
    br label %end

else:
    br label %end

end:
    ret i32 0
}

```