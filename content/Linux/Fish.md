---
tags:
  - linux
  - os
---
[https://wiki.archlinux.org/title/Fish](https://wiki.archlinux.org/title/Fish)
My favorite. Simple, has a lot of great features from the get-go
Fish is not [[POSIX]] compliant
### Fish plugins
Download fisher which is just for quality of life, it is the main repository for fish plugins.
[https://github.com/jorgebucaran/fisher](https://github.com/jorgebucaran/fisher)

use fisher list to list all currently installed plugins.
This: [https://github.com/jorgebucaran/awsm.fish#readme](https://github.com/jorgebucaran/awsm.fish#readme)
### Themes
Tide is how we get fish themes. It is a plugin for fish that we can get with fisher
[https://github.com/IlanCosman/tide](https://github.com/IlanCosman/tide)
### FZF
[https://github.com/patrickf1/fzf.fish](https://github.com/patrickf1/fzf.fish)
makes finding things in fish easier. Has a little display for things too.

**CTRL+ALT+F –** Find a file

**CTRL+ALT+P –** search for a process

**CTRL+V –** search for a variable. Doesn’t include all of them

## Fish configuration

I, ok, I wanted to add something cool but I failed so but I still added something cool that I didn’t want to add in the first place but I might need so it is this:

CTRL+BCKSPACE delete the entire line in terminal. I wanted it to delete a single string seperated by whitespace, but it deletes the whole line. Still handy to have.

Put this line in your `~/.config/fish/config.fish`

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsz_tmp_133c7d8c95fe266a.png)