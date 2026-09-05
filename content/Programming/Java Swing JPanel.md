---
tags:
  - programming
  - java
---
```java
JPanel panel = new JPanel();
int TOP, DOWN = 30;
int LEFT, RIGHT = 10;
panel.setBorder(BorderFactory.createTiltedBorder(BorderFactory.createEmptyBorder(TOP,DOWN,LEFT,RIGHT)));

JPanel mid = new JPanel();
panel.add(mid, BorderLayout.CENTER);
```