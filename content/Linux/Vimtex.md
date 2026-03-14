---
tags:
  - vim
  - math
---
A [[Neovim]] plugin that is able to lint and format latex.
# Installation
1. Install [[TeX Live]]. 
2. Install `sudo pacman -S texlive-fontsextra`
3. Using [[Lazy Nvim]], add the plugin `~/.config/nvim/lua/plugins/init.lua` with the following:
```
-- Configure plugins
require("lazy").setup({
  {
    "lervag/vimtex",
    lazy = false,
    config = function()
      vim.g.vimtex_view_method = 'zathura'
      vim.g.vimtex_compiler_method = 'latexmk'
    end,
  },
})
```
# AutoCompile
To enable autocompile, do: `:VimtexCompile`
And then you can use [[Zathura]] to view the pdf file. It will auto change everytime you `:w` to the file.