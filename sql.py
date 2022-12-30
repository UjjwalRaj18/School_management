import mysql.connector as sql
connt=sql.connect(host="localhost",user="root",password="ujjwalraj",database="school_management")

def enrollment():
    Day = input("Day erolled : ")
    Name = input("Name : ")
    date = input("Class : ")
    type_num = input("Student Number : ")
    data = (Day,Name,date,type_num)
    sql = 'insert into enrollment values(%s,%s,%s,%s)'
    c=connt.cursor()
    c.execute(sql,data)
    connt.commit()
    print("Alrighty,Data has been successfully entered :)")
    main()

def enrolled_out():
    type_num=input("Student Number : ")
    name= int(input("Name : "))
    Duefees = int(input("Due Fees : "))
    Stnd = int(input("class : "))
    date=input("Date_enrolledout : ")
    datas = (type_num,name,Duefees,Stnd,date)
    sql = 'insert into enrolled_out values(%s,%s,%s,%s,%s)'
    c=connt.cursor()
    c.execute(sql,datas)
    connt.commit()
    print("Alrighty,Data has been successfully entered :)")
    main()

def main():
    print("1.enrollled_in")
    print("2.enrolled_out")
    inp=int(input("choice: "))
    if inp==1:
        enrollment()
    elif inp==2:
        enrolled_out()
    else:
        print("incorrect choice")
        main()
main()