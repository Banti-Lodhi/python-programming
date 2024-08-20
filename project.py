
# #1. Number guessing game python (Using Random Module)
# import random

# Cnumber = random.randrange(1, 101)
# userInput = int(input("Enter your number:---"))
# if userInput>Cnumber:
#     print("Computer Nmumber", Cnumber)
#     print("Your guess number is too high")
# elif userInput<Cnumber:
#     print("Computer Nmumber", Cnumber)
#     print("Your guess number is too low")
# else:
#     print("Computer Nmumber", Cnumber)
#     print("Your guess number is equal")


# # 2.Rock, paper, scissors game:-
# l = ["rock", "scissor", "paper"]
# while True:
#     ccount=0
#     ucount=0
#     uc = int(input('''
# Game Start.....
# 1 yes
# 2 No | Exit

#     '''))
#     if uc == 1:
#         for a in range(1, 6):
#             userInput = int(input('''
# 1 Rock
# 2 Scissor
# 3 Paper
#             '''))
#             if userInput == 1:
#               uchoice="rock"
#             elif userInput == 2:
#                 uchoice="scissor"
#             elif userInput == 3:
#                 uchoice="paper"
#             else:
#              print("Invalid choice")
#              break
#             Cchoice=random.choice(l)
        
#             if uchoice == Cchoice:
#                 print("user choice",uchoice)
#                 print("Computer choice",Cchoice)
#                 print("draw game")
#                 ucount+=1
#                 ccount+=1
#             elif(uchoice=="rock" and Cchoice == "scissor")or(uchoice=="scissor" and Cchoice == "paper")or(uchoice=="paper" and Cchoice=="rock"):
#                 print("User choice",uchoice)
#                 print("Computer choice",Cchoice)
#                 print("you win")
#                 ucount+=1
#             else:
#                 print("user choice",uchoice)
#                 print("Computer choice",Cchoice)
#                 print("Computer win")
#                 ccount+=1
#         if ucount == ccount:
#                   print("Final Game draw!")
#                   print("User Score", ucount)
#                   print("Compter Score",ccount)
#         elif ucount > ccount:
#             print("Final user win!")
#             print("User Score", ucount)
#         else:
#             print("Fianl Computer Win!")
#             print("Compter Score",ccount)  
#     else:
#         break;                              


# 44.Json in python

# Python pickle function:-
# import pickle

# l = [10,20,30,40,50]
# file = open("project2.py", "wb")

# pickle.dump(l, file)
# file.close()

# file = open("project2.py", "rb")

# l = pickle.load(file)
# print(l)

# json import package function:-
# import json

# d = {'course':'python',
#      'fee':15000    
# }

# f = json.dumps(d)
# print(type(d))
# print(type(f))
# print(f)
  
# d = '{"C_name":"Python", "fees":12000, "Duration":"2 Months"}'
# x = json.loads(d)
# print(type(d))
# print(type(x))
# print(x)

# for a in x:
#     print(a, x[a ])

# Reading and Writing json file in python:-
# file = open("posts.json")
# x = file.read()
# finaldata = json.loads(x)
# print(finaldata)

# for a in finaldata:
#     print(a['title'], a['userId'])



#51. oop in python(Class && Object):===
# =Python def keyword is used to define a 
# function, it is placed before a function 
# name that is provided by the user to
# create a user-defined function. 
# In Python, a function is a logical unit of 
# code containing a sequence of statements
# indented under a name given
# using the “def” keyword.


# class DemoClass:
#     a=10
#     def sumvalue(self):
#         print(45+56)
    
# demoobject = DemoClass()
# print(demoobject.a)
# demoobject.sumvalue()

# 52.Methods and Constructers:
# class DemoClass:
#     a=10
#     def __init__(self):
#         print("Preetam Singh")
#     def showvalue(self):
#         print(self.a) 
#     def showvalue1(self, a, b):
#         print(a+b)
# obj = DemoClass()
# obj.showvalue()
# obj.showvalue1(12, 14)      
  
#54. Inheritence in Python:-
# class A:
#     def displayA(self):
#         print("Preetam Singh A")
# class B:
#     def displayB(self):
#         print("Preetam Singh B")        
# class C:
#     def displayC(self):
#         print("Preetam Singh C") 
# class D(A, B, C):
#     def displayD(self):
#         print("Preetam Singh D") 
# obj = D()
# obj.displayA()
# obj.displayB()
# obj.displayC()
# obj.displayD()

# 55. getter And setter method:-
# class Student:
#     def __init__(self):
#         self.__name=""
#     def getname(self):
#         return self.__name
#     def setname(self, name):
#         self.__name = name    
# obj = Student()
# obj.setname("Testing")
# name = obj.getname()
# print(name)



# Encapsulation:=
# from collections.abc import Iterable

# class Student:
#     __name = "Ravi"
#     def __init__(self):
#         print(self.__name)
#         self.__displayinfo()
#     def __displayinfo(self):
#         print("Welcome to Wscubetech")
#         print("Narendra Modi")   

# Student()            

# Polymorphism:=
# class Ws:
#     def displayinfo(self, name = ''):
#         print("Welcome to wstech "+name)
# obj = Ws()
# obj.displayinfo()
# obj.displayinfo('python')

# 2.

# class Ws:
#     def displayinfo(self):
#         print("Welcome to wstech")
# class IIP(Ws):
#     def displayinfo(self):
#         super().displayinfo()
#         print("Welcome to IIP")
# obj = IIP()
# obj.displayinfo()        
 

#  57. Method Overloading:=
# class Area:
#     def findArea(self, l=0, w=0):
#         if l!=0 and w!=0:
#             print('Area of Rectangle:-',l*w)
#         elif l!=0:
#             print("Area of Square", (l*l))    
#         else:
#             print("Nothiing Value find")    

# obj=Area()
# obj.findArea()
# obj.findArea(10)
# obj.findArea(10, 20)

# #  Method Overriding:=
# class A:
#     def showData(self):
#         print('A')
# class B(A):
#     def showData(self):    
#         print('B')
# obj = B()
# obj.showData()

# 58. Bike Rent System:-
# class bikeShop:
#     def __init__(self, stock):
#         self.stock = stock
#     def displayBike(self):
#         print("Total Bike ", self.stock)    
#     def rentForBike(self, q):

#         if q<=0:
#             print("Enter the positive value or greater than zero")
#         elif q >= self.stock:
#             print("Enter the value (less than stock)")
#         else:
#             self.stock -= q
#             print("Total prices ", q*100)            
#             print("Total Bikes ", self.stock)

# while True:
#    obj = bikeShop(100)
#    uc = int(input('''
#    1 Display Stocks
#    2 Rent a Bike 
#    3 Exit
#    '''))
#    if uc == 1:
#        obj.displayBike()
#    elif uc == 2:
#        n = int(input("Enter The Qty:---"))
#        obj.rentForBike(n)   
#    else:
#         break 

# 59. Errors in Built or Exceptions:-
# a=10
# b=20
# if a == b
#     print("No")
# else
#     print("Yes") 

#Python Logical Errors(Exceptions)
# print(1/0) 
# l=[10, 20, 30]
# print(l[4])



# 61.SQLite in Python
# connect SQLite, Create Table:
import sqlite3

conn = sqlite3.connect("sqlite3.db")
conn.execute ('''
Create table Student (
                    st_id INT Auto_Increment Primary Key,
                    st_name varchar(20),
                    st_name varchar(10),
                    st_email varchar(30)

);
''')
conn.close()

