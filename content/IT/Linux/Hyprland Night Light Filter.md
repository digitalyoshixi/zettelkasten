---
tags:
  - ricing
---
For [[NVIDIA]] gpus, you cannot use [[gammastep]].
You must apply a hyprland red filter to save your eyes.
1. Create a file `~/.config/hypr/shaders/nightlight.frag`
2. Write the following to the file:
```c
//
// Example blue light filter shader.
// 

precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {

    vec4 pixColor = texture2D(tex, v_texcoord);

    pixColor[2] *= 0.8;

    gl_FragColor = pixColor;
}
```
3. Edit `~/.config/hypr/hyprland.conf` and write:
```c
decoration {
	... // whatever was here before
	screen_shader = ~/.config/hypr/shaders/nightlight.frag
}
```

# Alternate Fix for [[OpenGL]] 300
```c
#version 300 es
//
// Blue light filter shader for Hyprland
// 
precision mediump float;

in vec2 v_texcoord;

out vec4 fragColor;

uniform sampler2D tex;

void main() {
    vec4 pixColor = texture(tex, v_texcoord);
    
    // Reduce blue component
    pixColor.b *= 0.85;
    
    // Slightly reduce alpha
    pixColor.a *= 0.9;
    
    fragColor = pixColor;
}
```