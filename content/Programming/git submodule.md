---
tags:
  - git
---
### Submodule
https://www.youtube.com/watch?v=gSlXo2iLBro
##### Adding Submodule
`git submodule add https://github.com/digitalyoshixi/calculus12raw foldernameuwant`
then edit .gitmodules to change the path if you so desire it
##### Deleting Submodule
```
git submodule deinit <name_of_submodule>
git rm -f <name_of_submodule>
rm -rf .git/modules/<name_of_submodule>
git commit -m "oopsie fixed"
```