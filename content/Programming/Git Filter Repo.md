---
tags:
  - git
aliases:
  - Git Removing Sensitive Information
  - Git Removing API Keys
---
A tool to remove [[Application Program Interface|API]] keys within a github repo by overwriting history.
Requires everybody who's cloned to repo to re-clone, so that they don't keep the old history.
# Usage
1. `git clone https://github.com/newren/git-filter-repo.git`
2. `chmod +x ./git-filter-repo/git-filter-repo`
3. `./git-filter-repo/git-filter-repo --sensitive-data-removal --invert-paths --path src/google-services.json --force`
4. Check affected branches `grep -c '^refs/pull/.*/head$' .git/filter-repo/changed-refs`
5. If there is no affected branches, then push these changes `git push --force --mirror origin`