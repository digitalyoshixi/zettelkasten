---
tags:
  - git
---
### branch
- `git branch <new-branch-name>`
# Push to a New Branch
```
git checkout -b mynewbranch
git add .
git commit -m "my message"
git push origin mynewbranch
```
Alternatively:
- Commit changes in your current branch (e.g `main`)
- `git checkout otherbranch`
- `git merge main`