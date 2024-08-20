# 1.The import statement
# from numpy import add

# print(add(8, 9))


#2.The from Import Statement 
# from module_name import name1, name2,.......name2
# importing sqrt() and factorial from the 
# module math


# from math import factorial, sqrt

# print(sqrt(16))
# print(factorial(4))



# import math
# import random
# # 3.Standard Modulus -SYS
# import sys

# loaded_modules = sys.modules

# print("Loaded modules:")

# for module_name in list(loaded_modules.keys())[:5]:
#     print(module_name)

# #Access the  names of the first few loaded modules
# math_module = loaded_modules.get('math')

# print("\n'{}' module:".format('math'))
# print(math_module)


# import sys

# # print(sys.version)
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input : {line}')
# print('Exit')   


# import sys


# def print_to_stderr(*a):
#     print(*a, file = sys.stderr)
# print_to_stderr('preetam singh rajput')    

# import sys

# sys.stdout.write('banti')

# import sys

# n = len(sys.argv)
# print('total arguments passed:', n)
# print('\n Name of python script:', sys.argv[0])
# # print('\n Arguments passed:', end=" ")

# for i in range(1, n):
#     print(sys.argv[i], end=" ")

# Sum = 0

# for i in range(1, n):
#     Sum += int(sys.argv[i])
# print('\n\nresult:', Sum)    


# age = 17

# if age < 18:
#     sys.exit('Age is less than 18')
# else:
#     print('age greater than 18')


# print(sys.path)

# import sys

# sys.path = []
# import pandas

# print(sys.modules)

# print(sys.maxsize)

# max_size = sys.maxsize

# list = range(max_size)
# print(len(list))

# print('List Successfully created.')

# print(sys.base_exec_prefix)

# print(sys.base_prefix)

# print(sys.byteorder)

# print(sys.stdin.readline())

# print(sys.getrefcount())


# import sys

# def main():
#     print("Enter something:")
#     user_input = sys.stdin.readline().strip()

#     print("You enetered:", user_input)

# if __name__ == "__main__":
#     main()    



# sample_obj = [1, 2, 3]

# intial_ref_count = sys.getrefcount(sample_obj)

# new_reference = sample_obj

# updated_ref_count = sys.getrefcount(sample_obj)

# # print the results
# print("Intial Reference Count:", intial_ref_count)
# print("Updated Reference Count:", updated_ref_count)

# # print(sample_obj)

# python_executable = sys.executable

# print("Python Executable Path:", python_executable)

# platform_info = sys.platform

# print("Platform:", platform_info)


# Standard Module - Math
# import matplotlib.pyplot as plt

# labels = ['Category A', 'Category B', 'Category C']

# sizes = [30, 45, 25]

# plt.pie(sizes, labels = labels, autopct='%1.1%%', startangle=90)

# plt.axis('equal')
# plt.show()

# import math

# number = 2e-7 #small value of of x

# print('log(fabs(x), base) is:', math.log(math.fabs(number), 10))

# # math log10()
# x = 13
# print('log10(x) is :', math.log10(x))

# number = 5e-2
# print('The given number(x) is :', number)
# print('e^x (using exp() function) is :', math.exp(number)-1)



# this function returns the square root of any given number.
# math.sqrt()

# import math

# x = 20
# y = 14
# z = 17.8995
# print(math.sqrt(x))
# print(math.sqrt(y))
# print(math.sqrt(z))

# number = 2e-1
# print(number)
# print(math.expm1(number))

# math.cos()
# angleDegree = 60
# angleRedian = math.radians(angleDegree)
# print(angleRedian)
# print('cos:-',math.cos(angleRedian))

# print('sin:-',math.sin(angleRedian))

# print('tan:-',math.tan(angleRedian))

import random
import time

# seconds = time.time()
# # print(seconds)
# result=time.gmtime(1545925769)

# print(result)

# print(result.tm_year)
# print(result.tm_hour)

# t = (2019, 12, 28, 8, 44, 6, 5, 362, 3)
# result = time.asctime(t)

# print('result:', result)

# secomd passed since epoch
# seconds = 1545925769.9618232
# local_time = time.ctime(seconds)
# print('Local time:', local_time)

# print('This is printed immediately.')
# time.sleep(400)
# print("This isprinted after 2.4 seconds.")

# local time:-
# result = time.localtime(1545925769)

# print("result:", result)
# print('\nyear',result.tm_year)
# print('tm_hour:', result.tm_hour)

# t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

# local_time = time.mktime(t)
# print("Local time:", local_time)

# named_tuple = time.localtime() #get struct time
# time_str = time.strftime("%m%d%Y, %H:%M:%S", named_tuple)
# print(time_str)

# time_string = "21 june, 2018"
# result = time.strptime(time_string, "%d %B, %Y")
# print(result)

# dir function 
# print(dir())
# import math
# import random

# print(dir())


print("The contents of random libray are::")
print(dir(random))