---
tags:
  - git
---
A set of rules for git commit messages.
# Structure
```
<type>[optional scope] : <description>
[optional body]
[optional footers]
```
### Types
- `fix` : A commit that patches bugs in codebases
- `feat` : A commit that introduces a new features
- `chore` : A routine commit
- `docs` : A documentation commit
- `build` : A change in build files
- `style` : A UI change
### Footers
- `BREAKING CHANGE` : commit that introduces a breaking [[Application Program Interface|API]] change
# Resources
- https://www.conventionalcommits.org/en/v1.0.0/