---
tags:
  - ctf
---
# Description

# Solution File

I dont know why there is an extra space, but it works out nicely

```python
message = "the bureau has got some very interesting projects in the works. some cool planes. cool mining operations around the globe. cool cars. cool malware. i have not been at the bureau very long and i wonder what the plan is for the future here. it seems like they are planning something big and it makes me uneasy not knowing what it is. i fear for what would happen if i got in the way. i am very confused"

alphabet = {

"a":"gtr4",

"b":"r7yrje",

"c":"gtfs5",

"d":"gt",

"e":"fr3h",

"f":"rew34",

"g":"hr",

"h":"rsjl",

"i":"gje",

"j":"fr3",

"k":"jki",

"l":"gtfs",

"m":"rew",

"n":"rxhbv",

"o":"fr3hrx",

"p":"fg4t",

"q":"rj",

"r":"fr34rs",

"s":"rts",

"t":"fr34",

"u":"fr3hrt",

"v":"4g",

"w":"gje3",

"x":"4r",

"y":"jki4",

"z":"r7y",

" ":"f53d7",

".":"234v5",

}

encoded = ""

for i in message:

encoded += alphabet[i.lower()]

  

print(encoded)

  
  
  

'''

===================

===================

Below is th function to obtain the flag, you need the original message in order to obtain it by passing it as an argument

===================

===================

'''

  

#flag with message as substitution flag key

def substitution_flag(original_message):

keys = [50, 89, 99, 121, 26, 235, 247, 166, 383, 266, 39, 282, 397, 338, 78, 141, 302]

#print('bhbureauCTF{', end='')

for sub in keys:

print(f"{sub} : {message[sub]} : {message[sub-3:sub+3]}")

#print(message[sub], end='')

#print('}')

  

substitution_flag(message)
```