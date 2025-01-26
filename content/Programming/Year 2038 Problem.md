---
tags:
  - c
  - internet_culture
---
Haha, its like Y2K all over again.

A common way to represent time in UNIX/C programs was to use a 32bit integer for the # of seconds that have passed since 1/1/1970. But, this would result in a overflow when the date reaches 1/19/1970.

To fix this, we converted to long values which allow us 64bits.
This gives us ~300 billion years more time.