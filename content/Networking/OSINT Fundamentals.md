---
tags:
  - OSINT
  - redteam
  - web
  - privacy
---
Its just some course to get you into the mindset of privacy.

[https://www.youtube.com/watch?v=qwA6MmbeGNo](https://www.youtube.com/watch?v=qwA6MmbeGNo)

the course will cover the fundamentals. Like 70-80% of OSINT methods.

Its a methodology based course, a mindset of OSINT. Tools come and go, they break, websites shut down but the mindset stays the same.

  

### The intelligence lifecycle

There are 5 parts to the intelligence lifecycle.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_13ea73b23c1a1db6.png)

there is **planning and direction**. Who, what, when, where, why? Who are we targetting, what are we targetting specifically, why are we even targetting them? When and what period?

The **collection phase** is the big one. Its the majority of the course. How do we gather image information, how do we gather metadata from an image, how do we gather information about the organization, the people in an organization?

**Processing an exploitation** is about interpreting the data.

**Analysis and production** will have you analyze the data. Saying this data point ties into this data point, and this is why. Create the report

**Dissemination and integration** is giving and communicating the report.


### Sockpuppets

A fake account, alternate identity, etc. don’t draw any attention with the sockpuppet account. Whenever we conduct OSINT, we never want our target to know there are people looking into them.

Fake person may have fake twitters, emails and they should never tie back to you, your IP address, a device that is yours, etc, etc.

  

### How to make a sockpuppet

So you can make an identity, give em a background, a occupation, awards, make him active, a real person. Or you can make an account based around a concept. Something impersonal like an organization or like [https://twitter.com/ShakiraSecurity](https://twitter.com/ShakiraSecurity). Like, nobody really makes accounts about themselves anymore anyways.

Some OSINT tools for a personal identity can be:

[https://www.fakenamegenerator.com](https://www.fakenamegenerator.com/)

[https://www.thispersondoesnotexist.com/](https://www.thispersondoesnotexist.com/)

its advised to make your personal identity female. Because men are vulnerable and women are inherently more trustworthy

[https://privacy.com/](https://privacy.com/)

privacy.com will make virtual credit cards.

Mint mobile also has hella cheap SIM cards for burner phones

Do not use the account on any other device and Do not use the account to browse things unrelated to the investigation as best you can. These things can be traced back to you. Everything can. Try to avoid as many of these pitfalls as possible and practice OPSEC.

  

### Search engine operators

Google is obviously the best if you want good results.

SearX is actually a pretty good choice for this. It aggregates results from various search engines to find the best results.

Google > Yandex > Bing/DDG > Baidu(CHINA)

so in google, I assume DDG also, but DDG has bangs.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_15269338ca52ed4b.png)

you can have site parameter. The site:url. Will only show search results that have the domain associated with the given URL.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_4bb66e8f6f216799.png)

yes it also works for DDG too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_62cd1ddfefe41d5f.png)

now, say we wanted search results to include more than 1 search term for the results. Like we ONLY want wgu AND cs958 results together, written on the same website.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_6da630f95d62a2d6.png)

you would use the AND.

Additionally, you could also use “” to combine 2. it will be less lenient than AND, but will still narrow down to have both terms on same webpage for the results

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_c904a565e931ebfa.png)

now, you can also have the OR opperator as you do AND.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_151fd1584e5b0f51.png)

but its not that good.

So, like this heath adams guy, I forgot what they call him. We can put a * for a wildcard. It will return anything between the keywords the mentor

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_a2d77c91fd37ce94.png)

  

OSINT is devestatingly overpowered. Helpdesk/service portals, anything off limits can be accessed through a smart searcher.

Lets go hack tesla.com

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_37cb9ff1dcb40ba2.png)

eh, not that good.

Lets find only PDF documents. **Filetype:pdf**

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_ad36dfe6e842e2a7.png)

62 results

lets try xlsx filetypes.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_13fab6797b2f858b.png)

tesla does not use xlsx files.

Docx?  
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_1fc7c4d71a7c0038.png)

they have 2 docx files.

And like, we can gather a lot of sensitive information like this.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_64b3e03bae8d9dfa.png)

tesla.com in general, like not specifically the website. We look for xlsx files and the keyword is pwd. We get a dovernment document

  

now, its also important to know that there are often subdomains associated with websites. Like there can be ir.tesla.com, forums.tesla.com, so on so forth. In order to view all these subdomians, we neglect flag the www

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_42a7b30a34862fd4.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_580a04254e206051.png)

we can also do this neglect flag for subdomains like forums.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_bd495a4cd2200270.png)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_50ab91c90c745fc6.png)

and so we can do the neglect flag not only for urls, but for the search result keywords too.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_2199d9916ad52e03.png)

say we don’t want to know anything about the cyber mentor for heath adams. We can neglect thecybermentor and neglect mentor and find only results correlating the him as a person

  

we can also do search results correlating to the website’s structure. In text results or in title results

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_62f64f951de859f5.png)

we can find if in the website html itself, there is any mention of password

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_84c97f8585e93ef1.png)

twitter HATES binning of isek

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_d189c845b9807e2d.png)

Inurl.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_f78a009078562254.png)

and lastly, intitle

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_c8048a2a25aeeca7.png)

now, if you cant remember these parameters. You can always use the google advanced search

[https://www.google.com/advanced_search](https://www.google.com/advanced_search)

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_b4ade73f140308f3.png)

helps you all the same

  

### Reverse image searching

You know this. Google allows you to reverse image search![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_11448e5fb77180ed.png)

you can do the same google querying.

Yandex is the best reverse image search tool though.

  

### EXIF data

Exchangable image file. Can be very telling. Can have data left behind that ties back to you. Its a bit more secure these dates, but still not secure. It can tell you the exact location, the exact device.

The site that is good for this type of stuff has now been taken down. So all thats left is alternatives.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_5083d8b0507aaec7.png)

hers using jimpl. It tells me 17.3% of the image is used by metadata. Jesus… and tells me the exact date it was created in.

jimpl is actually pretty good. It tells location and a lot more metadata.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_7cc01a5876b8c1be.png)

facebook and twitter will filter the metadata out.

  

### WHERE IN THE WORLD?

So just drop an image into google search and it will find the most accurate result it thinks the place is located at.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_7d06b37c86a1eb97.png)

  

### Pimeyes

In 2006, there was a hunt for Satoshi. [https://findsatoshi.com/](https://findsatoshi.com/)

The dude was found using pimeyes. [https://pimeyes.com/en](https://pimeyes.com/en)

shows a lot of porn results, but that is like 90% of the internet anyways. It tries to blur anything else other than the face. The free version will not allow you to enter the website aswell. You need 16 euros to view the current result, and 25 euros a month for a membership to view 25 results. Fair, I guess, its a good product.

Now, they cant crawl on social media, because social medias, the big ones have methods to throttle crawling on their websites. Thats why whenever you waybackmachine some reddit post, it usually tells you to GO MAKE A ACCOUNT or just takes a really dang long time.

  

### Discovering email addresses

There are several tools

Lets use hunter.io it gives 50-100 free searches per month.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_1d255bfc9ef37130.png)

they find it via pattern of emails.

[https://hunter.io/search/](https://hunter.io/search/)

above was just the trial version. If you make a free account, you are able to actually see the people.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_e0070ecad049127b.png)

theres also phonebook.cz

[https://phonebook.cz/](https://phonebook.cz/)

a way more simpler website. Requires an account but otherwise the service is completely 100% free.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_fd418ad3cdc2aa4.png)

actually intelligenceX has a lot more sweet products aswell. You can browse databases from simple search terms, view all files associated with a website and more.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_8852fa3232520a1e.png)

do you remember this? Man goatse emails are so damn cool!

Email hippo is how you can verify the email

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_16e87bb6692b7560.png)

you don’t need to even email, if you don’t want to interact with the person, just check if the email is correct.

Also, you can just try to log in.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_d356387fc89628d0.png)

like on google, if you get the username correct, it will tell you. Welcome!

Also, forgot password can link you to other accounts.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_cead39166baff3e9.png)

[h****@tc](mailto:h****@tc)*****.com.

Hm… the tc****.com seems like it belongs to a uncommon domain.

Say if you found a breached database with either of those email addresses, it only takes the weakest link. This user’s email is taken, gives the attacker the ability to access more emails.

  

### Password OSINT

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_1bcab630b4bc24dd.png)

lol

above is the tesla databreach. Its old, the user’s probably all quit or are dead or changed their password. Who knows?

There used to be a website called weleakinfo.io, but it got seized by the FBI. Damn alphabet boys.

Now, we get the shitty alternative called dehashed. [https://dehashed.com/](https://dehashed.com/)

you need to pay, unfortunately.

I don’t have an account, im not at that point where I need to pay for any service. There are always alternatives, or just don’t.

Got a database from 3 years ago. Before raidforumns shut down: [https://www.mediafire.com/file/tehm7a7sp7o8rgo/raidforums-hiddencontent.json/file](https://www.mediafire.com/file/tehm7a7sp7o8rgo/raidforums-hiddencontent.json/file)

  

### Scylla

Depreciated. Unfortunately. It used to be the masterclass. You get ALL THE DATA with scylla. Scylla comes prebundled with kali linux. Github too so you don’t have to worry about it being taken down. [https://github.com/scylladb](https://github.com/scylladb)

BUT. Nobody works with it anymore, and by OSINT standards, it is punk.

  

The idea is, there is so much information we can gather from these breached databases, you just need to connect the dots. There is really, really good information out there.

  

### Hunting usernames and accounts

So we can from a single username, find multiple other accounts the user may have. Like on websites like pintrest, quora, reddit with the same alias.

We can use namechk to see what websites a username is registered on. The popular websites that is. Green is unregisted, red is registered. The normal use of this website is to see if you are able to register, but us OSINTers use it to check for registered users.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_62e69b750d5f8bca.png)

so, im not on tiktok or slack, and the Yoshixi on github is also not me. There are a lot of red herings which I am glad for. There is a person who uses my exact online alias to protect me so im glad.

Also there is this website:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_4b2b28e0af08b494.png)

this one is the better of the 2. its always the second one he recommends which is the better one.

Also, the brute force method. Go to any website that you think a user alias is registed on, then you can try it on the website itself. It will tell you. Valid user? Not valid?

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_b389d94a68dfa78a.png)

  

### Networks

We can find people and use those people to find more people. Whitepages is the solution but its US-based only

they only allow US citizens to see the full info and also they require premium to see criminal records.

This site is actually quite bad, because it is afterall US based and for Hiring managers. Not for OSINTers, yet what little info we can extract, we can use.

Knowing address based off name is OP.

[https://thatsthem.com/](https://thatsthem.com/) thats them is another incredible tool. Give them a phone number, name, IP address, they will have the information. Thats them however, is just a frontend for spokeo and spokeo is a US based company. Nothing great at all man…

  

### Voter records

Voter records, like who doesn’t vote? [http://voterrecords.com/](http://voterrecords.com/)

Its US only, but you get a hell of a lot information

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_1fc0f6e732a1b7f8.png)

jesus… school, housing district, political party…

  

### Phone numbers

Not too special, just google search the phone numbers. Whats interesting is that certain craigslist vendors will go with the tactic of writing our their phone number with characters. Like “nine four nine – seven three six – five five two five” in order to prevent being picked up by webcrawlers and being called by scam services. So thats a tactic to find phone numbers, very niche case though. Emojis too may work.

Now, truecaller is a great service. It requires people to register on it and once they do, all their contacts are pulled. This is how it looks up callerid from a phone number.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_a694eb4bf42f2095.png)

NOTE: DO NOT LOG IN TO TRUE CALLER WITH YOUR OWN PHONE. YOU WILL LEAK YOUR CONTACTS TO THE INTERNET!!!

eek.

One phone number can lead to another. Like if you forgot password, then you will be able to provide phone number like for yahoo ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_ce20337e92d10844.png)

yahoo sucks with their privacy.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_aa7b9684e2b9433f.png)

it gave the FULL domain name. Like its blurred out in the picture, but it has the full fucking domain.

[https://use.infobelpro.com/Search/Basic](https://use.infobelpro.com/Search/Basic)

infobel is also an option. It has a rather lackluster database, but it is good for finding companies I guess?

  

### Birthdays

We leverage google chrome advanced search again

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_5a4ea45f28758a15.png)

pretty damn good way to find birthdays.

Nothing new, just excercises

  

### Resumes

I put 90% of myself on my resume, there is SO much personal information on a resume. Probably the WORST thing to give someone if you are worried about privacy. Google search and find images. Always usually pdf,png,jpg,doc.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_ed6b2736a7f6f162.png)

something really broken is to search on google domains. Especially drive domains

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivyj_tmp_18f1b03f5488aff4.png)

like docs.google.com, or just drive.google.com

dropbox.com, scribd.com.

And of course LINKEDIN . COM