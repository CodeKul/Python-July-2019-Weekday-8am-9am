import mysql.connector  # pip install mysql-connector-python

mydb = mysql.connector.connect (
    host="192.168.0.6",
    user="root",
    passwd="root@123",
    database="EmployeeDB"
)
mycursor = mydb.cursor()


# # create table
# mycursor.execute("CREATE TABLE Employee (name VARCHAR(255), email VARCHAR(255))")
# print("Table is created...")


# # Insert into table
# sql = "INSERT INTO Employee (name, email) VALUES (%s, %s)"
# val = ("PQR", "PQR@XYZ.COM")
# mycursor.execute(sql, val)
# mydb.commit()
# print("data inserted...")


# # Select from table
# mycursor.execute("SELECT * FROM Employee")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# Where clause
sql = "SELECT * FROM Employee WHERE email ='ABC@XYZ.COM'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)