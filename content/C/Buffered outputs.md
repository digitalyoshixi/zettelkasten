---
tags:
  - programming
---
buffering is used in streams like output streams. for example, outputting strings. statements in our program get in a line that is stored in a region of memory set aside to collect these requests called buffers, then that buffer is flushed meaning all the data is transferred to its destination(in this case, the console)

This also means that if your program crashes or aborts or pauses(like for debugging), any output still waiting inside the buffer will not be displayed

There is also [[Unbuffered outputs]]