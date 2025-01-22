---
tags:
  - android
  - reverse_engineering
---
p# Install
https://apktool.org/docs/install/
1. Download the Linux [wrapper script](https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool). (Right click, Save Link As `apktool`)
2. Download the [latest version](https://bitbucket.org/iBotPeaches/apktool/downloads) of Apktool.
3. Rename the downloaded jar to `apktool.jar`.
4. Move both `apktool.jar` and `apktool` to `/usr/local/bin`. (root needed)
5. Make sure both files are executable. (`chmod +x`)
6. Try running `apktool` via CLI.
Or
1. `yay -S android-apktool`
# Decompile
`apktool d <app>.apk`
After decompile, the flutter app engine can be found at `<app>/lib/arm64-v8a/libapp.so`