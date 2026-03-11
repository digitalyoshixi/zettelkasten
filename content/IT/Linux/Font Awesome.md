---
tags:
  - linux
---
The font with all the quirky icons of hacker culture!
# Install Locally
`sudo pacman -S ttf-font-awesome`
`sudo pacman -S nerd-fonts`
# Add To Webpage (With [[Sass|SCSS]])
1. Download font-awesome from the site https://fontawesome.com/download
2. move the `scss` folder files into a sub-folder called `fontawesome`inside where you keep your main `main.scss`.
   ![[Font Awesome-20241122043829262.webp]]
3. do 
```
@import 'fontawesome/fontawesome';
@import 'fontawesome/solid';
@import 'fontawesome/brands';
```
2. move `webfonts` folder to your root directory