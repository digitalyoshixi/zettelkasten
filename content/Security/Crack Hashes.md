---
tags:
  - redteam
  - cryptography
---
Say we grab a hash value of a user’s encrypted file. We are taught that hashes are irreversible, this is true for the most part. It would take an ungodly amount of time to sift through all prime multiples of the hash, but tools like hashcat can crack these hashes if given enough time.

The first thing we must do is grab the hashid of a hash. Hash analyzer is a built-in tool in kali linux that returns a bunch of possible hashing algorithms a hash might have. 5f4dcc3b5aa765d61d8327deb882cf99 is my hash. To use follow these steps:

1. Hash-identifier
    
2. 5f4dcc3b5aa765d61d8327deb882cf99
    

Look for the segment: Possible Hashs:. The first one will be the most likely hash.

Now we go into hashcat. Type: hashcat -h | grep [algorithm]

We get a list of numbers. Pick the one that is raw. This is our algorithm number

Then, create a file with ONLY the hash inside. I made a txt using echo ‘5f4dcc3b5aa765d61d8327deb882cf99’ > hesh.txt

Finally, type this last command: hashcat -m [algorithm number] [filename.txt] /usr/share/wordlists/rockyou.txt