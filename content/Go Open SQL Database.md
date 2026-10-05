---
tags:
  - programming
  - go
---
# Installations
```
go get github.com/mattn/go-sqlite3
```
# Usage
```go
import (
	"github.com/mattn/go-sqlite3"
)



func main() {
	conn, err := sql.Open("sqlite3", "./database.db")
	if err != nil {
		log.Fatal(err)
	}
	db = conn
	log.Println(db)
	users, err := GetAllUsers(db)
	if err != nil {
		log.Fatal(err)
	}
	log.Println(users)
}


func GetAllUsers(db *sql.DB) ([]User, error) {
	rows, err := db.Query("SELECT id, username, password, role, createdAt FROM users ORDER BY id ASC")
	if err != nil {
		return nil, err
	}
	users := []User{}
	for rows.Next() {
		u := User{}
		err := rows.Scan(&u.Id, &u.Username, &u.PasswordHash, &u.Role, &u.CreatedAt)
		if err != nil {
			return nil, err
		}
		users = append(users, u)
	}

	err = rows.Err()
	if err != nil {
		return nil, err
	}
	return users, nil
}


func InsertUser(db *sql.DB, registerdata UserAuth) error {
	stmt := `INSERT INTO users (username, password, role, createdAt) VALUES (?,?,0,datetime('now'))`

	passhash, err := HashPassword(registerdata.Password)
	if err != nil {
		return err
	}
	_, err = db.Exec(stmt, registerdata.Username, passhash)
	if err != nil {
		return err
	}
	return nil
}

```