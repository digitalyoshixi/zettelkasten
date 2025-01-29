---
tags:
  - vim
---
For [[VSCode]] style snippets.
Requires [[Lazy Nvim]]
# Installation and Setup
1. `nvim ~/.config/nvim/lua/plugins/init.lua`
2. 
```
 {
  "L3MON4D3/LuaSnip",
  lazy = true,
  dependencies = {
    "rafamadriz/friendly-snippets",
  },
  config = function()
    local luasnip = require("luasnip")
    luasnip.config.set_config({
      enable_autosnippets = true,
    })
    require("luasnip.loaders.from_lua").load({paths = "~/.config/nvim/lua/luasnippets/"})
  end,
 },
```
3. `mkdir -p ~/.config/nvim/lua/luasnippets/`
4. `nvim ~/.config/nvim/lua/luasnippets/all.lua`
```lua
local ls = require("luasnip")
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node

return {
  -- general purpose
  s({
    trig = "hi",
    snippetType = "autosnippet"
  }, {
    t("Hello, ")
    i(1)
    t(" , world!")
  }),

}


```
# My Snippets
```lua
local ls = require("luasnip")
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node

local function math()
    return vim.api.nvim_eval('vimtex#syntax#in_mathzone()') == 1
end

return {
  -- general purpose
  s({
    trig = "hi",
    snippetType = "autosnippet"
  }, {
    t("Hello, world!")
  }),
  -- latex
  s({
    trig = "sum",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\sum_{i=1}^{n}")
  }),
  s({
    trig = "int",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\int_{a}^{b}f(x)dx")
  }),
  s({
    trig = "tri",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\triangle")
  }),
  s({
    trig = "^",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("^{"),
    i(1),
    t("}"),
  }),
  s({
    trig = "_",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("_{"),
    i(1),
    t("}"),
  }),
  s({
    trig = "not",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\not")
  }),
  s({
    trig = "not",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\not")
  }),
  s({
    trig = "vec",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\overline{"),
    i(1),
    t("}")
  }),
  s({
    trig = "ds",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathds{"),
    i(1),
    t("}")
  }),
  s({
    trig = "inn",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\in"),
  }),
  s({
    trig = "fa",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\forall"),
  }),
  s({
    trig = "ex",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\exists"),
  }),
  s({
    trig = "inf",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\infty"),
  }),
  s({
    trig = "eps",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\epsilon"),
  }),
  s({
    trig = "del",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\del"),
  }),
  s({
    trig = "-->",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\Rightarrow"),
  }),
  s({
    trig = "<--",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\Leftarrow"),
  }),
  s({
    trig = "<-->",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\Leftrightarrow"),
  }),
  s({
    trig = "->",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\to"),
  }),
  s({
    trig = "<-",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\from"),
  }),
  s({
    trig = "qed",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\square"),
  }),
  s({
    trig = "lim",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\lim_{x \\to "),
    i(1),
    t("}"),
  }),
  s({
    trig = "nn",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\cap"),
  }),
  s({
    trig = "uu",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\cup"),
  }),
  s({
    trig = "and",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\wedge"),
  }),
  s({
    trig = "or",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\vee"),
  }),
  s({
    trig = "frac",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\frac{"),
    i(1),
    t("}{"),
    i(2),
    t("}"),
  }),
  s({
    trig = "sq",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\sqrt{"),
    i(1),
    t("}"),
  }),
  s({
    trig = "tex",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\text{"),
    i(1),
    t("}"),
  }),
  s({
    trig = "...",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\dots"),
  }),
  s({
    trig = "<=",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\leq"),
  }),
  s({
    trig = ">=",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\geq"),
  }),
  s({
    trig = "pi",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\pi"),
  }),
  s({
    trig = "RR",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathbb{R}"),
  }),
  s({
    trig = "FF",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathbb{F}"),
  }),
  s({
    trig = "set",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\{"),
    i(1),
    t("\\}"),
  }),
  s({
    trig = "partition",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("P = \\{ x_i^*\\}^n_{i=0}"),
  }),
  s({
    trig = "riepart",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("P  = \\{ x_i\\}_{i=0}^n"),
  }),
  s({
    trig = "subset",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\subset"),
  }),
  s({
    trig = "align",
    snippetType = "autosnippet"
  }, {
    t({"\\begin{align*}", "\\text{(1) } & \\text{} & \\text{}", "\\end{align*}"}),
  }),
  s({
    trig = "RR",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathbb{R}"),
  }),
  s({
    trig = "ZZ",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathbb{Z}"),
  }),
  s({
    trig = "FF",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathbb{F}"),
  }),
  s({
    trig = "QQ",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\mathbb{Q}"),
  }),
  s({
    trig = "neq",
    condition = math,
    snippetType = "autosnippet"
  }, {
    t("\\neq"),
  }),
}
```