import sqlite3

##connet to the sqlite3 database

connection = sqlite3.connect('student.db')

#  create a cursor object to insert record,create table,retrieve record
cursor = connection.cursor()

# create the table
table_info = """CREATE TABLE student(NAME VARCHAR(25),CLASS VARCHAR(25),section VARCHAR(25),MARKS INT);"""

cursor.execute(table_info)

# INSERT SOME RECORDS

cursor.execute("INSERT INTO student VALUES('John','5th','A',90)")
cursor.execute("INSERT INTO student VALUES('Doe','5th','B',80)")
cursor.execute("INSERT INTO student VALUES('Mark','5th','C',70)")
cursor.execute("INSERT INTO student VALUES('Smith','5th','D',60)")

# DISPLAY all THE RECORDS

print("All the records in the table are:")

data = cursor.execute("SELECT * FROM student")

for row in data:
    print(row)

# commit the connection
connection.commit()

# close the connection
connection.close()


