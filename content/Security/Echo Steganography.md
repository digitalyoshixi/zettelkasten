---
tags:
  - forensics
---
A form of hiding data within the echos of audio in a audio file.
Artificial echos are created with:
- Short delay (1ms) = 0
- Long delay (2ms) = 1
$$s(n) = x(n) + α × x(n - d)$$

- $s(n)$ is the stego-signal (audio with hidden data)
- $x(n)$ is the original audio signal
- $α$ is the attenuation factor (typically 0.1 to 0.5)
- $d$ is the delay in samples
- $n$ is the sample index
