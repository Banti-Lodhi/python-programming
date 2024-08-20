# #Input $ type casting
# a = eval(input("Enter the value1:- "))
# b = int(input("Enter the value2:- "))
# print(a+b)

##Conition statement


# /*if else */
# a = int(input("Enter the value: "))
# if a%2 == 0:
#     print(a, "Even number")
# else: 
#     print(a, "Number is odd")

# else, elif

# price = int(input("Enter number :- "))

# if price >= 60:
#     print("first div")
# elif price >= 40:
#     print("Second div")
# elif price >= 20:
#     print("third div")
# else:
#     print("Exit")

# Calculator

# num1 = int(input("Enter number1:- "))
# Oper = (input("Enter Operator:- "))
# num2 = int(input("Enter number2:- "))
 
# if Oper == '+':
#     print(num1+num2)
# elif Oper == '-':
#     print(num1-num2)
# elif Oper == '*':
#     print(num1*num2)
# elif Oper == '/':
#     print(num1/num2)
# elif Oper == '%':
#     print(num1%num2)
# elif Oper == '**':
#     print(num1**num2)
# else:
#     print("Invalid number")

# for loops -| 
# for n in range(6):
#     print(n)

# for m in range(1, 6):
#     print(m)

# for r in range(1, 6, 2):
#     print(r)


# for a in range(1, 11):
#     print("4 *", a, "==", 4*a)


# reverse for loop
# for a in range(10, -2, -4):
#     print(a)

# for a in range(10, 2, -3):
#     print(a)

# for a in range(10, 1, -2):
#     print(a)

# for a in range(10, 0, -1):
#     print(a)    

# While Loop
# i=1
# while i <= 10:
#     print(i)
#     i+=1

# i=10
# while i >= 1:
#     print(i)
#     i-=1

# # Strings 
# w= "Preetam Singh Lodhi"
# print(w[6])
# print(w[0::2]) #PetmSnhLdi
# print(w[-1::-1]) #ihdoL hgniS mateerP(reverse name)
# print(w[-1::-2]) #idLhnSmteP
# print(w[1::10]) #rg


# Strings iteration
# w = "Preetam Singh Lodhi"
# L = len(w)
# print(L)

# for a in range(L):
#     print(w[a])

# print("\n")
# # reverse name charcter
# for a in range(L-1, -1, -1):
#     print(w[a])

# w = "Singh"
# for a in w:
#     print(a )

# Lower, Upper, tittle, capitlize string

# w = "preetyam singh Lodhi"
# print(w.lower())
# print(w.upper())
# print(w.title())
# print(w.capitalize())

#String Function

# w = "preetam singh Lodhi"
# print(w.find('s', 5)) #start point 5 then search its start point
# print(w.index('t'))

# print(w.isalpha()) #Exists all alphabet string in string then true otherwise false
# print(w.isdigit())#Exists all Digit number in string then true otherwise false
# print(w.isalnum())#Exists only both alphabet and digit in string then true otherwise false


#char and ord function
# s = 65
# print(chr(s))

# s = 'z '
# print(ord(s))


# txt1 = "Welcome to {fname} {lname}".format(fname = "banti", lname = "Lodhi")
# txt2 = "Welcome to {0} {1}".format("preetam singh", "Rajput")
# txt3 = "Welcome to {} {}".format("Sanjay", "singh")
# print(txt1)
# print(txt2)
# print(txt3)

# l = [12, 41, 17, 23, 25]
# n = [4, 2, 7, 5]
# l.extend(n)
# print(l)


# # Space of 10 character in a wordline
# w = "Welcome{b:10} to {a}".format(b=40, a=30)
# print(w)
# # left side set point
# w = "Welcome{b:<20} to {a}".format(b="Preetam singh", a="Sanjay Singh")
# print(w)

# # Space of 10ch between in a line:-
# w = "Welcome{b:^20} to {a}".format(b="Preetam singh", a="Sanjay Singh")
# print(w)

# # Right side set point
# w = "Welcome{b:>20} to {a}".format(b="Preetam singh", a="Sanjay Singh")
# print(w)

# #26.List
# L=[1, 2, 3, 4, 5]
# print(L)

# print(L[3], L[4])

# print(L[0::2])

# print(L[0::1])

# print(L[-1::-2])
# #reverse
# print(L[-1::-1])

# List Iteration
# l = [20, 10, 40, 50, 80, 70, 90]
# print(l)
# print()
# print()
# t = len(l)
# for p in range(t):
#     print(l[p])

# # reverse print to point
# for p in range(t-1, -1, -1):
#     print(l[p])

# :-Function in List
# l = [20, 10, 40, 50, 80, 70, 90]
# del l[1] #Delete node
# print(l)

# print()

# print(l.pop(2)) #index pop
# print(l)

# print()

# l.remove(40) #index value remove
# print(l)

# print()

# l.clear()
# print(l)


#Update Element:-
# l = [20, 10, 40, 50, 80, 70, 90]
# l[0] = 30 #insert value in index 0
# print(l)
 
# print()

# l.insert(2, 12)
# print(l)

# print()
# #l.append(54)#insert the value in ending point
# # n = [63, 45]
# # l.append(n)
# # print(l)

# print()
# p = [63, 45]
# l.extend(p)#insert the value in array such that list of array of same array and no change in array
# print(l)

# #List comprehension elegent way to create lists:-
# l=[]
# # self array self call
# n = [h for h in range(1, 21)  if h%2 == 0]
# print(n)

# # String pass in array
# s = "Preetam Singh"
# d = [n for n in s]
# print(d)

# 31.count(), max(), min(), sort(), reverse(), Index() fiunction

# n = [30, 60, 40, 80, 70, 90, 40, 80, 40, 80]

# s = n.count(80)
# print(s)

# d = max(n)
# print(d)

# e = min(n)
# print(e)

# n.sort()
# print(n)

# n.reverse()
# print(n)

# l=n.index(80)
# print(l)

# zip Function-Iterate ovr2 + lists at the same time

# n = [30, 60, 40, 80, 70]
# m = [20, 30, 40, 50, 80]

# t = len(n)
# for a, b in zip(n, m):
#     print(a, b)
# for p in range(t):
#     print(n[p], m[p])

# # 33.Convert string to a List
# n = input("Enter the string")
# print(n)
# l = n.split()
# print(l)

# l= []
# for a in range (0, 4):
#     n=input("Enter the value "+ str(a)+":-")
#     l.append(n)
#     print(l)

# Stack Operations
# l = []
# while True:
#  c = int(input('''
# 1 push Elements
# 2 pop Elements
# 3 peek Elements
# 4 Display Elements
# 5 Exit
# '''))

#  if c == 1:
#     n = input("Enter the push value :-")
#     l.append(n)
#     print(l)
#  elif c == 2:
#     if len(l) == 0:
#         print("Stack Empty")
#     else:
#         p = l.pop()
#         print(p)
#         print(l)
#  elif c == 3:
#      if len(l) == 0:
#         print("Stack Empty")
#      else:
#          print("display last element of stack ",l[-1])     
#  elif c == 4:
#     print("display element ", l)
#  elif c == 5:
#     break
#  else:
#     print("Invalid opr......")

#Queue Operations
# l = []
# while True:
#  c = int(input('''
# 1.push Elements
# 2.pop First Element
# 3.front Element
# 4.last Element
# 5.Display Queue
# 6.Exit
# '''))

#  if c == 1:
#     n = input("Enter the push value :-")
#     l.append(n)
#     print(l)
#  elif c == 2:
#     if len(l) == 0:
#         print("Stack Empty")
#     else:     
#         del l[0]     
#         print(l)
#  elif c == 3:
#      if len(l) == 0:
#         print("Stack Empty")
#      else:
#          print("display front element of Queue ",l[0])   
#  elif c == 4:
#      if len(l) == 0:
#         print("Stack Empty")
#      else:
#          print("display last element of Queue ",l[-1])     
#  elif c == 5:
#     print("display Queue ", l)
#  elif c == 6:
#     break
#  else:
#     print("Invalid opr......")

# Dictionary
# d = {
#      'name':'python',
#      'fees':'1000',
#      'duration':'2Months'                    
# }
# #print(d) #print dictionary
# print(type(d))
# print(d['name']) #print key value

# for n in d:
#     print(d[n])


#35.Dictionary function
# d = {
#      'course':'python',
#      'fees':'1000',
#      'duration':'2 Months'                    
# }

#get function:-
# c = d.get('course')
# c1 = d['course']#same both get method
# print(c)
# print(c1)

#keys function:-
# for k in d.keys():
#     print(k)

# # Values function:-
# for v in d.values():
#     print(v)

#items function:-
# for a, b in d.items():
#     print(a+" == "+b)
    
#del, pop function:-
# del d['course']
# print(d) 

# print(d.pop('duration'))
# print(d)

# dict() function:-
# d = dict(course = 'python', Quantity = '3 months')
# print(d)

# update function:-
# d.update({'fees':120000})
# print(d)

# clear function:-
# d.clear()
# print(d)

#insert function:-
 
# d['About'] = "thia is python tutorials"

# print(d)


# # Nested dictionary 
# course = {
#     'php':{'duration':' 3 Months', 'fees':15000},
#     'java':{'duration':' 3 Months', 'fees':15000},
#     'python':{'duration':' 3 Months', 'fees':15000},
# }

# print(course)
# #update  
# course['java']['fees'] = 45000
# print(course['python']['fees'])

# for k, v in course.items():
#     print(k, v['duration'], v['fees'])    
# print(k, v)
     

# Tuple
# t = (12, 23, 45, 85, 47, 56)
# print(type(t))
# I = t[5]
# print(I)

# l = len(t)
# for a in range(l):
#     print(t[a])

# for a in t:
#  print(a)

# m = min(t)
# print(m)
# m = max(t)
# print(m)

# c = t.count(85)
# print(c)

# i = t.index(85)
# print(i)

# s = sum(t, 10)
# print(s)

# Sets
# s = {10, 20, 30, 40}
# s.remove(20)
# s.discard(20)
# print(s.pop())
# print(s)
# s.clear()
# s.add(15)

# l  = [10, 60, 70, 80, 90]
# s.update(l)
# print(s)



#40.function parameter-->>>>
# 1. simlpe function:-
# def showdata():
#    print("Welcome to Preeatm singh")  
# showdata() 
# showdata() 
# showdata() 

# # 2.argument function
# def sumfun(a, b):
#     print(a+b)
# sumfun(20, 63)
# sumfun(20, 65)
# sumfun(20, 60)

# Default Prameter function
# def default(a, b = 5):
#     print(a+b)
# default(20)
# default(20, 12)

# # return statement
# def square(x):
#     return x*x, x*2
# s = square(6)
# print(s)         

#  Module Function:-
# def sum(a, b):
#     c = a + b
#     return c

# def mul(a, b):
#     c = a * b
#     return c

# import python2
# print(python2.sum(10, 20))
# print(python2.mul(10, 20))

# import python2 as m
# print(m.sum(10, 20))
# print(m.mul(10, 20))

# from python2 import sum

# print(sum(50, 60))
# print(mul(50, 60))
  
# import math

# Ceil function:-
# x = 10.5
# print(math.ceil(x))
# fabs function:-
# x = -10
# print(math.fabs(x ))
# # factorial function:- 
# x = 5
# print(math.factorial(x ))

# floor function:-
# x = 10.5  #remove float value and return 10
# print(math.floor(x))

# l = [10, 20, 30, 40]
# print(math.fsum(l))

# Square function:-
# print(math.sqrt(81))



# Random Module:-
# import random

# n=random.randint(5, 10)
# print(n)

# n1 = random.randrange(2, 9)
# print(n1)

# l = [10, 20, 30, 40, 50]
# print(random.choice(l))
# print(random.random())

# random.shuffle(l)
# print(l) 

# print(random.uniform(3, 9)) 


# datetime module:-
# import datetime

# x = datetime.datetime.now()
# print(x)
# print(datetime.datetime(2023, 9, 27))
# print(x.strftime("%Y")) #print year
# print(x.strftime("%M")) #print month
# print(x.strftime("%D")) #print current date
# print(x.strftime("%b")) #short name of month
# print(x.strftime("%B")) #full name of month
# print(x.strftime("%H")) #time period in 24 hour
# print(x.strftime("%I")) #time period in 12 hour
# print(x.strftime("%p")) #time period in AM/PM time

# from datetime import datetime

# print(datetime.now().microsecond) #print microsecond
# print(datetime.now().second) #print second
# print(datetime.now().minute) #print minute

