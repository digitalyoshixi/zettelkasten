---
tags:
  - vim
---
A plugin manager for [[Neovim]]
# Adding Plugins
`nvim ~/.config/nvim/lua/plugins/<pluginname>`
And then write you plugin details in that file
![[Lazy Nvim-20240903194814659.webp]]
# Files
After installing, you will have:
- `init.lua`
- `lua/options.lua` - the [[Vim .vimrc]] file, but you must use `vim.opt.<option>` instead of `set`
- `lua/keymaps.lua`
# Uninstall
1. `rm ~/.config/nvim`
2. `rm rf ~/.local/state/nvim`
3. `rm rf ~/.local/share/nvim`

# Plugins
- [[Vimtex]]
- [[Luasnips]]