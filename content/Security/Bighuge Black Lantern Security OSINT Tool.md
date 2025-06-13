---
tags:
  - security
aliases:
  - BBOT
---
A osint tool used to recursively scan website domain relations
# Installation
```
pip install bbot
```
# Usage
### Find all links
```
bbot -t website.com
```
### Find all subpages
```
bbot -t lnor.net -p spider -c web.spider_distance=2 web.spider_depth=2  
```