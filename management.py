import mysql.connector as sql 
connt= sql.connect(host="localhost",user="root",password="ujjwalraj")
c=connt.cursor()
sql1="create database school_management"
c.execute(sql1)
sql2="use school_management"
c.execute(sql2)
##datatypes - varchar and integer respectively
sql3="create table enrollment (Date_enrolled varchar(40),Name varchar(20),Class varchar(20),Student_number integer)"
c.execute(sql3)
sql4 = "create table enrolled_out(Date_enrolledout varchar(30),Name integer, Class integer, fees integer,Student_number integer)"
c.execute(sql4)
connt.commit()
