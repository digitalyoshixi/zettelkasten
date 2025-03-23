---
tags:
  - python
  - database
---
# Boilerplate
```python
import sqlite3

# Initialize connection and cursor at module level
conn = sqlite3.connect("carbon.db")
cursor = conn.cursor()
cursor.execute(
"""CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
name text NOT NULL,
coins INTEGER DEFAULT 0)""")

conn.commit()

def insert_user(user : str, coins : int = 0):
    cursor.execute("""INSERT INTO users(name, coins) VALUES(?,?);""", (user, coins))
    conn.commit()  # Add commit to save changes

def get_user(user : str):
    cursor.execute("""SELECT * FROM users WHERE name = ?;""", (user,))
    return cursor.fetchone()

def set_coins(user : str, coins : int):
    cursor.execute("""UPDATE users SET coins = ? WHERE name = ?;""", (coins, user))
    conn.commit()  # Add commit to save changes

def get_coins(user : str):
    cursor.execute("""SELECT coins FROM users WHERE name = ?;""", (user,))
    return cursor.fetchone()

def inc_coins(user : str, coins : int):
    user_coins = get_coins(user)
    set_coins(user, user_coins[0] + coins)

#insert_user("dude", 0)
#print(get_user("dude"))
#inc_coins("dude", 10)
#print(get_coins("dude"))
```