---
tags:
  - linux
  - ricing
---
For [[swww]] there is no native support, you must use [[Imagemagick]] to split a single image into multiple.
https:/github.com/LGFae/swww/issues/121
```bash
#!/bin/bash
wallpapers=$HOME/pictures/wide
random=$(ls $wallpapers | shuf | head -1)
random=$wallpapers/$random

# split image
convert -crop 50%x100% $random /tmp/output.png

swww img -o "DP-2" --transition-type random /tmp/output-0.png
swww img -o "DP-1" --transition-type random /tmp/output-1.png
```
# JaKooLit Custom WallpaperSelect Multiple Monitor Script
```bash
#!/bin/bash

# /* ---- 💫 https://github.com/JaKooLit 💫 ---- */

# This script for selecting wallpapers (SUPER W)

  

# WALLPAPERS PATH

wallDIR="$HOME/Pictures/wallpapers"

SCRIPTSDIR="$HOME/.config/hypr/scripts"

  

# variables

focused_monitor=$(hyprctl monitors | awk '/^Monitor/{name=$2} /focused: yes/{print name}')

# swww transition config

FPS=60

TYPE="any"

DURATION=2

BEZIER=".43,1.19,1,.4"

SWWW_PARAMS="--transition-fps $FPS --transition-type $TYPE --transition-duration $DURATION"

  

# Check if swaybg is running

if pidof swaybg > /dev/null; then

  pkill swaybg

fi

  

# Retrieve image files using null delimiter to handle spaces in filenames

mapfile -d '' PICS < <(find "${wallDIR}" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -print0)

  

RANDOM_PIC="${PICS[$((RANDOM % ${#PICS[@]}))]}"

RANDOM_PIC_NAME=". random"

  

# Rofi command

rofi_command="rofi -i -show -dmenu -config ~/.config/rofi/config-wallpaper.rasi"

  

# Sorting Wallpapers

menu() {

  # Sort the PICS array

  IFS=$'\n' sorted_options=($(sort <<<"${PICS[*]}"))

  # Place ". random" at the beginning with the random picture as an icon

  printf "%s\x00icon\x1f%s\n" "$RANDOM_PIC_NAME" "$RANDOM_PIC"

  for pic_path in "${sorted_options[@]}"; do

    pic_name=$(basename "$pic_path")

    # Displaying .gif to indicate animated images

    if [[ ! "$pic_name" =~ \.gif$ ]]; then

      printf "%s\x00icon\x1f%s\n" "$(echo "$pic_name" | cut -d. -f1)" "$pic_path"

    else

      printf "%s\n" "$pic_name"

    fi

  done

}

  

# initiate swww if not running

swww query || swww-daemon --format xrgb

  

# Choice of wallpapers

main() {

  choice=$(menu | $rofi_command)

  # Trim any potential whitespace or hidden characters

  choice=$(echo "$choice" | xargs)

  RANDOM_PIC_NAME=$(echo "$RANDOM_PIC_NAME" | xargs)

  

  # No choice case

  if [[ -z "$choice" ]]; then

    echo "No choice selected. Exiting."

    exit 0

  fi

  

  # Random choice case

  if [[ "$choice" == "$RANDOM_PIC_NAME" ]]; then

#    mv $RANDOM_PIC_NAME ~/.config/hypr/wallpaper_effects/.wallpaper_current

    width=$(identify -format "%w" $RANDOM_PIC)

  

    # Calculate the widths of each segment

    part1_width=$((width * 30 / 100))

    part2_width=$((width * 40 / 100))  # 70% - 30% = 40%

    part3_width=$((width * 30 / 100))  # 100% - 70% = 30%

  

    # Split the image into three parts

    convert $RANDOM_PIC -crop ${part1_width}x+0+0 ~/.config/hypr/wallpaper_effects/part1.jpg

    convert $RANDOM_PIC -crop ${part2_width}x+${part1_width}+0 ~/.config/hypr/wallpaper_effects/part2.jpg

    convert $RANDOM_PIC -crop ${part3_width}x+$((${part1_width} + ${part2_width}))+0 ~/.config/hypr/wallpaper_effects/part3.jpg

    echo $RANDOM_PIC  

    echo $RANDOM_PIC  

    echo $RANDOM_PIC  

    swww img -o "HDMI-A-1" ~/.config/hypr/wallpaper_effects/part1.jpg $SWWW_PARAMS;

    swww img -o "DP-1" ~/.config/hypr/wallpaper_effects/part2.jpg $SWWW_PARAMS;

    swww img -o "DVI-D-1" ~/.config/hypr/wallpaper_effects/part3.jpg $SWWW_PARAMS;

    sleep 0.5

    "$SCRIPTSDIR/WallustSwww.sh"

    sleep 0.2

    "$SCRIPTSDIR/Refresh.sh"

    exit 0

  fi

  

  # Find the index of the selected file

  pic_index=-1

  for i in "${!PICS[@]}"; do

    filename=$(basename "${PICS[$i]}")

    if [[ "$filename" == "$choice"* ]]; then

      pic_index=$i

      break

    fi

  done

  

  if [[ $pic_index -ne -1 ]]; then

    thepic = "${PICS[$pic_index]}"

  

    width=$(identify -format "%w" "${PICS[$pic_index]}")

  

    # Calculate the widths of each segment

    part1_width=$((width * 30 / 100))

    part2_width=$((width * 40 / 100))  # 70% - 30% = 40%

    part3_width=$((width * 30 / 100))  # 100% - 70% = 30%

  

    # Split the image into three parts

    convert "${PICS[$pic_index]}" -crop ${part1_width}x+0+0 ~/.config/hypr/wallpaper_effects/part1.jpg

    convert "${PICS[$pic_index]}" -crop ${part2_width}x+${part1_width}+0 ~/.config/hypr/wallpaper_effects/part2.jpg

    convert "${PICS[$pic_index]}" -crop ${part3_width}x+$((${part1_width} + ${part2_width}))+0 ~/.config/hypr/wallpaper_effects/part3.jpg

   swww img -o "HDMI-A-1" ~/.config/hypr/wallpaper_effects/part1.jpg $SWWW_PARAMS;

    swww img -o "DP-1" ~/.config/hypr/wallpaper_effects/part2.jpg $SWWW_PARAMS;

    swww img -o "DVI-D-1" ~/.config/hypr/wallpaper_effects/part3.jpg $SWWW_PARAMS;

  
  
  

  #  swww img -o "$focused_monitor" "${PICS[$pic_index]}" $SWWW_PARAMS

  else

    echo "Image not found."

    exit 1

  fi

}

  

# Check if rofi is already running

if pidof rofi > /dev/null; then

  pkill rofi

  sleep 1  # Allow some time for rofi to close

fi

  

main

  

sleep 0.5

"$SCRIPTSDIR/WallustSwww.sh"

  

sleep 0.2

"$SCRIPTSDIR/Refresh.sh"
```