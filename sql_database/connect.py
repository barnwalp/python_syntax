from mysql.connector import connect
import os

# connecting to mysql localhost server
mydb = connect(
    host='127.0.0.1',
    user='root',
    passwd=os.environ.get('sql_password')
)

mycursor = mydb.cursor()
# Creating a new database
# mycursor.execute("CREATE DATABASE testdb")

# Show all databases
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)