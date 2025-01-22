---
tags:
  - web
---
A [[Static Site Generator|SSG]]
# Setup
1. `sudo pacman -S ruby`
2. Add `/home/yoshixi/.local/share/gem/ruby/3.3.0/bin` to [[Linux PATH]]
3. `sudo gem update --system`
4. edit `~/.zshrc` or `~/.bashrc`
```
export GEM_HOME="$HOME/.gem"
export PATH="$HOME/.gem/bin:$PATH"
```
5. `gem install bundler erm jekyll`
6. `jekyll new my-awesome-site`
7. `cd my-awesome-site`
8. `bundle add erb`
9. `bundle add webrick`
10. `bundle`
11. `bundle exec jekyll serve`

# Basic Boilerplate Rundown
![[Jekyll-20241119212710784.webp]]
### \_site
the final website. Do not modify and files in here
### \_config.yml
A configuration file for the sites data. Used as shared variables for other pages to use
### Gemfile
Used to store ruby dependencies for the website
# Concepts
- [[Jekyll Frontmatter]]
- [[Jekyll Themes]]
- [[Jekyll Layout]]
- [[Github Pages]]
- [[Jekyll Clean Site]]