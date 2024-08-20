# x=5
# y=6
# print(x&y, bin(x&y))
# print(x|y, bin(x|y))
# print(x^y, bin(x^y))

# i = 12
# if(i == 11):
#     if(i<15):
#         print("i is less than 15")

#     if(i<12):
#         print("i is less smaller to")
#     else:
#         print(i, "is grater than 15")
# else:
#     print("Hi hello!")

# list = ['s', 'p', 'w', 'o', 'd']
# print(type(list))

# tuple1 = ('s', 'p', 'w', 'o', 'd')
# print(type(tuple1))

# dict = {1:'s', 2:'p', 3:'w', 4:'o', 5:'d'}
# print(type(dict))

# set = {1, 2, 3, 4}
# print(type(set))


# #simle
# for i in range(6):
#     print(i)
# #increment per nnumber +3=> 1, 4 return
# for i in range(1, 6, 3):
#     print(i)
# #reverse
# for i in range(10, 1, -2):
#     print(i, " ")

# while loop
# i=10
# while i >= 1:
#     print(i)
#     i-=1

# String:-
# w = "Preetam Singh"
# print(w[6])

# print(w[0::2])
# print(w[:-1])
# print(w[::-1])
# print(w[0])

# print(w[8])
# for i in range(len(w)-1, -1, -1):
#     print(w[i])

# print(w.upper())
# print(w.lower())
# print(w.title())
# print(w.capitalize())
# print(w.find('r'))
# print(w.index('S'))
# print(w.isalpha())
# print(w.isdigit())
# print(w.isalpha())
# print(w.isascii())

# l = [1, 2, 3, 4, 5]
# print(l[0:2])
# print(l[3], l[4])
# print(l[0::2])
# print(l[-1::-2])


# print(w.remove(w.index('S')))


# temp = input("Enter the value in F and celcius\n")

# degree = int(temp[:-1])

# i_convention = temp[-1]

# if i_convention.upper() == 'F':
#    result = int(round(5/9*(degree-32)))
#    o_convention = 'Celcius'
# elif i_convention.upper() == 'C':
#    result = int(round((degree)*9/5+32))
#    o_convention = 'Fareneheit'
# else:
#    print("Enter Proper convention of temp")
# print("the tempeture in", o_convention, "is", result, "degree")

# # chr, ord
# y = chr(65)
# print(type(y), y)

# s = 'B'
# print(ord(s))

# l = [20, 30, 40, 50, 60, 70]
# del l[1]
# # print(l)
# print(l.pop(2))
# print(l)


# l.clear()
# print(l)

# print(l[0])
# l.insert(0, 10)
# print(l)

# l.append(80)
# print(l)

# l.extend([90, 45, 75, 25, 65])
# print(l)
# l=[]
# for n in range(1, 101):
#     l.append(n)
# print(l)

# n = [h for h in range(1, 25) if h%2 == 0]
# print(n)

# s = 'preetam singh'
# d = [g for g in s]
# # print(d)

# l = ['p', 'r', 'e', 'e', 't', 'a', 'm', ' ', 's', 'i', 'n', 'g', 'h']
# l1 = [20, 30, 40, 50, 60, 70, 12, 15, 7, 8, 8]
# print(l.count('e'))
# print(max(l))
# print(min(l1))
# l.sort()
# print(l)
# l.reverse()
# print(l)

# print(l.index('m'))
# l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # for a, b in zip(l, l1):
# #     print(a, b)
# t = len(l)
# for p in range(t):
#     print(l[p], l1[p])


# input = input("Enter the string\n")
# print(input)

# l = input.split()
# print(l)


# l = []
# for a in range(1, 4):
#     n = input("Enter the value "+str(a)+":-")
#     l.append(n)
# print(l)

# l = []
# while True:
#     c = int(input('''
#     1.Push Elements
#     2.pop Element
#     3.peek Element
#     4.Display Element
#     5.Exit
#     '''))
#     if c==1:
#         n=input('Enter the value:\n')
#         l.append(n)
#         print(l)
#     elif c==2:
#         if(len(l)==0):
#             print("Empty list n remove Element:")
#         else:
#             p = l.pop()
#             print(p)
#             print(l)
#     elif c == 3:
#         if(len(l)==0):
#             print("Empty list n remove Element:")
#         else:
#             p = l[-1]
#             print("Last stack value", p)
#     elif c==4:
#         print(l)
#     elif c == 5:
#         break;
#     else:
#         print("Invalid opr...")


# # print(d['course'])
# list = []
# while True:
#      curr = int(input('''
#      1. Push Element
#      2. Pop Element
#      3. front Element
#      4. last Element
#      5. Display Queue
#      6. Exit
#      '''))
#      if curr == 1:
#           n = int(input('Enter the value\n'))
#           list.append(n)
#      elif curr == 2:
#           if(len(list) == 0):
#                print('Empty Queue n pop element in this queue')
#           s = list.pop()
#           print(s)
#           print(list)
#      elif curr == 3:
#           e = list[0]
#           print('First element of queue:', e)
#      elif curr == 4:
#           r = list[-1]
#           print('Last element of queue:', r)
#      elif curr == 5:
#           print('queue element:', list)
#      elif curr == 6:
#           break;
#      else:
#           print("Default Oper...")


# d = {
#     'course':'python',
#     'duration':'2 Months',
#     'fees':8000
# }
# p = d.get('course')
# print(p)
# for k in d.keys():
#     print(k)
# for v in d.values():
#     print(v)

# for a, b in d.items():
#     print(a, " == ", b)
# d.update({'fees':45000})
# print(d)

# d.clear()
# print(d)

# d.insert function:
# d['About'] = 'Course is more beneficial for our education:'
# print(d)

# courses = {
#     'php':{'duration':'2 Months', 'fees':45000},
#     'java':{'duration':'3 Months', 'fees':45009},
#     'python':{'duration':'4 Months', 'fees':45050}
# }

# for k, v in courses.items():
#     print(k, v['duration'], v['fees'])
# print(k, v)
#
# tuple = (50, 20, 30, 40, 10)
# # add_number = sum(tuple)
#
# print(tuple)

# tuple = {50, 20, 30, 40, 10}
# tuple.discard(20) #that's mean deletes function
# print(tuple)

# s={10, 20, 30, 40}
# l=[10, 50, 60, 70, 80]
# s.update(l)
# print(s)

# def showdata():
#     print('Hello')
# showdata()
# showdata()


# def sum(a, b):
#     print(a+b)
# sum(13, 45)
# sum(12, 15)

# (II)Function with argument
# def function(a, b=4):
#     print(a*b)
# function(3)
# function(9)


# Return type
# def Square(x):
#     return x*x
# print(Square(4))
# print(Square(5))


# module function
# def sum(a, b):
#     c = a+b
#     return c
# def mul(x, y):
#     z=x*y
#     return z

# import python2

# print(python2.sum(10, 20))
# print(python2.mul(10, 20))


# import python2 as m

# print(m.sum(50, 60))
# print(m.mul(50, 60))


# from python2 import sum

# print(sum(50, 60))
# from python2 import mul

# print(mul(50, 60))

# 1.ceil
# import math

# x = 10.5
# print(math.ceil(x))

# x = -10
# print(math.fabs(x))

# x=5
# print(math.factorial(x))

# x = 10.5
# print(math.floor(x))

# l = [10, 20, 30, 40, 50, 60]
# print(math.fsum(l))

# print(math.sqrt(3))


# import random

# print(random.randint(5, 10))
# x=random.randrange(2, 10)
# print(x)
# l = ["apple", "banana", "chery", "Pine_Apple"]
# print(random.choice(l))

# print(random.random())
# l = [10, 20, 30, 40, 50, 60]
# random.shuffle(l)
# print(l)

# print(random.uniform(3, 9))

# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime(2021, 1, 18))
# from datetime import datetime

# x=datetime.datetime.now()
# print(x.strftime("%Y")) #print year
# print(x.strftime("%M")) #print month
# print(x.strftime("%D")) #print current date
# print(x.strftime("%b")) #short name of month
# print(x.strftime("%B")) #full name of month
# print(x.strftime("%H")) #time period in 24 hour
# print(x.strftime("%I")) #time period in 12 hour
# print(x.strftime("%p")) #time period in AM/PM time

# # print(datetime.now().microsecond) #print microsecond
# # print(datetime.now().second) #print second
# # print(datetime.now().minute) #print minute

import random

l = ["rock", "sessior", "paper"]
while True:
    U_count = 0
    C_count = 0

    user_choice = int(input('''
         Game Start...
          1. yes | Start
          2. No | Exit
    '''))
    if user_choice == 1:
        for a in range(1, 6):
            u_input = input('''
            1.'rock',
            2.'Sessior', 
            3.'paper'
    ''')

            if u_input == 1:
                u_choice = 'rock'
            elif u_input == 2:
                u_choice = 'Sessior'
            elif u_input == 3:
                u_choice = 'paper'
            else:
                print('Invalid Choice!')
                break
            c_choice = random.choice(l)

            if u_choice == c_choice:
                print('Computer choice', c_choice)
                print('uchoice', u_choice)
                print("Game Draw!")
                C_count += 1
                U_count += 1
            
            elif (u_choice == 'rock' and c_choice == 'sessior') or (u_choice == 'sessior' and c_choice == 'paper') or (u_choice == 'paper' and c_choice == 'rock'):
            
            print('Computer choice', c_choice)
            print('uchoice', u_choice)
            print('you win!')
            U_count += 1
            
            else:
                print('Computer choice', c_choice)
                print('uchoice', u_choice)
                print('Computer machine Win!')
                C_count += 1

        if C_count == U_count:
            print('Final Draw game!')
            print('Total:', C_count, U_count)
        elif C_count < U_count:
            print('User`s Final Result', U_count)
        else:
            print('Computer`s Final Result', C_count)
    else:
        break
