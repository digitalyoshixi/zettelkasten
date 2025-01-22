---
tags:
  - ctf
  - web
---
# Challenge
![[ImaginaryCTF 2024 journal-20240722162438202.webp]]
https://cybersharing.net/s/6f429753e4ae6d3c
http://journal.chal.imaginaryctf.org/
### Recon
![[ImaginaryCTF 2024 journal-20240722162528976.webp]]
A docker instance is created where a flag with a random name is stored at the root directory
![[ImaginaryCTF 2024 journal-20240722162552880.webp]]
The PHP back end states that the filename in the URL, if it contains `..`, then it will be deemed an invalid file.
# Solution
To circumvent the `..` assertion, and perform the local file inclusion, the exploit is this:
[https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp#rce-via-assert](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp#rce-via-assert "https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp#rce-via-assert")
You can run a php function if you make the filename:
`'.phpfunction.'`
![[ImaginaryCTF 2024 journal-20240722162748462.webp]]
![[ImaginaryCTF 2024 journal-20240722162753931.webp]]