---
tags:
  - 0xInfection
  - vim
---
### Part 18: Vim:

We must first configure vim to look nice:

1. Type: vi .vimrc in terminal
    
2. Press i
    
3. Type:
    

set number

set smartindent

set tabstop=4

set shiftwidth=4

set expandtab

syntax on

set nowrap

set showmode

set hlsearch

set clipboard=unnamedplus

  

4. Press esc, :wq, enter
    

There are 2 modes in vim. Command mode and insert mode. Command move lets you navigate and do extra options regarding editing. Insert mode will allow you to start writing file

The following commands are available in command mode:

**j** Move cursor down a line

**k** Move cursor up a line

**h** move cursor left a character

**l** move cursor right a character

**0** move cursor to start of line

**$** move cursor to end of line

**b** move cursor to beginning of current character

**dd** delete line the cursor is on

**D** delete from cursor position to end of line

**yy** copy current line

**p** paste copied text

**u** undo

**:w** save

**:wq** save and quit

**:q!** quit

  