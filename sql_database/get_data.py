from mysql.connector import connect
import os


mydb = connect(
    host='localhost',
    user='root',
    passwd=os.environ.get('sql_password'),
    database='testdb'
)

my_cursor = mydb.cursor()

# Getting all rows
# sql = "SELECT * FROM students"

# Getting conditional data
# sql = "SELECT * FROM students WHERE age=33"

# Using wildcard to select desired data
sql = "SELECT * FROM students WHERE name LIKE '%in%'"

# Execute the sql statement
my_cursor.execute(sql)
# fetch all rows
my_result = my_cursor.fetchall()

# fetch first row
# my_result = my_cursor.fetchone()

# printing all fetched data
for row in my_result:
    print(row)
