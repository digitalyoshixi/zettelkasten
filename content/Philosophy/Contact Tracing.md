---
tags:
  - biology
---
A solution to track the flow of infectious diseases.

It is the process of identifying and managing people who are exposed by a disease to prevent further transmission.
# Possible Implementation
### Centralized Server Tracking
1. Track the location of people and the time that they are at the location
2. Establish links between people depending on location and time
##### Issues
- Able to identify patterns of people not-intended
### Peer-to-Peer Tracking
1. Bluetooth app pings other devices and saves the nearby devices IDs into local storage
2. End of the day, the local storage is saved onto a centralized server
3. Past day's logs are deletes
##### Issues
- Unable to identify super spreaders