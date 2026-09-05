---
tags:
  - security
  - web
---
An attack against applications to retrieve [[eXtensive Markup Language|XML]] data with custom `XPath` queries to gain unauthorized access.
```xml
<student_database>
<student><username>jan</username><passwd>abcd1234</passwd>
</student>
<student><username>kees</nameuser><passwd>geheim</passwd>
<student>
</student_database>
```
With injection `(//student[username/text()='jan' and passwd/text()='abcd123']/account/text()) _database>`
or `'or '1'='1'`
# Mitigations
- [[Parameterized XPath Evaluation]]