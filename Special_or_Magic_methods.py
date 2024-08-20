# # __new__()method:
# class emp:
#     def __new__(cls):
#         print("__new__ magic method is called")
#         inst = object.__new__(cls)
#         return inst
#     def __init__(self):
#         print("__init__ magic method is called")
#         self.name = "banti kumar"    

# print(emp())


# __str__() method
# class employee:
#     def __init__(self):
#         self.name = 'Swati'
#         self.salery = 10000
#     def __str__(self):
#         return 'name='+self.name+' salery=$'+str(self.salery)   
# print(employee())     

# __add__ method:-
# class distance:
#     def __init__(self, y = None, z = None):
#         self.ft = y
#         self.inch = z
#     def __add__(self, y):
#         temp = distance()
#         temp.ft = self.ft + y.ft
#         temp.inch = self.inch+y.inch
#         if temp.inch >= 12:
#           temp.ft += 1
#           temp.inch -= 12 
#           return temp 
#         def __str__(self):
#             return 'ft:'+str(self.ft)+'in: '+str(self.inch)
# d1 = distance(3, 10)
# d2 = distance(4, 4) 
# print('d1 = {} d2 = {}'.format(d1, d2))
         

# greater method
class distance:
    def __init__(self, x = None, y = None):
        self.ft = x
        self.inch = y
    def __ge__(self, x):
        val1 = self.ft*12+self.inch
        val2 = x.ft*12+x.inch 
        if val1 >= val2:
            return True
        else:
            return False   
   