---
tags:
  - gitlab
---
No way to do this from terminal I believe.
Initializing a repo needs to be done on website.
https://gitlab.com/projects/new#blank_project
![[Making Gitlab Project-20231008182312112.webp]]
Go to settings > repository
![[Making Gitlab Project-20231008183554365.webp|483]]
Protected Branches > Allow force push
![[Making Gitlab Project-20231008183702274.webp|612]]
Now, open your terminal. cd into your repo with the .git file, and type the following:
```
git remote add origin https://gitlab.com/Yoshixi/yourreponame.git 
git branch -M main
git push -uf origin main
```
Gitlab will log you in via browser or ssh, use either.
And then your local repo files will be on gitlab. good to go.