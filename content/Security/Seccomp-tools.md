---
tags:
  - binary_exploitation
---
A group of tools to analyze and bypass sandboxes.
https://github.com/david942j/seccomp-tools
# Installation
Requires [[Ruby]]
`sudo pacman -S ruby`
Then install with gem.
`gem install seccomp-tools`

Set gem tools to be in path.
```ruby
export GEM_HOME="$(ruby -e 'puts Gem.user_dir')"
export PATH="$PATH:$GEM_HOME/bin"
```
Now you can run `seccomp-tools`
![[Seccomp-tools-20240701045638321.webp|564]]
