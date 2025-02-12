---
tags:
  - windows
  - ricing
---
Pimp up your terminal. https://ohmyposh.dev/docs/installation/windows
1. download Windows Terminal https://github.com/microsoft/terminal
2. Download the meslo nerd font https://ohmyposh.dev/docs/installation/fonts
3. `winget install JanDeDobbeleer.OhMyPosh -s winget`
4. Find you favorite theme in `ls C:\Users\Digit\AppData\Local\Programs\oh-my-posh\themes\`
5. Set oh-my-posh to init everytime powershell is opened. https://ohmyposh.dev/docs/installation/prompt 
	1. `notepad $PROFILE`
		1. If this doesn't work. create the profile `New-Item -Path $PROFILE -Type File -Force`
	2. write `oh-my-posh init pwsh | Invoke-Expression`
	3. `$PROFILE` to update it
	4. open a new session
