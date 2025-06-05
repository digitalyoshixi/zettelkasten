---
tags:
  - automation
  - linux
aliases:
  - Cronjob
---
In order to setup a chronological repeating task without a for loop that checks every second, you will use cron library installed on most linux distros.
# Setups
1. `crontab -e`
2. [https://crontab.guru](https://crontab.guru/) find the time that you want to repeat.
3. Write your task: `* */5 * * * /sbin/shutdown -r now` (will reboot every 5hrs)
4. After saving, cron will update right away, no extra steps required.
5. `crontab -l` to view saved tasks