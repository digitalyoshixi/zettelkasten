---
tags:
  - os
  - security
  - malware
  - networking
  - windows
---
I have downloaded a program to view file changes. I am hoping to use it currently to monitor what files are changed from what processes for tasks like installing new apps and seeing where the stuff is installed to, checking what happens when I pip install a python library, all this behavioral stuff saved as logs by procmon. The issue is, procmon is not intuitive, actually, its a rather difficult piece of software that monitors the whole friggin OS.

Its used by malware analysts and IT professionals and something I am acutally willing to seek out and use so I am very happy with it

  

Right, so I am going to disable some processes that make too many logs. Going to add it to a blacklist so that I never have to see their logs again. They are routine processes that I know for sure im not going to care for too much. Procmon for me right now is pure utility, I want to see where files are downloaded. If I am to analyze malware behavior, I want to capture everything and plop it into Procdot to visualize, but im not using it for malware at the moment, so I set it up purely for utility OK?

If I wanted a malware behavior procdot, I would set it up on my VM where I can acutally capture shit without breaking my own computer.

When im done I want to export my procdot configuration.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_659718633a3f02c9.png)

so that I can just have this utility configuration whenever I need it.

  

### Few key buttons

[https://www.youtube.com/watch?v=5FMpfk8knNQ](https://www.youtube.com/watch?v=5FMpfk8knNQ)

**capture button:**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_68763f9c679c5c0e.png)

by default it autocaptures. Disable this if you want to manually capture.

  

**Autoscroll:**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_b1988426cf4e2e60.png)

goes to the most recent logs automatically. Also a flag/option you can turn on and off.

  

**Clear logs:**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_aaa9a08cfc61e9f4.png)

the bin, you just clear all your logs.’

  

**Filter:**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_324abaa97ae80c7a.png)

your filtered blacklist and whitelist(i believe there is a whitelist)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_4ddb999900456b77.png)

you can add a process manually, or right click a process log and exclude to add to blacklist or include to add to whitelist.

  

**Tree:**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_ce711786831104cb.png)

some of the many bullshit a programmer has to deal with daily

its a process tree. So you can see all the processes currently running like task manager, and then also blacklist or whitelist a process

  

### Programs blacklisted

Lets blacklist some processes I find that IDK what they do.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_ea9416cb24cac26f.png)

TPOSD.Exe is a thinkpad exclusive.

[https://www.reddit.com/r/thinkpad/comments/qij15e/can_someone_explain_the_on_screen_display_drawer/](https://www.reddit.com/r/thinkpad/comments/qij15e/can_someone_explain_the_on_screen_display_drawer/)

I believe its for displaying certain lock keys. Like if you accidently enable caps lock, there will be a quick UI to tell you, CAPS LOCK ON!!

or FNLOCK ON!!!

you know what, this might be a good process to hijack since I am not thinking twice about blocking the procmon logs. And also, it only occurs upon key press like caps lock and such.

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_5f9a4ab5d03a5a32.png)

SearchIndexer is a microsoft daemon process.

Search indexer is the thing that powers the search feature in this OS. Whenever you search for something in your searchbar at the bottom left, or your file explorer, you will use the windows search service.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_fd204f5cd6e93abc.png)

  

**Runtime broker**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_7c12c60cf47d17ae.png)

this is another windows daemon process

[https://www.howtogeek.com/268240/what-is-runtime-broker-and-why-is-it-running-on-my-pc/](https://www.howtogeek.com/268240/what-is-runtime-broker-and-why-is-it-running-on-my-pc/)

it manages permissions of apps. Like gives some apps access to microphone, location.

GREAT GREAT for malware analysis, bad for me casually.

It goes into the blacklist.

  

### Screen clipping

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_119bed0c5234ee4.png)

self explanatory right? This is snipping tool!!!! I LOVE SNIPPING TOOL AND SNIP AND SKETCH TOO!!!!! WIN+SHIFT+S FTW.

Blacklist it goes.

  

Uhmm, oops, I don’t think I was meant to blacklist this much processes.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_3a74852251c62d6c.png)

procmon was not meant to blacklist all these processes. Don’t use procman like a retard.

  

### Process whitelist. Single process logger

I mentioned before there was a whitelist, in order to do a whitelist, well I only know how to whitelist one at this moment, but whitelisting 2 should be no trouble.

Go to tree while procmon is still capturing

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_ce711786831104cb.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_f7399271ae6a9c3c.png)

if you open tree without capturing, then it wont be able to show all these processes, and then it will crash if you click on any button. Super annoying.

Say I only wanted to monitor firefox.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_9b11800ab62b2092.png)

I would rightclick the process and then add it to my include filter.

Now its all firefox

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_2e889e35a06dc23.png)

you may also see that the operations differ in nature

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_51b627e2d14f7351.png)

some are relating to files, some are relating to registrys.

To filter which ones you want, just edit these:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_1a8463636668e60a.png)

and personally, I don’t care about network or profile. Files and registrys are the big ones, program behavior also matters a bit I guess.

I find a log that firefox is creating a file.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_ccce762be9a6d7ca.png)

double click that log, and then we can see the info of that created file.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_5eed8a41668aab95.png)

the whole path is: C:\Users\Digit\AppData\Roaming\Mozilla\Firefox\Profiles\gn6a2f0v.default-release\storage\default\https+++[www.youtube.com](http://www.youtube.com/)\idb\2460537361L7o7g6s4D5a2t8a7b6a6s.sqlite-shm

I believe it maybe is caching this page so that If loaded again, I can easily rewatch.

I also see the OpenResult, It didn’t write anything, it just opened it. What is it doing, hmm??? I wonder, is it reading????

if it acutally wrote something, it would have had openresult be OverWritten or Written or some shit like that

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_a8700874df99b429.png)

you cant see the data that it wrote unfortunately.

To reset the filter, just reset the filter bruh

or if you don’t want to reset the entire filter, just uncheck your filtered things

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iw2r_tmp_b9374ecb9f3bb5bf.png)