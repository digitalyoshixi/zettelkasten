---
tags:
  - security
---
# Syntax
- `pattern`: matches code that fits specified expression
- `pattern-not`: matches code that does not conform to expression
- `patterns`:  triggers for multiple patterns with [[And|Logical And]]
- `pattern-either`: triggers for multiple patterns with [[Or|Logical Or]]
- `pattern-regex`: matches strings using [[Perl-Compatible Regular Expression]]
- `pattern-not-regex`: Matches patterns not conforming to the regex
- `pattern-inside`: matches code located within given expression
- `pattern-not-inside`: matches code located outside given expressionn
- `...`: matches zero or more elements
- `$VAR`: a variable defined
- `$_`: wildcard variable
- `#comment`: comment