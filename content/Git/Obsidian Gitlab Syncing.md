---
tags:
  - obsidian
  - gitlab
  - synchronization
---
# Setup Token
![[Obsidian Gitlab Syncing-20240203011229153.webp|244]]
Preferences
![[Obsidian Gitlab Syncing-20240203011250370.webp]]
Access tokens
![[Obsidian Gitlab Syncing-20240203011456098.webp]]
Add new token
Be sure to copy it and save it once you get it. You will never see it again.

# Git Setup
https://andrewwegner.com/obsidian-gitlab-setup.html
1. cd into your obsidian note folder
2. Make a `.gitignore` file with the following data:
```
.obsidian/*
!.obsidian/app.json
!.obsidian/appearance.json
!.obsidian/config
!.obsidian/community-plugins.json
!.obsidian/core-plugins.json
!.obsidian/graph.json
!.obsidian/hotkeys.json
```
3. Initialize repository like such:
```
git init --initial-branch=main
`git remote add origin https://gitlab.com/Yoshixi/calculus12-notes.git`
git remote set-url origin https://<username>:<token>@gitlab.com/Yoshixi/reponame
git add .
git commit -m "Initial Commit"
git push --set-upstream origin main
```
### Troubleshooting
If you cannot git push, then try:
`git pull origin main --allow-unrelated-histories`
and then push.
# Obsidian Git Plugin
Be sure to install the `Git` plugin
![[Obsidian Gitlab Syncing-20240203011821823.webp]]
Setup Vault backup intervals
![[Obsidian Gitlab Syncing-20240203011842392.webp]]
And the commit author too.
![[Obsidian Gitlab Syncing-20240203011904184.webp]]