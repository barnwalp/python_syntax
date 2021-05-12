from mysql.connector import connect
import os


mydb = connect(
    host='localhost',
    user='root',
    passwd=os.environ.get('sql_password'),
    database='testdb'
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM students")
# fetch all rows
my_result = my_cursor.fetchall()
# fetch first row
# my_result = my_cursor.fetchone()

# printing all fetched data
for row in my_result:
    print(row)
