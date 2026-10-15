---
tags:
  - linux
---
```
sudo lsof -i -P -n | grep LISTEN
```

```
sudo netstat -tulpn | grep LISTEN
```

```
sudo ss -tulpn
```
