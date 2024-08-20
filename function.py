# def function(num1, num2):
#     return num1+num2

# print(function(45, 45))
# print(function(452, 452))
# print(function(453, 445))
# print(function(465, 475))
# print(function(485, 415))

# recusion function:-
# n=10
# product = 1
# for i in range(n):
#     product = product*(i+1)

# print(product)    
# print(10*9*8*7*6*5*4*3*2*1)    

# or
# def recursive_recursion(n):
#     if n==0 or n==1:
#         return 1
#     return n * recursive_recursion(n-1)
    
# print(recursive_recursion(7))        

# # Greater number concept
# def greater_number(n1, n2, n3):
#     if(n1>n3):
#         if(n1>n2):
#             return n1
#         else:
#             return n2
#     else:
#         return n3   

# print(greater_number(9, 5,7))     

# pattern print
# n = 5
# for i in range(n):
#     print('*' * (n-i))


# def remove_function_split(str, word):
#     newStr = str.replace(word, 'Banti kumar lodhi')
#     return newStr.strip()
# this = 'Harry is a Strong  boy'
# n = remove_function_split(this, 'Harry')
# print('remove the string from ',this,'and new string is', n)


# str = '        Harry is a boy strong.         '
# print(str)
# print(str.strip())

# file function

f = open('sample.txt')
data = f.read()
print(data)
f.close()