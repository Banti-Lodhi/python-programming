# Magic or Special method
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def myfunc(self):
#         print("Hello my name is"+self.name + "and age is"+self.age)
# p1 = Person("John", 36)
# p1.myfunc()        
        
        
# 2.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __add__(self, other):
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Point(new_x, new_y)
# point1 = Point(9, 5)
# point2 = Point(8, 9)

# result = point1+point2
# print(result.x, result.y)

        
# print(dir(int))  

#new method
# class A(object): 
#     def __new__(cls): 
#          print("Creating instance") 
#          return super(A, cls).__new__(cls) 
  
#     def __init__(self): 
#         print("Init is called") 
  
# A()        
          
          
# class String:
#     def __init__(self, string):
#         self.string = string
        
#     def __repr__(self):
#         return 'Object: {}'.format(self.string)
    
#     def __add__(self, other):
#         return self.string + other
        
# if __name__ == '__main__':
    
#     string1 = String("Hello")
    
#     print(string1 ,' World')
    
#     print(string1 + ' Geeks') 

# Binary Operato/r

# class CustomerNumber:
#     def __init__(self, value):
#         self.value = value
        
#     def __add__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value + other.value)
    
#     def __sub__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value - other.value)
    
#     def __mul__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value * other.value)
    
#     def __floordiv__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value // other.value)
    
    
#     def __truediv__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value / other.value)
    
    
#     def __mod__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value % other.value)
    
    
#     def __pow__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value ** other.value)
    
    
#     def __lshift__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value << other.value)
    
    
#     def __rshift__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value >> other.value)
    
    
#     def __and__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value & other.value)
    
    
    
#     def __xor__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value ^ other.value)
    
    
#     def __or__(self, other):
#         # Custom addition logic
#         return CustomerNumber(self.value | other.value)
    
#     def __repr__(self):
#         # return f"CustomerNumber result => {self.value}"
#         return f"{self.value}"
    
# num1 = CustomerNumber(5)
# num2 = CustomerNumber(6)   
                      
# result = num1+num2
# result1 = num1-num2
# result2 = num1*num2
# result3 = num1//num2
# result4 = num1/num2
# result5 = num1%num2
# result6 = num1**num2
# result7 = num1<<num2
# result8 = num1>>num2
# result9 = num1&num2
# result10 = num1^num2
# result11 = num1|num2
# print(num1, "+", num2, "==", result)                      
# print(num1, "-", num2, "==", result1)                      
# print(num1, "*", num2, "==", result2)                      
# print(num1, "//", num2, "==", result3)                      
# print(num1, "/", num2, "==", result4)                      
# print(num1, "%", num2, "==", result5)                      
# print(num1, "**", num2, "==", result6)                      
# print(num1, "<<", num2, "==", result7)                      
# print(num1,">>", num2, "==", result8)                      
# print(num1, "&", num2, "==", result9)                      
# print(num1, "^", num2, "==", result10)                      
# print(num1, "|", num2, "==", result11)                      
                      
 
# #Assignment operator:-
# class Number:
#     def __init__(self, value):
#         self.value = value
        
#     def __iadd__(self, other):
#         print("__iadd__ method called")
#         self.value += other
#         return self
# num1 = Number(5)
# num2 = Number(6)

# num1 += num2.value
# print(num1.value)


# or

# class LogicNumber:
#     def __init__(self, value):
#         self.value = value
        
#     def __iadd__(self, other):
#         print("__iadd__ method called")
#         self.value += other
#         return self
            
#     def __isub__(self, other):
#         print("__isub__ method called")
#         self.value -= other
#         return self
    
            
#     def __imul__(self, other):
#         print("__imul__ method called")
#         self.value *= other
#         return self
               
#     def __ifloordiv__(self, other):
#         print("__iflooordiv__ method called")
#         self.value //= other
#         return self    
            
#     def __idiv__(self, other):
#         print("__idiv__ method called")
#         self.value /= other
#         return self
    
            
#     def __imod__(self, other):
#         print("__imod__ method called")
#         self.value %= other
#         return self
    
            
#     def __ipow__(self, other):
#         print("__ipow__ method called")
#         self.value **= other
#         return self
    
            
#     def __ilshift__(self, other):
#         print("__ilshift__ method called")
#         self.value <<= other
#         return self
    
            
#     def __irshift__(self, other):
#         print("__irshift__ method called")
#         self.value >>= other
#         return self
    
            
#     def __iand__(self, other):
#         print("__iand__ method called")
#         self.value &= other
#         return self
    
            
#     def __ixor__(self, other):
#         print("__ixor__ method called")
#         self.value ^= other
#         return self
    
#     def __ior__(self, other):
#         print("__ior__ method called")
#         self.value |= other
#         return self
    
# num1 = LogicNumber(60)
# num2 = LogicNumber(40)
          
# num1 += num2.value
# print(num1.value)

# num1 -= num2.value
# print(num1.value)

# num1 *= num2.value
# print(num1.value)

# num1 //= num2.value
# print(num1.value)

# num1 /= num2.value
# print(num1.value)

# num1 %= num2.value
# print(num1.value)

# num1 **= num2.value
# print(num1.value)

# num1 <<= num2.value
# print(num1.value)

# num1 >>= num2.value
# print(num1.value)

# num1 &= num2.value
# print(num1.value)

# num1 ^= num2.value
# print(num1.value)

# num1 |= num2.value
# print(num1.value)


class Student:
    stream = 'cse'
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
a = Student("Preetam Singh", 60483)
b = Student("Banti Kumar", 60673) 

print(a.stream, b.stream)
print(a.name,"'s roll is ", a.roll)       
print(b.name,"'s roll is ", b.roll)       
        