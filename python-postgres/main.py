import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=some_new_database user=objectrocket password=mypass host=localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

print("\n type(conn)", type(cur))

DB_NAME = "some_new_database"
# # #cursor.execute('CREATE DATABASE ' + str(DB_NAME))

autocommit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
print ("ISOLATION_LEVEL_AUTOCOMMIT:", psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
conn.set_isolation_level( autocommit )
# cur.execute('GRANT ALL ON DATABASE python_test TO objectrocket;')
# cur.execute('ALTER DATABASE python_test OWNER TO objectrocket;')
# cur.execute("set role to objectrocket;")
cur.execute("CREATE TABLE IF NOT EXISTS user_table (user_id serial PRIMARY KEY, name varchar NOT NULL, age integer NOT NULL,phone varchar);")
# cur.execute("INSERT INTO user_table (user_id, name, age, phone) VALUES(3, 'Jenny', 34, NULL);")
# Execute a query
# cur.commit
rows = cur.execute("SELECT * FROM user_table;")
print(rows)
# Retrieve query results
records = cur.fetchall()
