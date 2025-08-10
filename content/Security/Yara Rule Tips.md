---
tags:
  - security
  - malware
---
https://www.youtube.com/watch?v=xKeF_cPKXt0
# [[Yara Strings]] Tips
1. Avoid short strings
2. Avoid breaking [[Yara Hexadecimal String]] into segments smaller than 4 bytes
   ![[Yara Rule Tips-20250808013109941.webp|368]]
3. Do not add leading or trailing wildcards to [[Yara Hexadecimal String]], it doesnt change anything
4. Avoid [[Yara Regular Expression]], if you must use a regex, then ensure there is a 4-byte string to act as a [[Yara Searching Algorithm|Yara Atom]].
   ![[Yara Rule Tips-20250808013242325.webp]]
5. Avoid repeating single byte strings. The best [[Yara Searching Algorithm|Yara Atom]] will occur VERY often
   ![[Yara Rule Tips-20250808013350722.webp|384]]
6. Use the `nocase` keyword sparingly. It creates `n!` variants of the string
   ![[Yara Rule Tips-20250808013442943.webp]]
# [[Yara Imports|Yara Modules]] Tips
1. Including a module means every file must be scanned by the module. Dont use module imports if you can write a faily simple conditional instead.
   ![[Yara Rule Tips-20250808013725614.webp]]
# [[Yara Conditions]]
1. Yara conditions will have a short-circuit feature, where the first false condition will end a `AND` conjunction. Place your conditions strategically
   ![[Yara Rule Tips-20250808013910367.webp]]