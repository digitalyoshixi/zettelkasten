---
tags:
  - security
---
A keyword used to find the most common values of fields.
```
sourcetype=access_* | top
```
# Returning only one category
```
sourcetype=access_* | top categoryId
```
returns the categoryId fields from all items.