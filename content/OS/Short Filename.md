---
tags:
  - os
  - file_system
aliases:
  - SFN
---
A filename that conforms to:
- Eight characters, less than 8 is padded with `0x20`
- Three characters allocated for file extension, less than 3 is padded with `0x20`
- Spaces and `+`, `*`, `,`, `.`, `/`, `:`, `;`, `<`, `=`, `>`, `?`, `[`, `\`, `]`, `|`