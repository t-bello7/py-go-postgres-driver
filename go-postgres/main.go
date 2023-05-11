package main

import "fmt"
import (
	"database/sql"
	_ "github.com/lib/pq"
)

func main() {
	connStr := "user=objectrocket dbname=some_new_database password=mypass host=localhost sslmode=verify-full"
	db,err := sql.Open("postgres", connStr)
	if err != nil {
		fmt.Println(err)
	}
	err2 := db.QueryRow(`INSERT INTO user_table (user_id, name, age, phone) VALUES(3, 'Jenny', 34, NULL);`)
	fmt.Println(err2)

	rows, err := db.Query("SELECT * FROM user_table;")
    fmt.Println("Hello, world.")
	fmt.Println(rows)
}
