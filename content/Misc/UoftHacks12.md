---
tags:
  - hackathons
---
# Before Hacking
1. The guy I was planning to build with dipped
2. Met 3 ppl. took so long to find the last member, its so weird most ppl are in teams of 3/4, hard to find others that are indivudual. Admittedly, I was finding people in person, searching online wouldve been easier I suppose
   ![[UoftHacks12-20250117235037088.webp]]
3. The prize tracks are as follows:
- RBC Tech (Best Security Threats) - 1000 dollars
- Databricks (Best use) - Legos, was told that databricks is adopted in [[Sci-kit Learn]] and [[Terraform]]
- [[Terraform]] (Best use) - Mech board
- [[Auth0]] (Best use) - Something
1. We are told that:
- Demo video (2-5min) for showcasing demo of the app
- Pitch (2-5min) for pitching the app
# Session Notes
### Intro Session
- Erin tells us to learn [[Git]], [[DevOps]]
- Being memorable is more important than being the smartest in the room
### Milos RBC Cybersecurity
He talks about the challenges we face in the cyber landscape
He is a red-teamer.
- [[Modern Cyber Threat Landscape]]

Milos tell us to focus on mobile app data management

![[UoftHacks12-20250118040125262.webp]]

# During Build
- Roles are established and I am working on twilioo
- I have to create a system that can call and recieve calls
- I make 3 free twilio accounts
- The function to call is very straightforwards
- The function to recieve requires twillio to watch post requests for a site and then return the response given by a POST requets's XML response
- The way to establish communication is to use a Connection and Stream tag
	- I spent very long trying to setup the webhook link to be accurate with [[Amazon Web Services|AWS]], it ended up being a lot easier to just [[ngrok]] to setup a tunnel on the public internet
	- I did not figure out how to get recording the conversation to work, we could record the [[muval]] data, but could not decode property, I could not find a way to decode, i tried [[AssemblyAI]] and [[Vox]]
- Worked on frontend a bit, added a [[Progressive Web App|PWA]] [[Agent]], but it does not appear to work in full
- Looked back at twilio: https://github.com/MarcosSan4/realtime-twilio-outbound/blob/main/main.py 
- 