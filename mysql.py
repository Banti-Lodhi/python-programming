import mysql as mq

# # Server name
# myobj=mq.connect("localhost", "root", "")
# cursorobj=myobj.cursor()
# try:
#     db="create database school"
#     cursorobj.execute(db) 
#     print("Database created")
# except:
#     print("database error..")    


# Connection & Crete Database;=
 
# import mysql as mq

# myobj = mq.connect("localhost", "root", "")
# cursorobj = myobj.cursor()
# try:
#    db = "create database school"
#    cursorobj.execute(db)
#    print("data created")

# except:
#     print("databasse error ..")   


# conn=mq.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="school"
# )

# create table student data tanle:== 
# mysqlc=conn.cursor() 
# # create table:--
# tc="create table student(st_id INT primary key auto_increment, st_name varchar(50), st_class(10), st_email(20))"
# mysqlc.execute(tc)    

# Insert data in the table:==
# myobj=mq.connect("localhost", "root", "", "school")
# mycursor=mysql.cursor()
# try:
#     ins = "INSERT INTO std_py(st_name, st_class, st_email) values(%s, %s ,%s)"
#     t=("ram", "12th", "ram@gmail.com")
#     mucursor.execute(ins, t)
#     mysql.commit();
#     print("Insert Data")
# except:
#     print("Error...")
