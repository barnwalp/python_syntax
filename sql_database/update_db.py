from mysql.connector import connect
import os


mydb = connect(
    host='localhost',
    user='root',
    passwd=os.environ.get('sql_password'),
    database='testdb'
)

my_cursor = mydb.cursor()
# will return only 5 rows offset by 2 rows
my_cursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")

# update the row in table
# my_cursor.execute("UPDATE students SET age = 39 WHERE name = 'Anita'")
# mydb.commit()
my_results = my_cursor.fetchall()
for row in my_results:
    print(row)
