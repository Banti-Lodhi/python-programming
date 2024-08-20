# Class for computer student:
# class CSStudent:
#     stream = 'cse'
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
# # Object of CSStudent class:
# a = CSStudent('preetam Singh', 5)
# b = CSStudent('Banti kumar', 604963)
# print(a.stream, '/n')
# print(b.stream, '/n')
# print(a.name, '/n')
# print(b.name, '/n')
# print(a.roll, '/n')
# print(b.roll, '/n')

# # Class variables can be accessed using class
# print(CSStudent.stream)


# # Inheritence:-
# class Person(object):
#     # constructer
#     def __init__(self, name):
#         self.name = name
#     # To get the name
#     def getName(self):
#         return self.name
#     # To check if this person is employee
#     def isEmp(self):
#         return False
#     # Inheritence or sub
# class Emp(Person):
#     def isEmp(self):
#         return True
# #Driver Code
# emp = Person("Asian") #An Object of person
# print(emp.getName(), emp.isEmp())
# emp = Emp("Publishers")
# print(emp.getName(), emp.isEmp()) 
    

# Subclassing(Calling constructer of parent class)
# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name 
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name) 
#         print(self.idnumber)
# #child class
# class Emp(Person):
#     def __init__(self, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#         Person.__init__(self, post, idnumber)

# a = Person('Ram', 604963)
# a.display()        

# 2.Multiple Class:-
# class Base1(object):
#     def __init__(self):
#         self.str1 = "Asian"
#         print("Base1")

# class Base2(object):
#     def __init__(self):
#         self.str2 = "Publishers"
#         print("Base2")

# class Derived(Base1, Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#     def printStrs(self):
#         print(self.str1, self.str2)
# ob = Derived()
# ob.printStrs()            

# 3.Multilevel Inheritence
# class base(object):
#     def __init__(self, name):
#         self.name = name
#     #To get name
#     def getName(self):
#         return self.name
# class Child(base):
#     def __init__(self, name, age):
#         base.__init__(self, name)
#         self.age = age        
#     #To get the age
#     def getAge(self):
#         return self.age
# class GrandChild(Child):
#     def __init__(self, name, age, Address):
#         Child.__init__(self, name, age)
#         self.Address = Address
    
#     def getAdd(self):
#         return self.Address    
    
# g = GrandChild("Asian", 23, "Muzzaffarnagar")
# print(g.getName(), g.getAge(), g.getAdd())

# 4.Hierachical Inheritence
# class Details:
#     def __init__(self):
#         self.__id = "<No Id>"
#         self.__name = "<No name>"
#         self.__gender = "<No gender>"
#     def setData(self, id, name, gender):
#         self.__id = id 
#         self.__name = name
#         self.__gender = gender  
#     def showData(self):
#         print('id: ', self.__id)
#         print('name: ', self.__name)
#         print('gender ', self.__gender)


# class Employee(Details):
#     def __init__(self):
#         self.__company = "<No company>"
#         self.__dept = "<No Dept>"
#     def setEmployee(self, id, name, gender, company, dept):
#         self.setData(id, name, gender)
#         self.__company = company
#         self.__dept = dept
#     def showEmployee(self):
#         self.showData()
#         print('Employee\'s Company name: ', self.__company)
#         print('department: ', self.__dept)

# class Docter(Details):
#     def __init__(self):
#         self.__Hospital = "<hospital>"
#         self.__dept = "<department>"
#     def setEmployee(self, id, name, gender, hos, dept):
#         self.setData(id, name, gender)
#         self.__Hospital = hos
#         self.__dept = dept  
#     def showEmployee(self):
#         self.showData()
#         print("Hospital: ", self.__Hospital)
#         print("Department: ", self.__dept)  
# def main():
#     print('Empolyee Object')
#     e = Employee()
#     e.setEmployee(1, "Prem Sharma", "Male", "gmr", "excavation")
#     e.showEmployee()
#     print('\nDocter object')
#     d = Docter()
#     d.setEmployee(1, 'pankaj', 'male', 'aiims', 'eyes')
#     d.showEmployee()
# if __name__=="__main__":
#     main()    

# # 5.Hybrid Inheritence:
# class Parent:
#     def func1(self):
#         print('This is function one')
# class child(Parent):
#     def func2(self):
#         print('This is function 2')
# class child1(Parent):
#     def func3(self):
#         print('this is function 3')
# class child3(child1):
#     def func4(self):
#         print('This is function 4')        

# ob = child3()
# ob.func1()
# ob.func3()
# ob.func4()

# super() method in inheritence
# class Square:
#     def __init__(self, side): 
#         self.side = side 

#     def area(self):
#         return self.side* self.side    
# class Cube(Square):
#     def area(self):
#         face_area = self.side * self.side 
#         return face_area * 6 
#     def Volume(self):
#         face_area = self.side*self.side 
#         return face_area * self.side
# sq = Square()
# sq.area(4)

# or

# class Square:
#     def __init__(self):
#         pass
# class SquarePrism(Square):
#     def __init__(self):
#         pass
# class Cube(SquarePrism):
#     def __init__(self):
#         pass
# sq = Square()
# sqp = SquarePrism()
# cube = Cube()
# print(isinstance(sqp, Square))
# print(isinstance(cube, Square))


# Polymorphism:-
# class India:
#     def capital(self):
#         print('New Dehli is the capital of india')
#     def language(self):
#         print('Hindi is the primary language of india')
#     def type(self):
#         print('India is developing country') 
# class USA:
#     def capital(self):
#         print('Washington, D.C. is the capital of USA')
#     def language(self):
#         print('English is the primary language of USA')
#     def type(self):
#         print('USA is developing country') 
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# or
# class Bird:
#     def intro(self):
#         print('There are many types of birds can flight')
#     def flight(self):
#         print('Most of the birds can fly but some cannot')
# class sparrow(Bird):
#     def flight(self):
#         print('Sparrow can fly')
 
# class ostrich(sparrow):        
#     def flight(self):
#         print('ostrich can not fly')

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()


# or

class India:
    def capital(self):
        print('New Dehli is the capital of india')
    def language(self):
        print('Hindi is the primary language of india')
    def type(self):
        print('India is developing country') 
class USA:
    def capital(self):
        print('Washington, D.C. is the capital of USA')
    def language(self):
        print('English is the primary language of USA')
    def type(self):
        print('USA is developing country') 

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)