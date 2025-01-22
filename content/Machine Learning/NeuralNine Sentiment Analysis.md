---
tags:
  - machine_learning
  - machine_learning
  - NeuralNine
  - neural_networks
  - python
---

don’t really see the need to do this. I mean we are using another library and the code is just like 9 lines long.

But I suppose I can delve deep into the library to truly discover, I guess.

[https://www.youtube.com/watch?v=tXuvh5_Xyrw&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=4](https://www.youtube.com/watch?v=tXuvh5_Xyrw&list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-&index=4)

### Setup

You will want to install **nltk** (natural language tool kit) from pip

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_d3dcbda93fdd3bca.png)

and also install **textblob**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_6dad9db316165f58.png)

and lastly, install **newspaper3k**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_cd032be3c5e16a14.png)

  

this is what we import for our script:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_aae74d334398556.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_a08fff2726ef3066.png)

we want to import nltk and nltk.download(‘punkt’) and just run that once, you should be good to continue the code now.

and then we want to grab our article from the internet.

The result we get from the article will be a value from -1 – 1. -1 meaning a negative emotion like hateful, angry, despair, 0 being completely neutral and 1 being upbeat, positive and gleeful.

We pick a wikipedia article which is very tone-neutral

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_98fed4fbbd69b4c3.png)

then we prepare it for natural language processing. Download the html page, take the raw html, and prepare nlp.

  

### Summarizing

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_691a0f5f5f0f3bea.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_eb5843dfe880d326.png)

now, look how long that text is.

Lets summarize it.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_1147cacc332492e.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_d05dfc41d4f14a2b.png)

the summary we get is quite dull. I believe the AI is searching for general terms like ‘in general’, ‘oftentimes’, ‘many’. Its not really a summary.

The text is all from the article. The webcrawler denotes where it is found(what # div it is I believe)

  

### Getting sentiment

We make a textblob, then we grab the sentiment from blob.sentiment.polarity

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_8f7da0d47c18ab39.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_e151789c34a31ced.png)

0.14. more positive than negative, still pretty neutral

  

I want to try to get a sentiment from a forumn post

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_fef8884a74417be7.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_27ea2b52a64db453.png)

  

I can also give it my own text

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_5335c0eaa5985448.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_5c6dfd541f3b2b4f.png)

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_63d6cdffc92e548f.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_5ae20681ed50084c.png)

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_9ce4ec6e33320001.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_49fd0a2cbec250fe.png)

  

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_fe750b8d8ce2292.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_29fdb32aec91bb15.png)

  

### File reading

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_21887b5cc22696f7.png)

same sorta deal, just get the text from a file.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_f3d55deee8f5b0a9.png)

now I want you to notice how god-awful the AI performs. I need to add a >:( to signify anger. BRUH!

  

I believe the algorithm is not so good because it is not actually neural network, it is just a simple AI which scans for words like good(+0.25), bad(-0.25), >:((-0.75), :D(+1)

  

### Other textblob features

This is not included in the video, it is on readthedocs.io [https://textblob.readthedocs.io/en/latest/quickstart.html#quickstart](https://textblob.readthedocs.io/en/latest/quickstart.html#quickstart)

  

**Subjectivity**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_e8a243ff5dcc81d5.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_b177d850863fafe1.png)

  

**sentence correction**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_8dd1eabc4fbce487.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivux_tmp_ea9a0a7b0d2644af.png)

  

textblob is a piece of shit