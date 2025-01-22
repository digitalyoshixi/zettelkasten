---
tags:
  - privacy
  - firefox
  - security
---
## Firefox hardening

This video: [https://www.youtube.com/watch?v=Fr8UFJzpNls](https://www.youtube.com/watch?v=Fr8UFJzpNls)

DOES FIREFOX CARE ABOUT MY PRIVACY??? NO! HELL NO!

about:telemetry

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_50e1d50d0638335e.png)

firefox collects all your interactions with the UI. They want to improve their browser, but I don’t want to improve their browser.

They are sending google analytics on their firefox addons store.

To change a lot of the annoying settings like pocket, and built in adds for pocket, you could go to about:config.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_205da9248f4a394.png)

and manually configure each setting you want

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_997e378aa190184b.png)

but, that would take tooooooo long to do 1 by 1. so instead, we have a user.js file that will change our preferences for us.

  

### User.js

We will use a js file which holds our user preferences. We have several templates to choose from. Betterfox, arkenfox and narsil’s userjs.

Betterfox will be the best for those that don’t want to break many websites while still limiting telemetry

arkenfox is some good default privacy features

narsil’s user js is 99% isolated from mozilla, no data is sent back.

Lets use better firefox. [https://github.com/yokoffing/BetterFox](https://github.com/yokoffing/BetterFox)

I get the js

[https://raw.githubusercontent.com/yokoffing/Betterfox/main/user.js](https://raw.githubusercontent.com/yokoffing/Betterfox/main/user.js)

then I want to add a patch to the user.js

  

### User.js patching

It has a few common patches it allows us to do. Lets do that

[https://github.com/yokoffing/Betterfox/wiki/Common-Overrides](https://github.com/yokoffing/Betterfox/wiki/Common-Overrides)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_bcc8b5de80f07d57.png)

edit your user.js file and locate the segment which allows for patching

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_43906c8f946f3177.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_57ebd54f401a230f.png)

  

### Applying the aid

ok, now before I add the js, I will make it a new profile.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_d4cf65d32422904e.png)

new profile

and then open the root directory

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_8907a7e508769c51.png)

then drag your user.js file inside the root folder

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw3y_tmp_82b7a227c8c9b5b8.png)

and we are done. Set your new brower as the default profile in your about:profiles and betterfox is now setup. Make DDG the default search, and adjust a bit, relogin to all your accounts.