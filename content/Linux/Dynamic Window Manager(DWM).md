---
tags:
  - arch
  - linux
  - ricing
---

DWM is a dynamic Window Manager

## Dwm setup

[https://wiki.archlinux.org/title/Dwm](https://wiki.archlinux.org/title/Dwm)

You configure dwm by copying its config.def.h file to config.h

I copy this guide:

[https://stackoverflow.com/questions/31275672/how-to-install-dwm-in-arch-linux](https://stackoverflow.com/questions/31275672/how-to-install-dwm-in-arch-linux)

### my git fork

First thing I want to to is make a fork of dwm so I can customize it myself. It will go on my github.

  

What I need is:

```
git clone git://git.suckless.org/dwm
```

Dwm is the main window manager

st is the simple terminal

dmenu is the menu for a lot of items. I think it Is the top menu with firefox and all that not too sure but its essential

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivr1_tmp_c50a3fc79a8e60e4.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivr1_tmp_3703a24f74f7e9d7.png)

_and I didn’t take a screenshot of dmenu but it is created aswell_

  

### config setup

do some configurations of your configs in vscodium

I clone my first dwm repo inside vscodium

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivr1_tmp_4e0f13da2f3fbaa5.png)

[https://dwm.suckless.org/customisation/](https://dwm.suckless.org/customisation/)

dwm is configured at compile-time by editing some of its source files, specifically `config.h`

`config.def.h` is the one we want to edit first, because it has comments in it that help us.

This is config.def.h:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivr1_tmp_69118ffc3eb5dd52.png)

the source code doesn’t come with a config.h, we will copy the config.def.h to config.h when we are done configuring

don’t really need to edit config.mk. Its to help with the make file, but we will just install default after we configure config.def.h

  

you have a few things you can change:

1. **keybindings**. Keybindings for launching windows, moving windows, etc.
    
2. **colors and appearance**. Adjust colors, fonts, borders, text colors
    
3. **bars and status**. what you want the status bar to show. CPU? RAM usage? You usually find 3rd party patches to do this.
    
4. **Layouts.** Window behavior, how they are tiled, aranged, floating
    
5. **Rules**. Always open a certain application, and idk
    
6. **Default applications.** What u use as text editor and shit
    

  

### Installing fonts

[https://wiki.archlinux.org/title/Fonts](https://wiki.archlinux.org/title/Fonts)

for all users to have the same font selection, put fonts in this directory:

`/usr/local/share/fonts/`

baby

you may need to make the directory first.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivr1_tmp_b45b3bac38053e7d.png)

I want these fonts:

[https://sourcefoundry.org/hack/](https://sourcefoundry.org/hack/)

[https://typeof.net/Iosevka/](https://typeof.net/Iosevka/)

  

_I didn’t actually install any_

  

  

### Arch linux compiling

then follow this guide:

```
https://stackoverflow.com/questions/31275672/how-to-install-dwm-in-arch-linux 
```

`and then go to home/``david` `directory and then vim .xinitrc`

`write exec dwm then :wq`

`finally type startx`

  

`it is all black right now, but this is the default dwm`

`![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivr1_tmp_e2eb7341f5a19bf7.png)`

  

## **Virtualbox guest additions**

Things are getting fucked!

This is a virtual machine and I cant copy and paste in it.

[https://wiki.archlinux.org/title/VirtualBox/Install_Arch_Linux_as_a_guest](https://wiki.archlinux.org/title/VirtualBox/Install_Arch_Linux_as_a_guest)

so go into root

run the pacman -S [virtualbox-guest-utils](https://archlinux.org/packages/?name=virtualbox-guest-utils)

den, `rcvboxadd setup`

then, this is the important step. Pacman update the guest and then update your virtualbox version on your host machine to the most recent version. the bugfix versions don’t matter like 7.08 → 7.0.10 no need. Its the slightly larger jumps in version like 7.0.0 → 7.1.0 that matter.

then type:

VBoxClient-all

  

also there is this service:

systemctl start vboxservice

does some cool things I guess.

  

Now put that VboxClient-all in the .xinitrc before anything else.

feel free to include a bg [[feh]]


## DWM important files

A quick primer on the important files to keep note of in dwm.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivrh_tmp_b52ca5955ec8f776.png)

**config.def.h:** this is a header file which is essentially a copy of config.h. just kept incase you need to revert back to the original config.h

**config.h:** this is a header file which is all the customization, coloring, of dwm

**dwm.c:** the main file that makes dwm

# [[DWM Patches]]
apply some patches you swine