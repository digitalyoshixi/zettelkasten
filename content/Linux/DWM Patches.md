---
tags:
  - linux
  - arch
  - ricing
---
following this tut:

[https://www.youtube.com/watch?v=6MaTMuFVGck](https://www.youtube.com/watch?v=6MaTMuFVGck)

  

go to dwm patches website

[https://dwm.suckless.org/patches/](https://dwm.suckless.org/patches/)

  

### Attach below

[https://dwm.suckless.org/patches/attachbelow/](https://dwm.suckless.org/patches/attachbelow/)

Whenever you spawn a new terminal, it takes up the main terminal space. We don’t want that, so we get the patch that turns any newly spawned process and put it below 1.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrj_tmp_e04fed941951842b.png)

there are 2 download options. I don’t want to use the toggleable version so just get the regular patch

  

### Useless gaps

[https://dwm.suckless.org/patches/uselessgap/](https://dwm.suckless.org/patches/uselessgap/)

Will add a bunch of useless margins between terminals

get the most recent version

  

### Always centre

[https://dwm.suckless.org/patches/alwayscenter/](https://dwm.suckless.org/patches/alwayscenter/)

Will always centre a spawned process when in floating mode

  

### Applying patches

As root.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrj_tmp_2131f405ea794383.png)

go into your dwm folder. Assuming you also have a patch folder with all the diff files directly inside the dwm folder, you apply each patch one by one like this:

patch -i patches/patchname.diff

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrj_tmp_c0e882f7dd794c9f.png)

then do a sudo make clean install

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrj_tmp_df8884d3bd55078e.png)

  

lets see if the patch worked

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrj_tmp_bff6919d7a3468dd.png)

yes it does!

  

Now, patches are not always this simple.

Most patches will always firstly patch to config.def.h. and then they will often throw some errors out. They will make a config.deh.h.rej file that shows all the errors. You will have to edit whatever file it tells you to edit(++++ filename), then edit the + lines (+ line).

Once done that, copy the config.def.h file to the config.h file to update the configuration file.

It always patches first to config.def.h because config.def.h is the template.

  

There will also often times be a dwm.c reject file too.

by catting the rej files. They will tell you what they are trying to remove and what they are trying to add

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrj_tmp_ffe0d003b0958c7d.png)

in this case they want to remove attach(c) and add 4 lines of if else statements.

Just search for that segment in vim and then remove the line and add 4 more lines.

  

No need to run the reject files again, unless you need to cross reference again.

## DWM important keybinds

[https://gist.github.com/erlendaakre/12eb90eef84a3ab81f7b531e516c9594](https://gist.github.com/erlendaakre/12eb90eef84a3ab81f7b531e516c9594)

like all of these are important, but many I will not use.

I will be using:

**MOD+ENTER –** make the current window the master window or make the master window inside the stack

**MOD+SHIFT+ENTER –** create a new terminal

**MOD+NUM –** move to the next tab

**MOD+TAB –** move to previous tab

**MOD+SHIFT+NUM –** move current window to X tab

**MOD+P –** open a app

**MOD+J/K –** move current focus left or rightmost on the stack