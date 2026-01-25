---
tags:
  - security
---
Free online hacking resources provided by the university of arizona.
# Starting challenges
1. Select the `Start` on challenge. ![[PwnCollege-20231218005651958.webp]]
2. Go to urls: 
	1. https://pwn.college/workspace/vscode
	2. https://pwn.college/workspace/desktop
3. In the desktop, open terminal, type in `~/challenge/run`
4. Solving challenges will give you a flag. Flag can be like: `pwn.college{otwGof-ZqGfaBxHbcDceYxk4R0s.dhjNyMDL0AjMzQzW}`

Additionally, you can solve the challenges on your own machine, but you will have to ssh into them.
# SSH Into Challenges
1. [[OpenSSH Keygen]] and then store the values of the `key.pub` file into your pwncollege account.
2. `ssh -i key hacker@dojo.pwn.college`
3. Navigate to the `/challenge` directory
4. Flag is always located at `/flag`