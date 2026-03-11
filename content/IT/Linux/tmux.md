---
tags:
  - linux
aliases:
  - Terminal Multiplexer
---
The best program for [[Command Line Interface]] coding.
- Saved sessions
- Multiple windows
# Installation
1. `sudo pacman -S tmux`
2. `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
3. `nvim ~/.config/tmux/tmux.conf`
```
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

run '~/.tmux/plugins/tpm/tpm'

# set prefix
unbind C-b
set -g prefix C-Space
bind C-Space send-prefix
```
# Keybinds
- `prefix` is `CTRL+Space`. You press the **prefix** key then release before pressing the other keys
- Enter commands `: ...` with `prefix+:`
### [[Tmux Session]] Management
- `tmux new -s my_session_name` : create new session
- `tmux ls` : view sessions
- `:new new_session_name` : create new session inside tmux
- `prefix+s` : view sessions inside tmux
- `prefix+w` : view each session as window
- `tmux attach` : attach to most recent session
- `tmux attach -t my_session_name` : attach to specific session
### [[Tmux Window]] Management
- `prefix+c` : make new [[Tmux Window]]
- `prefix+<window number>` : make window number the primary window
- `prefix+n` : go to next window
- `prefix+p` : go to previous window
- `prefix+&` : kill current window
- `:swap-window -s 2 -t 1` : swaps window 1 with 2
### [[Tmux Pane]] Management
- `prefix+%` : split current window horizontally
- `prefix+"` : split current window vertically
- `prefix+<arrow key>` : change current focused pane
- `prefix+q` : quick change to a numbered pane
- `prefix+z` : zoom into pane
- `prefix+!` : convert pane into window
- `prefix+x` : close current pane
- `prefix+PG_UP` : enable scrolling
# Commands
# Concepts
- [[Tmux Session]]
- [[Tmux Window]]
- [[Tmux Pane]]