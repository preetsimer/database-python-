
#question 1
import sys
import sqlite3
con=sqlite3.connect('Students.db')

#question 2
cursor = con.cursor()
query = 'create table stu_details(Name varchar(20),Marks int(3))'
cursor.execute(query)
con.commit()
for i in range(1,11):
    names=input("Enter name: ")
    marks=int(input("Enter marks:  "))
    if marks>=0 and marks<=100:
        #question 3
        cursor.execute("insert into stu_details values(?, ?);",(names,marks))
    else:
        print("Invalid marks!! please try again and enter correct details")
        sys.exit()    
con.commit()    
print("10 rows inserted successfully\n")


#question 4
import sqlite3
con=sqlite3.connect('Students.db')
cursor = con.cursor()
query = 'select * from stu_details where marks>80'
cursor.execute(query)
data = cursor.fetchall()
for row in data:
        print('Name: {}, Marks: {}'\
             .format(row[0], row[1]))   
cursor.close()
con.close()
