---
tags:
  - reverse_engineering
  - ctf
---
We are given this program that will output a midi file given a stream of arguments

# Installing MIDI Player
I plan to start making MIDI music soon, so I got a full DAW.
the Ardour DAW was a free DAW for linux that was pretty alright.
![[SwampCTF2025 Midigen-20250330040641672.webp]]
This is it loaded inside the DAW, we can play it,
and it sounds pretty shit.
# Recon
![[SwampCTF2025 Midigen-20250330040811368.webp]]
We see that this file will have different arguments, that will do as it says. It will create a file called `audio.midi` t
![[SwampCTF2025 Midigen-20250330040907776.webp]]
It will create a midi file regardless of what we do. This is apparent as strace will just run until completion
![[SwampCTF2025 Midigen-20250330041120311.webp]]
No libraries, so ltrace gives nothing.