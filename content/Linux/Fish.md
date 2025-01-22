---
tags:
  - linux
  - os
---
[https://wiki.archlinux.org/title/Fish](https://wiki.archlinux.org/title/Fish)

My favorite. Simple, has a lot of great features from the get-go

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsa_tmp_6b7cee9536228036.png)

not too great on the eyes, but lets give it a try anyways. If I don’t like it, we go to zsh.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsa_tmp_cf3fa1d5ffd19603.png)

then just type fish

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsa_tmp_68117e3b58694fd4.png)

and look, it has autocomplete showed

to set fish as the default shell, first find the fish directory.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsa_tmp_a3416979442e101f.png)

for me it is /usr/bin/fish

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsa_tmp_a3776d74b2743ad9.png)

then I type chsh -s /usr/bin/fish

  

reboot and then you will see the new shell

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsa_tmp_2f6962ec9428928f.png)

pretty nice.

You can also use tab to autocomplete/search for autocomplete. Great features

but.. fish is not [[POSIX]] compliant

## Fish plugins

Download fisher which is just for quality of life, it is the main repository for fish plugins.

[https://github.com/jorgebucaran/fisher](https://github.com/jorgebucaran/fisher)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_8477f532370312ed.png)

use fisher list to list all currently installed plugins.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_12ae440439f47470.png)

at the moment I have none.

Lets learn to zest up fish.

This: [https://github.com/jorgebucaran/awsm.fish#readme](https://github.com/jorgebucaran/awsm.fish#readme)

is a fuckin goldmine.

It has plugins, prompts, and community links all inside of it.

### Themes

Tide is how we get fish themes. It is a plugin for fish that we can get with fisher

[https://github.com/IlanCosman/tide](https://github.com/IlanCosman/tide)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_857f90c486e2b788.png)

then we configure our prompt.

I don’t like zsh styles. I will go with lean. I LOVE LEAN

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_a2ff64e6e44ec347.png)

then prompt colors

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_666ca91446ebaae1.png)

il try 2 for now, if I don’t like it il idk remove the tide and reinstall.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_4d83796f05c1f055.png)

no current time.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_1f6ecc3e9a97fb1d.png)

one line please

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_34c697a7c90ae750.png)

lets do sparse actually, give it new flavour

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_9d340a1de4f3f613.png)

many Icons. We will get icons later.

Then I press Y and we have our new tide

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivso_tmp_a2a2fb740acbd734.png)

this is beautiful.

[[Font Awesome]] will allow you to get the icons

### FZF

[https://github.com/patrickf1/fzf.fish](https://github.com/patrickf1/fzf.fish)

makes finding things in fish easier. Has a little display for things too.

firstly, install these with pacman

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsz_tmp_999acc2184b7f608.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsz_tmp_ca1bf57c44228bb2.png)

  

**CTRL+ALT+F –** Find a file

**CTRL+ALT+P –** search for a process

**CTRL+V –** search for a variable. Doesn’t include all of them

## Fish configuration

I, ok, I wanted to add something cool but I failed so but I still added something cool that I didn’t want to add in the first place but I might need so it is this:

CTRL+BCKSPACE delete the entire line in terminal. I wanted it to delete a single string seperated by whitespace, but it deletes the whole line. Still handy to have.

Put this line in your `~/.config/fish/config.fish`

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivsz_tmp_133c7d8c95fe266a.png)