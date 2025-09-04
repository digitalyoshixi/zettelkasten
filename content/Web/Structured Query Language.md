---
tags:
  - database
aliases:
  - SQL
---
A language for making [[Relational Database|Relational Databases]].
It is [[Create Read Update Delete|CRUD]] supported
Data is stored in tables
# Concepts
- [[SQL Table]]
# Query Types
### SELECT Queries
![[Structured Query Language-20240802195210682.webp]]
# SQL DB Relationships
- One-to-one
- One-to-many
- Many-to-many
# SQL Operations
- [[SQL CREATE]]
- [[SQL Insert]]
- [[SQL Update]]
- [[SQL Drop]]
- [[SQL Select]]
- [[SQL Join]]
- [[SQLite View Columns]]
# SQL Constaints
### SERIAL
Denotes unique integer numbers for IDs
### PRIMARY
The column is the primary key
### NOT NULL
Cannot accept a null value
# Connecting
- [[psycopg2]]
- [[Django]]
- [[Flask]]
- [[SQLAlchemy]]