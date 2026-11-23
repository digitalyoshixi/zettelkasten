---
tags:
  - file
---
# Compress Fully
```
qpdf --compress-streams=y --recompress-flate --compression-level=9 --object-streams=generate --optimize-images input.pdf output.pdf
```