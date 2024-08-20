#1. class Student:
#     name = "Karan Singh"
# std = Student()
# print(std.name)    
# print(std.name)    
# print(std.name)    
# print(std.name)    

# 2.
# class Car:
#     color = "blue"
#     model = "spinga"

# car1 = Car()
# print(car1.color)    
# print(car1.model) 

#init function:-
# class Student:
#     print("add new student in databse..") 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
     
# s1 = Student("karan", 94)
# s2 = Student("Arjun", 84)
# print([s1.name, s1.marks], end=", ")
# print([s2.name, s2.marks])


# Practicec set:-
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "to your score is:", sum/3)           
# s1 = Student("karan Kumar", [45, 56, 19])
# s1.get_avg()  

# abstraction:-
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False

#     def car_run(self):
#         self.acc = True
#         self.brk = True
#         print("Car Started..")
# car1 = car()
# car1.car_run()            

# Let's Practice:-
# Crate Account class with 2 attributes-balance 
# & account methods for debit, credit & printing 
# the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance:", self.get_balnace())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance:", self.get_balnace())

    def get_balnace(self):
        return self.balance    
    
acc1 = Account(10000, 843875)
acc1.debit(45000)
acc1.credit(5000)
acc1.get_balnace()
