# Functions in Python:
# Block of statements that perform a specific task:=

# def calc_sum(a, b):
#     return a+b
# print(calc_sum(4, 6))
# print(calc_sum(5, 7))
# print(calc_sum(9, 3))

# def hello_func():
#     print("hello")
# hello_func()    
# hello_func()    
# hello_func()    
# hello_func()    

# def calc_avg(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg
# calc_avg(9, 4, 5)    
# calc_avg(4, 1, 5)    
# calc_avg(9, 0, 5)    
# calc_avg(7, 4, 5)


# practice set:-

# cities = ["dehli", "gurgaon", "noida", "pune", "mumbai", "chennai"] 
# heroes = ["thor", "ironman", "csptain america", "shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# def print_len(list):
#     for item in list:
#         print(item, end=", ")

# print_len(cities)
# print_len(heroes)

# 3.
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)

# 4.
# def converter(usd_val):
#     inr_val = 83*usd_val
#     print(usd_val, "usd == ", inr_val, "INR")        
# converter(1)
# converter(3)
# converter(4)
# converter(6)

# Recursion function:-
#1.
#  def show(n): 
#     if(n == 0):
#         return   
#     print(n)
#     show(n-1)
#     print("END")

# show(4)    

# 2.
# def fact(n):
#     if(n==0 or n==1):
#       return 1
#     else:
#       return n*fact(n-1)
    
# print(fact(6))    

# practice set:-
# 1.
# def calc_sum(n):
#     if(n == 0):
#         return 0 
#     return calc_sum(n-1)+n
# sum = calc_sum(5)
# print(sum)

# 2.
def print_list(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "Litchi", "orange", "banana", "patoto", "pineaple"] 
print_list(fruits)