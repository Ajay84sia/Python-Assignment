# Day 7 Assignment - Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sql           # importing module

# Connecting the local mysql database
import mysql.connector as sqlcon
db = sqlcon.connect(host = 'localhost', user = 'root', passwd = 'system', database = 'essentials')

cur = db.cursor()


cur.execute("update student set marks = 95 where sname = 'Ajay'")     # Update the record 
cur.execute("select * from student")        # View the table

for i in cur:
    print(i)

cur.close()
db.commit()       # commit changes or save changes.