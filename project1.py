# 61.SQLite in Python
# connect SQLite, Create Table:
# import sqlite3

# Connect file to the database:--
# conn = sqlite3.connect("sqlite3.db")
# Create Table:--
# conn.execute ('''
# Create table Student (
#      st_id INT AUTO INCREMENT PRIMARY KEY,
#      st_name VARCHAR(50),
#      st_class VARCHAR(10),
#      st_email VARCHAR(30)
# );
# ''')
# conn.close()

# Data insert in the file
# ins = '''
#    insert into Student VALUES
#    (101, 'HariOm', 'Mtech', 'HarOmi1254@gmail.com'),
#    (102, 'Hari', 'Btech', 'Hari1254@gmail.com'),
#    (103, 'Om', 'BSC', 'Om1254@gmail.com'),
#    (104, 'Goga Ji', 'B.COM', 'GogaJI1254@gmail.com')
  
# '''
# conn.execute(ins)
# conn.commit()
# conn.close() 


# display data on python command:--
# data = conn.execute("SELECT * FROM  Student limit 1, 3")
# print("St_id " ,"St_name ", "St_class ","St_mail")
# for n in data:
#    # print(n)
#    print(n[0],"  ",n[1],"   ",n[2],"  ", n[3])


# 65.Delete Command Query:--
# data = conn.execute("SELECT * FROM  Student")
# print("St_id " ,"St_name ", "St_class ","St_mail")
# for n in data:
#    print(n)
# st_id = input("Enter the student id:-")
# conn.execute("DELETE FROM Student where st_id="+st_id)
# print(n)
# conn.commit()
# conn.close()


# # 65.UPDATE Command Query:--
# import sqlite3

# conn = sqlite3.connect("sqlite3.db")
# conn.execute('''
#  t_id=102
# ''')  
# conn.commit()
# conn.close()

# # 65.Searching Command Query:--
# data = conn.execute("SELECT * FROM  Student")
# print("St_id " ,"St_name ", "St_class ","St_mail")
# for n in data:
#    print(n[0],"  ",n[1],"   ",n[2],"  ", n[3])
# print()
# print()


# st_name = input("Enter thee student name:--")
# st_class = input("Enter thee student Class:--")
# # data = conn.execute("SELECT * FROM  Student where st_name='"+st_name+"'")
# data = conn.execute("SELECT * FROM  Student where st_name like '%"+st_name+"%' and st_class like '%"+st_class+"%' ")

# for n in data:
#       print(n[0],"  ",n[1],"   ",n[2],"  ", n[3])

# conn.commit()
# conn.close()





#SQLite Join:--
# conn.execute('''
# create table fee(
# fees_id int auto increment primary key,
# st_id int(10),
# fees_Amount int(20)
# )
# ''')
# conn.commit()
# conn.close() 
     
# conn.execute('''
# insert into fee values
# (2, 101, 2000),
# (3, 102, 1000),
# (4, 103, 4000),
# (5, 101, 1200),
# (6, 102, 2300),
# (7, 102, 5000)
# ''')
# conn.commit()
# conn.close()             

# inner join:--
# data = conn.execute("select s.st_id, s.st_name, f.fees_Amount from fee as f inner join Student as s on f.st_id=s.st_id")
# for a in data:
#     print(a)
# conn.close()    


