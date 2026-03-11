---
tags:
  - vim
  - programming
---
a improved version of the text editor vi.
VI improved.
Highly customizable keyboard based text editor.

https://www.youtube.com/watch?v=RZ4p-saaQkc
# Modes
Vim has 3 modes.
1. **Normal** -  allows for vim keybind commands by first typing **:**, giving a keyword, and then pressing enter.
	To enter normal mode, the key is **ESC**
2. **Insert** - for typing the file data
	To enter insert mode, the key is **i**
3. **Visual** - for selecting segments of the file
	To enter visual mode, the key is **v**
## Normal Mode Keywords
| key       | meaning  | function                                                                                                                                           | function2                                                         | function3 |
| --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------- |
| **!**     | command  | [:!\*] allows for terminal commands after it                                                                                                       | [:\*!] forces the previous command. like :q! quits without saving |           |
| **q**     | quit     | quits the currently edited file                                                                                                                    |                                                                   |           |
| **w**     | write    | writes to the file                                                                                                                                 |                                                                   |           |
| **r**     | replace  | replaces cursor selection charcter with the next character you type                                                                                |                                                                   |           |
| **1-inf** | repeat # | [:(some number between 1-inf)\*] # of times to repeat the next action you do. for example, [:15(right arrow key)] will cursor 15 characters right. |                                                                   |           |
| **h**     | left     | moves cursor left                                                                                                                                  |                                                                   |           |
| **l**     | right    | moves cursor right                                                                                                                                 |                                                                   |           |
| **j**     | down     | moves cursor down                                                                                                                                  |                                                                   |           |
| **k**     | up       | moves cursor up                                                                                                                                    |                                                                   |           |
## Mode Changing Keywords
| key   | meaning                         | function                                                                   | function2 |     |
| ----- | ------------------------------- | -------------------------------------------------------------------------- | --------- | --- |
| **i** | **Enter Insert Mode Before**    | Enter insert mode before the cursor selection                              |           |     |
| **I** | Enter Insert Mode Start of Line | Enter insert mode at the start of the current line                         |           |     |
| **a** | Enter Insert Mode After         | Enter insert mode after the cursor selection                               |           |     |
| **A** | Enter Insert Mode End of Line   | Enter insert mode at the end of the current line                           |           |     |
| **o** | Enter Insert Mode Newline Below | Enter insert mode and create a newline below which we start inserting from |           |     |
| **O** | Enter Insert Mode Newline Above | Enter insert mode and create a newline above which we can start inserting  |           |     |
| **v** | **Enter Visual Mode**           | Enter visual mode, switching modes in the process                          |           |     |

## Keyword Chaining
You can chain these keyword commands to do several at once.
or example, :wq will write to the file, then quit the file. So you do 2 commands in one.

# Vim Preferences
Inside normal mode, you are able to enable features like numbered lines or relative numbering or tabstop.
A list of 50 of them found here: https://www.shortcutfoo.com/blog/top-50-vim-configuration-options
Now, these will only be for the current file. opening a new file will not save these changes.
To make these changes permanent, you will need to edit the [[Vim .vimrc]]
# Tricks
- [[Vim Replace]]
- [[Vim Indent]]