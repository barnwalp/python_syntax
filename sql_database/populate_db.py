from mysql.connector import connect
import os

# connecting to mysql database
mydb = connect(
    host='127.0.0.1',
    user='root',
    passwd=os.environ.get('sql_password'),
    database='testdb'
)

mycursor = mydb.cursor()
# Creating a table with 2 variables
# mycursor.execute("CREATE TABLE students (name VARCHAR(256), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)

# Writing a sql formula; (%s %s) is a placeholder
sqlFormula = (
    "INSERT INTO students (name, age)"
    "VALUES (%s, %s)"
)
data = [
    ("Adaa", 32),
    ("Anita", 40),
    ("Srinidhi", 28),
    ("Karishma", 37),
    ("Surbhi", 32),
    ("Sonarika", 28),
    ("Nia", 30),
    ("Erica", 28)
    ]

# Executing the formula in sql with the tuple
# it is always advisable to use sql queries in this
# form so as to avoid sql injection
mycursor.executemany(sqlFormula, data)
# Saving the databases
mydb.commit()
