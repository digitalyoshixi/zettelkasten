---
tags:
  - redteam
  - web
  - security
---
To install, watch this: [https://www.youtube.com/watch?v=WkyDxNJkgQ4](https://www.youtube.com/watch?v=WkyDxNJkgQ4)

To boot up again, type:

- Sudo service apache2 start
    
- Sudo service mysql start


### [[SQL Injection]]

There are certain sql queries that when inputted into a textbox, can break through the sql prompt.

Single quotes will allow us to inject sql commands into the statements. An example being:

The statement: “SELECT name FROM users WHERE userid = ‘$id’;”

We are able to input id.

So, if id is 1’ or ‘1’ = ‘1

Then, statement is “SELECT name FROM users WHERE userid = ‘1’ or ‘1’ = ‘1’;”

This will return all user names since it will go to the or statement where 1 = 1 is true.

  

There are a few types of sql injection techniques. They can all gather various types of data and perform different attacks. Below are them listed.

- Retrieving hidden data. Modify a SQL query to retrieve unintended data
    
- Subverting application logic. Using queries to interfere with application logic
    
- UNION attacks. Retrieve data from different database tables.
    
- Examining database. Extract information about version and structure of database
    
- Blind sql injection. No results, but timed attacks.

### [[OS Command Injection]]:

Following this video.

[https://www.youtube.com/watch?v=WiqRvlN_UIU](https://www.youtube.com/watch?v=WiqRvlN_UIU)

  

Wireshark can be used to obtain packets

1. sudo wireshark
    
2. any
    

Command injection is only possible if an input allows linux commands to be run through. Since linux commands can pipe, && and ; to allow multiple commands on one line, we can leverage this to run any command we want. This allows us to also write scripts. By using [echo “sometext” > sometext.py] and then ./sometext.py then we can perform havoc

### [[Cross Site Request Forgery]]:

Changing a url to already pre-include form information. There are 3 main conditions that must be in place.

1. An action that gives the attacker priority. Remember, we give them a url with information already included. We can leverage this in password reset urls where we change the email it sends the reset to as ours.
    
2. Cookie based sessions. The user is already logged in so the url doesn’t reroute
    
3. Predictable parameters. Know what the website has for parameters so you don't need to guess. You can’t know their password, so don't use their password.
    

This requires social engineering to send this URL.

we can catch a specific http request with [[Burp Suite]]


    


[[Path Traversal]]:

Take advantage of url navigation. If it opens files that are local, then you can manipulate the directories like /somedir/file.php or ../websiteimages/nudes.png the ../ is meaning to go backwards. By the way, you can also view it through terminal instead of a webapp since it is stored locally.
to find directories, we can use [[Gobuster]] or [[Wfuzz]]

