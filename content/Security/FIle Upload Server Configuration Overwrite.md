---
tags:
  - web
  - security
---
A file upload vulnerability wherein key server configuration files can be overwritten by [[Path Traversal]].
# Apache
`/etc/apache2/apache2.conf`
Example directive to allow executable of PHP:
```
LoadModule php_module /usr/lib/apache2/modules/libphp.so AddType application/x-httpd-php .php
```
Alternatively, use the [[htaccess]] file for the local directory
```
AddType application/x-httpd-php .l33t
```
- Adds the mime type `.l33t` to map to php, so any file with this extension is interpreted as PHP
# IIS
`web.config`
Example directive to allow JSON files to be served:
```
<staticContent>
    <mimeMap fileExtension=".json" mimeType="application/json" />
</staticContent>
```