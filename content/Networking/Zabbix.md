---
tags:
  - automation
---

Zabbix is a service that allows you to monitor networks and visualize data. It works off a JSON RPC api, not a rest api unfortunately. This means you must input a json file to receive something back. Curl is able to access it, I have tried to access it with pyzabbix api, but it does not allow it. urls for this are only zabbix domains.