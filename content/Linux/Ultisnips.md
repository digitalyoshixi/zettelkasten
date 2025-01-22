---
tags:
  - vim
---
A code snippet tool for [[Vim]].
# Installation
1. Install `vim-snippets` using lazy nvim:
```lua
return{
	"honza/vim-snippets"
}

```   
2. Using [[Lazy Nvim]],
```lua
return{
{
    "SirVer/ultisnips",
    init = function()
      vim.g.UltiSnipsSnippetDirectories = {"~/.config/nvim/UltiSnips"}
    end,
  },
}
```
# Installing [[LaTex]] snippets
1. Download: https://github.com/gillescastel/latex-snippets/blob/master/tex.snippets
2. Move `tex.snippets` to `~/.config/nvim/UltiSnips`