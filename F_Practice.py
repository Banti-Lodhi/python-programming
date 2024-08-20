# 1.
# def maximum(a, b, c):
#     if ((a >= b) and (a >= c)):
#         largest = a
#     elif ((b >= c) and (b >= a)):
#         largest = b
#     else:
#         largest = c

#     return largest
# a = 10
# b = 12
# c = 15
# print(maximum(a, b, c))

# 1.
# def maximum(a, b, c):
#     list = [a, b, c]
#     list.sort()
#     return list[-1]
# a=14
# b=148
# c=10
# print(maximum(a, b, c))

# # 2.
# list = (8, 2, 3, 0, 7)
# sum = 0
# for i in list:
#     print(i)
#     sum += i
# print(sum)    


# # 3.
# list = (8, 2, 3, -1, 7)
# mul = 1
# for i in list:
#     mul *= i
# print(mul)    

# 4.
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
# s = "Greekforgreeks"

# print('Original str:', s)
# print()
# print()
# print('revesred str:',reverse(s))     

# OR
# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]

# s = 'Geeksforgeeks'
# print('The original string is : ', end='')
# print(s)

# print('The reverse string is : ', end='')
# print(reverse(s))

# OR
# def createStack():
#     stack = []
#     return stack

# def size(stack):
#     return len(stack)

# def isEmpty(stack):
#     if size(stack) == 0:
#         return True

# def push(stack, item):
#     stack.append(item)

# def pop(stack):
#     if isEmpty(stack):
#         return
#     return stack.pop()

# def reverse(string):
#     n = len(string)

#     stack = createStack()
# # push all characters of  string to  stack
#     for i in range(0, n, 1):
#         push(stack, string[i])

#     string = ''

#     for i in range(0, n, 1):
#         string += pop(stack)
#     return string

# s = 'Geeksforgeeks'

# print('Original string is : ', end='')
# print(s)

# print('The reversed string(using stack) is : ', end=' ')
# print(reverse(s))

# OR
# def reverse(string):
#     string = ''.join(reversed(string))
#     return string
# string = 'Soniya gandhi'
# print('The original string is:', string)
# print('The reversed string is:',reverse(string))

# OR
# def reverse(string):
#     string = [string[i] for i in range(len(string)-1, -1, -1)]
#     return ''.join(string)
    
# string = 'Soniya gandhi'
# print('The original string is:', string)
# print('The reversed string is:',reverse(string))

# OR
# def reverse(string):
#     string = list(string)
#     print(string)
#     string.reverse()
#     print(string)
#     return "".join(string)
 
# s = "Geeksforgeeks"
 
# print("The original string  is : ", s)
 
# print("The reversed string(using reversed) is : ", reverse(s))

# 5.
# def factorial(n):
#     return 1 if (n==0 or n==1) else n * factorial(n-1)

# num = 0
# print('factorial of ',num, 'is', factorial(num))

# or

# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#        return 1
#     else:
#         fact = 1
#         while(n > 1):
#             fact *= n
#             n -= 1
#         return fact
# num = 5
# print('factorial of', num, 'is', factorial(num))            

# or
# def factorial(n):
    
#     res = 1

#     for i in range(2, n+1):
#         res *= i
#     return res 

# num = 4
# print('factorial of', num, 'is', factorial(num)) 

# or

# import math


# def factorial(n):
#     return (math.factorial(n))   

# num = 6
# print('factrial of', num, 'is', factorial(num))

# or
# import numpy

# n = 5 

# res = numpy.prod([i for i in range(1, n+1)])
# print('factrial of', n, 'is', res)


# or
# # Function t find prime factors of a number
# def primeFactorial(n):
#     factors = {}
#     i = 2
#     while i*i <= n:
#         while n % i == 0:
#             if i not in factors:
#                 factors[i] = 0
#             factors[i] += 1
#             n //= i
#         i += 1
#     if n > 1:
#         if n not in factors:
#             factors[n] = 0
#         factors[n] += 1
#     return factors   

# #Funtion to find factorial of a number
# def factorial(n):
#     result = 1
#     for i in range(2, n+1):
#         factors = primeFactorial(i)
#         for p in factors:
#             result *= p ** factors[p]
#     return result
# #Driver Code
# num = 5
# print('factrial of', num, 'is', factorial(num))

# 6.
# def count(list1, l, r):
#     c = 0
#     for i in list1:
#         if (i >= l and i <= r):
#             c += 1
#     return c    
# list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70] 
# l = 40
# r = 80
# print(count(list1, l, r))           

# # or

# def count(list1, l, r):
    
#     return len(list(x for x in list1 if x >= l and x <= r))
# list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70] 
# l = 20
# r = 80
# print(count(list1, l, r))

# or

# def count(list1, l, r):
    
#     return sum(x >= l and x <= r for x in list1) 

# list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70] 
# l = 30
# r = 80
# print(count(list1, l, r))

# or

# def count(list1, l, r):
    
#     return len(list(filter(lambda x: x>=l and x<=r, list1)))
# list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70] 
# l = 20
# r = 80
# print(count(list1, l, r))


# OR
# import bisect


# def count(list1, l, r):
#     list1.sort()
#     left_idx = bisect.bisect_left(list1, l)
#     right_idx = bisect.bisect_right(list1, r)
#     range_count = right_idx-left_idx
#     return range_count
# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# num_count_system = count(list1, 40, 90)
# print(num_count_system)

# 7.
# str = 'The quick Brow Fox'
# lower = 0
# upper = 0
# for i in str:
#     if (i.islower()):
#         lower += 1
#     elif (i.isupper()):
#         upper += 1
#     else:
#         exit
# print('Lower case count number are', lower)
# print('Upper case count number are', upper)

# or

# def lower_upper_case(str):
#     lower = 0
#     upper = 0
#     for i in range(len(str)):
#         if(ord(str[i])>=97 and ord(str[i])<=122):
#             lower += 1
#         elif(ord(str[i])>=65 and ord(str[i])<=90):
#             upper += 1
#         else:
#             exit
#     print('lower case letter in this str are = %s' %lower)            
#     print('upper case letter in this str are = %s' %upper)            
# str = 'The quick Brow Fox'
# lower_upper_case(str)

# OR
# str = 'The quick Brow Fox'
# l, h = 0, 0
# for i in str:
#     if (i>='a' and i<='z'):
#         l += 1

#     if (i<='A' and i<='Z'):
#         h += 1
# print('lower case ch are', l) 
# print('upper case ch are', h)               

# 8.
# def unique_list(l):
#     x = []
#     for i in l:
#         if i not in x:
#             x.append(i)
#     return x

# print(unique_list([1, 2, 2, 3, 4, 8, 5, 6, 4, 5, 7, 5, 5, 2, 2, 3, 2]))

# 10.
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l = []
# for i in list:
#     if i%2==0:
#         l.append(i)
#     else:
#         exit   

# print('even number : ', l)

# 9.
# def test_prime(n):
#     if(n==1):
#         return False
#     elif(n==2):
#         return True
#     else:
#         for x in range(2, n):
#             if (n%x==0):
#                 return False
#         return True
    
# print(test_prime(19))    

# or
# from math import sqrt

# n=7

# prime_flag = 0

# if(n > 1):
#     for i in range(2, int(sqrt(n)) + 1):
#         if (n % i == 0):
#             prime_flag = 1
#             break
#     if(prime_flag == 0):
#         print("True")
#     else:
#         print("False")
# else: 
#     print('False')  

# or
# def is_prime_trial_division(n):
#     if n<=1:
#         return False
    
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# print(is_prime_trial_division(11))

# or
# import math


# def is_prime(n):
#     if n < 2:
#         return False
#     i=2
#     while i*i <= n:
#         if n%i == 0:
#             return False
#         i += 1
#     return True
# print(is_prime(11))
# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(9))

# or
# import math


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
 
# n = 15
# print(is_prime(n))

# or
# Python program to check prime number
# using sympy.isprime() method
 
# # importing sympy module
# from sympy import *

# # calling isprime function on different numbers
# geek1 = isprime(30)
# geek2 = isprime(13)
# geek3 = isprime(2)
 
# print(geek1) # check for 30 is prime or not
# print(geek2) # check for 13 is prime or not
# print(geek3) # check for 2 is prime or not
 
# # This code is contributed by Susobhan Akhuli

# 11.
# def perfect_number(n):
#     sum = 0

#     for x in range(1, n):
#         if n%x == 0:
#             sum += x
#     return sum == n 
# print(perfect_number(5))      

# or
# def isPerfect(n):
#     sum = 1
#     i=2
#     while i*i<=n:
#         if n%i == 0:
#             sum = sum + i + n/i
#         i += 1
#     return (True if sum == n and n != 1 else False)

# print('Below are all perfect numbers till 10000')
# n = 2
# for n in range(10000):

#     if isPerfect(n):
#         print(n, 'is a perfect number')   

# 12.

# def isPalindrome(string):

#     left_pos = 0
#     right_pos = len(string) - 1

#     while right_pos >= left_pos:
#         if not string[left_pos] == string[right_pos]:
#             return False
#         left_pos += 1
#         right_pos -= 1

#     return True    
# print(isPalindrome('azoza'))
# print(isPalindrome('madam'))
# print(isPalindrome('nursesrun'))

# 12.
# from math import factorial

# #n input
# n = 5

# for i in range(n):
#     for j in range(n-i+1):

#         print(end=' ')

#     for j in range(i+1):

#         print(factorial(i) // (factorial(j) * factorial(i-j)), end=' ')
#     print()    

# or
# n = 5 
# for i in range(1, n+1):
#     for j in range(0, n-i+1):
#         print(' ', end='')

#     C = 1
#     for j in range(1, i+1):
      
#       print(' ', C, sep='', end='')

#       C = C*(i-j)//j
#     print()   

# or
# n=5
# for i in range(n):
#     print(' '*(n-i), end='')

#     print(' '.join(map(str, str(11**i))))     


# or
# # Define a function named 'pascal_triangle' that generates Pascal's Triangle up to row 'n'
# def pascal_triangle(n):
#     # Initialize the first row of Pascal's Triangle with value 1 as a starting point
#     trow = [1]
    
#     # Create a list 'y' filled with zeros to be used for calculations
#     y = [0]
    
#     # Iterate through a range starting from 0 up to the maximum of 'n' or 0 (taking the maximum to handle negative 'n')
#     for x in range(max(n, 0)):
#         # Print the current row of Pascal's Triangle
#         print(trow)
        
#         # Update the current row based on the previous row by calculating the next row using list comprehension
#         # The formula for generating the next row in Pascal's Triangle is based on addition of consecutive elements
#         trow = [l + r for l, r in zip(trow + y, y + trow)]
    
#     # Return True if 'n' is greater than or equal to 1, else return False
#     return n >= 1

# # Generate Pascal's Triangle up to row 6 by calling the 'pascal_triangle' function
# pascal_triangle(6) 

# 14.
# import string

# def ispangram(str):
#     alphabet = 'abcdefghijklmnopqrtuvwxyz'
#     for char in alphabet:
#         if char not in str.lower():
#             return False
#     return True

# # driver code
# string = 'The quick brown fox jumps over the lazy dogister'    

# if(ispangram(string)==True):
#     print('Yes')
# else:
#     print('No')

# or

# alphabet = set(string.ascii_lowercase)
# def ispangram(string):
#     return set(string.lower()) >= alphabet
# # Driver code
# string = 'The quick brown fox jumps over the lazy dog' 
# if(ispangram(string) == True):
#     print('yes')
# else:
#     print('No')

# alphabet = set(string.ascii_lowercase)
# def ispangram(string):
#     return not set(alphabet) - set(string)
# # Driver code
# string = 'The quick brown fox jumps over lazy dog' 
# if(ispangram(string) == True):
#     print('yes')
# else:
#     print('No')

# 15.

# items = [n for n in input().split('-')]
# items.sort()
# print('-'.join(items))

# 16.
# def printValue():
    
#     l = list()
    
#     for i in range(1, 31):
#         l.append(i**2)

#     print('Square list ==', l)
# printValue()   

# # 17.
# def make_bold(fn):
#     def wrapped():
#         return '<b>' + fn() + '</b>'
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return '<i>' + fn() + '</i>'
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return '<u>' + fn() + '</u>'
#     return wrapped

# @make_bold
# @make_italic
# @make_underline

# def hello():
#     return 'hello banti kumar singh'
# print(hello())

#or
# # Define a decorator 'make_bold' that adds bold HTML tags to the wrapped function's return value
# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# # Define a decorator 'make_italic' that adds italic HTML tags to the wrapped function's return value
# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# # Define a decorator 'make_underline' that adds underline HTML tags to the wrapped function's return value
# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped

# # Apply multiple decorators (@make_bold, @make_italic, @make_underline) to the 'hello' function
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello world"

# # Print the result of the decorated 'hello' function, which adds HTML tags for bold, italic, and underline

# print(hello()) ## returns "<b><i><u>hello world</u></i></b>"


# or
# mycode = 'print("hello_India")'
# code = '''
# def function(x, y):
#     return x * y
# print(function(4, 7))
# '''

# exec(mycode)
# exec(code)

# 19.
# def test(a):

#     def add(b):
#         nonlocal a
        
#         a+=1

#         return a + b
#     return add
# func = test(4)
# print(func(4))

# 20.
# def abc():

#     a = 1
#     b = 2
#     str = 'w3resource'
#     print('Hello India')

# print(abc.__code__.co_nlocals)    

# 21.
# r = lambda s:s+15
# print(r(10))

# t = lambda a, f:a*f
# print(t(21, 12))

# # 22.
# def func_compute(n):
#     return lambda x:x*n

# result = func_compute(15)
# print('print the double number of 15 is', result(2))

# result = func_compute(15)
# print('print the triple number of 15 is', result(3))

# result = func_compute(15)
# print('print the quadine number of 15 is', result(4))

# result = func_compute(15)
# print('print the quindian number of 15 is', result(5))

# result = func_compute(15)
# print('print the quintin number of 15 is', result(6))

# result = func_compute(15)
# print('print the septian number of 15 is', result(7))

# 23.
# subject_marks = [('math', 97), ('science', 90), ('social science', 80), ('chemistry', 98)]

# print('Original the list of tuples : ', subject_marks)

# subject_marks.sort(key = lambda x:x[1])
# print('sorting the list of tuples:', subject_marks)

# 24.

# models = [
#     {'make' : 'Nokia', 'models' : 217, 'color' : 'Silver'},
#     {'make' : 'Samsung', 'models' : 27, 'color' : 'Magenta'},
#     {'make' : 'MI max', 'models' : 2, 'color' : 'Gold'},
#     {'make' : 'Apple 4G', 'models' : 15, 'color' : 'Yellow'}
# ]

# print('Originaly dictioanry', models)
# print('\n\n')

# sorted_dictonary = sorted(models, key = lambda x : x['color'])

# print('sorted models to dictioanry: ',  sorted_dictonary)

# # 25.
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print('Originally numbers:\n', nums)

# even_num = list(filter(lambda x : x % 2 == 0, nums))
# print('\neven numbers:\n', even_num)

# Odd_num = list(filter(lambda x : x % 2 != 0, nums))
# print('\nOdd numbers:\n', Odd_num)

# 26.
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print('Originally numbers:\n', nums)

# Square_num = list(map(lambda x : x ** 2, nums))
# print('\nSquare every number of the said list:\n', Square_num)

# Cube_num = list(map(lambda x : x ** 3, nums))
# print('\nCube every number of the said list:\n', Cube_num)

# # 27.
# starts_with = lambda x: True if+(x.startswith('p') or x.startswith('P')) else False

# print(starts_with('python'))
# print(starts_with('Python'))
# print(starts_with('java'))
# print(starts_with('C++'))

# 28.
# import datetime

# now = datetime.datetime.now()

# print('Current time table process:', now)

# year = lambda x: x.year

# month = lambda x: x.month

# day = lambda x: x.day

# time = lambda x: x.time()

# minute = lambda x: x.minute


# print('year :', year(now))

# print('month :', month(now))

# print('day :', day(now))

# print('time :', time(now))

# print('minute :', minute(now))


# 29.
# is_num = lambda q: q.replace('.', '', 1).isdigit()

# print(is_num('124.65'))
# print(is_num('-124.65'))
# print(is_num('12.65'))
# print(is_num('A065'))
# print(is_num('0.09'))
# print(is_num('12465'))

# is_num1 = lambda r: is_num(r[1:])  if r[0] == '-' else is_num(r)
# print(is_num1('123-123'))
# print(is_num1('-12.3'))
# print(is_num1('-89.0'))

#30. from functools import reduce

# Fib_series = lambda n: reduce(lambda x, _: x+[x[-2] + x[-1]], range(n-2), [0, 1])

# print('\nFibonacci series upto 2\n', Fib_series(2))
# print('\nFibonacci series upto 3\n', Fib_series(3))
# print('\nFibonacci series upto 4\n', Fib_series(4))
# print('\nFibonacci series upto 5\n', Fib_series(5))
# print('\nFibonacci series upto 6\n', Fib_series(6))


# arr1_num = [1, 2, 3, 5, 7, 8, 9]
# arr2_num = [3, 4, 5, 6, 8, 1]

# print('\nOriginal string:\n', arr1_num, arr2_num)

# intersection = list(filter(lambda x: x in arr1_num, arr2_num ))

# print('Intersection of both strings are', intersection)


# 32.

# str = [4, 1, 2 ,5, 3, 7, -5, 9, -10, -20]

# print('Original String \n: ', str)

# sorted_str = sorted(str, key = lambda i: 0 if i == 0 else -1/i)

# print('sorted string: ', sorted_str)

# 33.
# num_str = [0, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 19, -78]

# print('Original string:\n\n ', num_str)

# odd_num = len(list(filter(lambda x: (x % 2 != 0), num_str)))
# even_num = len(list(filter(lambda x: (x % 2 == 0), num_str)))

# print('odd numbers:\n',odd_num)
# print('even_number:\n', even_num)

# # 34.
# weeksdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday' 'Friday', 'Saturday']

# return_filter = filter(lambda day: day if len(day) == 6 else '', weeksdays)

# for i in return_filter:
#     print(i)

# 35.
# num1 = [1, 2, 3]
# num2 = [4, 5, 6]

# print('Original list: \n\n',num1, num2)
# result = map(lambda x, y: x+y, num1, num2)

# print('print list after both string add:\n\n ',list(result))

# 37.

# def list_benefits(str):


# 40.
# def outerFunction(text):
#     text = text

#     def innerFunction():
#         print(text)

#     innerFunction()

# if __name__ == '__main__':
#     outerFunction('Hey!')

# 41.
# def map_func(n):
#     return n+n
# numbers = [1, 2, 3, 4]
# result = map(map_func, numbers)
# print(list(result))

# 42.
# def func(d):

#     for key in d:
#         print("key:", key, "value:", d[key])

# D = {'a':1, 'b':2, 'c':3}
# func(D)  

# 43.
# def f():
#     global s
#     print(s)
#     s='Asian publishers'
#     print(s)
# s = 'Hello World'
# f()
# print(s) 
# 
# 45.
# (i).
import logging

# logging.basicConfig(filename='example.log', level = logging.INFO)

# def logger(func):
#     def log_func(*args):
#         logging.info(
#             'Running "{}" with arguments {}'.format(func.__name__, args)
#         )
#         print(func(*args))
#     return log_func
# def add(x, y):
#     return x+y
# def sub(x, y):
#     return x-y

# add_logger = logger(add)    
# sub_logger = logger(sub)

# add_logger(3, 4)
# add_logger(5, 3)

# sub_logger(9, 5)
# sub_logger(67, 25)

# # ii.
# def func1():
#     print('i`m learning python course')
#     print('still in func1')

# def square(x):
#     return x*x
# print(square(4))

# def multiply(x, y=0):
#     print('print value of x is', x)
#     print('print value of y is', y)
#     return x*y

# print(multiply(12, 45))
    
# # iii.
# def simple_interset(p, r, t):
#     return (p*r*t)/100
# p = float(input('Enter principle amount:\n'))
# r = float(input('Enter rate of interset:\n'))
# n = float(input('Enter time in years:\n'))

# print('Simple Amount', simple_interset(p, r, n))

# # iv.
# def printme(*names):
#     print('type of passed argument is', type(names))
#     print('printing the passed arguments...')
#     for name in names:
#         print(name)
# printme('Swati','kavita', 'Jully', 'Sony', 'Mohany')

# v.
# def Calculate(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     print('The sum is: ', sum)
# sum = 0
# Calculate(10, 20, 30, 40, 50, 60)
# print("Value of sum outside the function: ", sum)

# vii.
# List = {1, 2, 24, 1, 5, 24, 4, 7}

# new_list = list(map(lambda x: x**4, List))

# print(new_list)

# viii
# def add_all_arguments(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(add_all_arguments(2, 3, 4, 5, 7, 8, 9, 5, 12, 45))    
# print(add_all_arguments(45, 45, 12, 48, 45, 15, 23, 12))    
# print(add_all_arguments(45, 45, 55, 45, 12, 23, 4, 5, 5))    
# print(add_all_arguments(45, 12, 14, 25, 35, 21, 47, 15, 23))    
# print(add_all_arguments(2, 3, 4, 5, 7, 12, 45))    
# print(add_all_arguments(2, 8, 9, 5, 12, 45))    
# print(add_all_arguments(8, 9, 5, 12, 45))    
# print(add_all_arguments())   
# 
# ix.
# text = "global text"

# def outer_func():
#     text = 'enclosing text'
# def inner_func():
#     text = 'inner text'
# print('inner func', text)
# print('outer func', text)

# inner_func()
# print('outer func', text)
# print('global:', text)
# outer_func()
# print('global:', text)

# # ix.
# def capitalize(func):
#     def uppercase():
#         result = func()
#         return result.upper()
#     return uppercase
# def say_hello():
#     return 'hello'
# print(say_hello())

# xii.
def print_arguments(**kwargs):
    print(kwargs)
print(print_arguments(name='Moyosore'))
print(print_arguments(name = 'Moyosore', country= 'Nigeria'))
print(print_arguments())

def print_arguments_values(**kwargs):
    for key, value in kwargs.items():
        print('{0}: {1}'.format(key, value))
print_arguments_values(name = 'Moyosore', country = 'Nigeria')        