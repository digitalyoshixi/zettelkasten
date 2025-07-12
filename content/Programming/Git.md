---
tags:
  - libre
  - git
aliases:
---
A repository is a folder or place where your project is kept
Git is the method that tracks change of a file overtime
[[Github]], [[Gitlab]], Bitbucket, etc.. are all based off git
# Setup
### Username and Email Setup
```
git config --global user.name "yoshixi"
git config --global user.email "davidchenyuhe@proton.me"
```
# Concepts
- [[Git Commit Conventions]]
- [[Git Branching Conventions]]
# Commands
### init
Creates a .git folder for a completely new repo
### clone
Grabs an already created repository
- `git clone https://github.com/digitalyoshixi/Calculus12.git`
- `git clone git clone -b <branch> <remote_repo>
### add
Adding some files to the repository
- `git add .` adds all files
### commit
Save your files
- `git commit -m "commit msg"` commits all files
### push
upload files to remote repository
- `git push` push all committed
- `git push -u origin main` pushes to main branch at original repo
- `git push -u origin feat/mybranch` push to a branch
- `git push origin feat/branch1:feat/branch2` push current changes from existing branch to other branch
### pull
download changes from github or another repository-
- `git pull` pull from main branch
### log
See all commit hashes within a repo
- `git log`
### checkout
Reverts to a previous change
- `git checkout <commithash>`
Change to a branch
1. `git checkout <branchname>`
2. `git pull origin <branchname>`
Create a branch
- `git checkout -b <branchname>`
### branch
- `git branch <new-branch-name>`
### diff <somechangeID\>
See the changes in the file at a given changeID.
you can use [[Gitk]] to track and see all changes in the file 
### remote
Set the origin and upstream repos
- `git remote -v` lists all repositories tracked
- `git remote set-url origin REMOTE-URL.git` sets the origin stream
- `git remote add origin REMOTE-URL.git` adds the origin stream
- `git remote add upstream UPSTREAM-URL.git` Where you get updates if you have forked a repo
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