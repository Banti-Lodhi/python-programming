# 1.
# try:
#   a = 3
#   if a < 4:
#     b = a/(a-3) # throws ZeroDivisionError for a = 3
#     # throws NameError if a >= 4
#     print("value of b:", b)
#     # note that braces are necessary for multiple exceptions
# except(ZeroDivisionError, NameError):
#   print("\nError Occurred and Handled")
  
# 2.
# try:
#     a = int(input("Enter a:\n"))
#     b = int(input("Enter b:\n"))
#     c = a/b
#     print("a/b = %d" %c)
# except Exception:
#     print("Can't divide by Zero")
# else:
#     print("Hi i am else block")    

#Handled multiple Exceptions
# code1
# try:
#   client_obj.get_url(url)    
# except (URLError, ValueError, SocketTimeout):
#   client_obj.remove_url(url)   
# try:
#     f = open(filename)

# except OSError as e:
#     if e.errno == errno.ENOENT:
#         logger.error('File not found')
#     elif e.errno == errno.EACCES:
#          logger.error('Permission denied')
#     else:
#         logger.error('Unexpected error: %d', e.errno)


# raise:->
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# assert:->
# x = 'Hello'
# assert x == "goodbye", "x should be 'hello'"

# Excersize
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

# 11.
# x = 10
# y = 8
# assert x > y, 'X too small'

# 12.
# def f(x):
#     yield x+1
#     print("test")
#     yield x+2
# g = f(10)
# print(next(g))
# print(next(g))

# 13.
# import itertools

# l1 = (1, 2, 3)
# l2 = [4, 5, 6]
# l = itertools.chain(l1, l2)
# print(next(l1))

# 15.
# a = False
# while not a:
#     try:
#         f_n = input("Enter the name")
#         i_f = open(f_n, 'r')
#     except:
#         print("Input file not found")

# 16.
# lst = [1, 2, 3]
# lst[3]

# 17.
# t[5]

# 18.
# 4+'3'

# 19.
# code1:-
# import math

# num = int(input("Enter a number of whose factorial you want to find"))
# print(math.factorial(num))

# code2:-
# num = int(input("Enter a number of whose factorial you want to find"))
# print(math.factorial(num))

# 20.
# valid = False
# while not valid:
#     try:
#         n=int(input("Enter a number"))
#         while n%2==0:
#             print("Bye")
#         valid = True
#     except ValueError:
#         print("Invalid")  

# 21.
# Print("Good Morning")      
# print("Good night)


# try:
#     a = 3
#     if a < 4:
#         b = a/(a-3)

#         print("Value of b =", b)
# except(ZeroDivisionError, NameError):
#     print("\n Error Occured and Handled")


# tryexcept
# try:
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     c=a/b
#     print("a/b = %d"%c)
# except Exception:
#     print("cam't divide by zero")
# else:
#     print("Hi i am else block")


# # code5.
# try:
#     file=open("class9.py")

# except OSError as e:
#     if e.errno == e.errno.ENOENT:
#         e.logger.error('File not found')
#     elif e.errno == e.errno.EACCES:
#         e.logger.error('Permission denied')
#     else:
        # e.logger.error('Unexpected error: %d', e.errno)

# Raise:-
# x=10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was:{}'.format(x))

# # Assert :-
# x="hello"
# assert x == "goodbye", "x should be 'hello'"


import re

emailaddress = input()
part2 = "(\w+)@(w+)\.(com)"
r2 = re.match(part2, emailaddress)
print(r2.group(2))