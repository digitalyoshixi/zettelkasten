---
tags:
  - python
  - database
---
A [[Python Library]] for CRUD operations on [[PostgreSQL]] databases.
# Installation
1. `sudo pacman -S postgresql`
2. `source /bin/activate`
3. `pip install psycopg2`
# Connecting To [[Supabase]]
1. ![[psycopg2-20241003041153443.webp]]
2. ![[psycopg2-20241003041224222.webp]]
# [[PostgreSQL]] Operations
### [[SQL CREATE]]
```python
conn = psycopg2.connect(f"user=postgres.vbxwlsqodbrcxzqnjggs password={postgrespass} host=aws-0-us-east-1.pooler.supabase.com port=6543 dbname=postgres")

with conn: # assuming we have connection
    with conn.cursor() as dbcurs:
        try:
            dbcurs.execute("""
                           CREATE TABLE users (
                            uid SERIAL PRIMARY KEY,
                            username VARCHAR(255) NOT NULL,
                            password VARCHAR(255) NOT NULL
                           )
                           """)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
```
### [[SQL Insert]]
```python
with conn: # assuming we have connection
	with conn.cursor() as dbcurs:
	        try:
	            dbcurs.execute("""
		            INSERT INTO users (username,password) VALUES
		            ('DANIEL','dogecoin'),
		            ('DEMON', 'dogworm7')
	            """)
	        except (Exception, psycopg2.DatabaseError) as error:
	            print(error)
```
### [[SQL Select]]
```python
with conn: # assuming we have connection
    with conn.cursor() as dbcurs:
        try:
            dbcurs.execute("SELECT * FROM users")
            results = dbcurs.fetchall()
            # result = dbcurs.fetchone() # fetch only one row
            # print(results)
            for row in results:
	            print(row)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
```
### [[SQL Update]]
```python
with conn: # assuming we have connection
    with conn.cursor() as dbcurs:
        try:
            dbcurs.execute("""
            UPDATE users set password = 'dogecoin2' WHERE uid = 1
            """)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
```
### [[SQL Drop]]
```python
with conn: # assuming we have connection
    with conn.cursor() as dbcurs:
        try:
            dbcurs.execute("""
            DELETE FROM users WHERE uid = 1
            """)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
```