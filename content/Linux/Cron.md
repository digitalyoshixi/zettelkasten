---
tags:
  - automation
  - linux
aliases:
  - Cronjob
---
In order to setup a chronological repeating task without a for loop that checks every second, you will use cron library installed on most linux distros.
1. Crontab -e
2. [https://crontab.guru](https://crontab.guru/) find the time that you want to repeat.
* 5 * * * means at 00:05 * /5 * * * means at every 5 minutes
3. If you are running a python file, first type the directory of python. python or /whereveryouinstalledpython/python3
4. Type the directory of the file you want to run. Eg. /etc/cron.d/davidlogs.py
A single line is required for setting it up. Example of a line:
*/5 * * * * /opt/stackstorm/virtualenvs/python3_test/bin/python3 /home/pwadmin/david/projects/getlogs.py