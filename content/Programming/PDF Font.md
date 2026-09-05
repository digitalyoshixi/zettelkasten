---
tags:
  - programming
---
A PDF font is comprised of 3 PDF objects:
- `Font`
- `FontDescriptor`
- `FontFile`
```postscript
1 0 obj
<<
  /Type /Font
  /Subtype /Type1
  /FontDescriptor 2 0 R
  /BaseFont /FooBarFont
>>
endobj

2 0 obj
<<
  /Type /FontDescriptor
  /FontName /FooBarFont
  /FontFile 3 0 R
  /ItalicAngle 0
  /Flags 4
>>
endobj

3 0 obj
<<
  /Length 100
>>
... (actual binary font data) ...
endobj
```