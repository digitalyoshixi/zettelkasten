---
tags:
  - programming
  - godot
  - game_dev
---
# Collision Mode
A setting to toggle how collisions are generated in game.
- Dynamic/Game : Collisions are generated for chunks around the camera
- Dynamic/Editor : Collisions are generated for chunks around the camera during editor, so collisions can be visualized
- Full/Game : Collisions are all generated at the start of game, slow initial start
- Full/Game : Collisions are all generated in editor, allows visualizing collisions
- Disabled: No collision generation
# Collision Shape
- Only used if mode is dynamic
- Defines the size of each collision shape
- Smaller adds more detail, larger 
# Collision Radius
- Only used if mode is dynamic
- The distance from camera that collisions start being generated.