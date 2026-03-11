---
tags:
  - linux
aliases:
  - FFMPEG
---
A command line tool for processing video and audio [[Video Files|Codecs]].
# Process
1. [[Demultiplexer|DEMUX]] a given file into frames
2. Decode into uncompressed raw frames
3. Perform some filter or operation (optional)
4. Encoded
5. [[Multiplexer|MUX]] into a single file
# Converting Codecs
```
ffmpeg -i input.mp4 out.mov
```
# Extra Tools
- [[ffplay]]
- [[ffprobe]]