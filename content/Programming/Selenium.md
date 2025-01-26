---
tags:
  - webcrawler
---
Python module that allows you to grab information from webpages and interact with them. This allows you to make bots, automated scripts to test websites.

First you need to connect your driver. Give is a service(browser like chromium or firefox) and option.

Secondly, you can start searching. driver.find_element(By.Type, “type name”). You should only search for divs with special ids, classes or tags, since they are special

Thirdly, if you are on a textbox or clickbox, you can enter commands like typing or clicking

Lastly, you are able to get the text from a div by using div.text