---
tags:
  - programming
---
A golang library for database migrations
# Installations
```
go install github.com/pressly/goose/v3/cmd/goose@latest
```
# Create a new Table
```
goose -dir=assets/migrations create mytablename sql
```
Example file:
```sql
-- +goose Up
CREATE TABLE users {
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    pwd VARCHAR(255) NOT NULL,
    createdAt DATETIME NOT NULL
}

-- +goose Down
DROP TABLE users;
```
# Create Database From Table
```
goose -dir=assets/migrations sqlite3 database.db
```