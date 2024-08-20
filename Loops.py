#2. practice set
# i = 100
# while i >= 1:
#     print(i,". hello")
#     i -= 1

# 3.
# n = int(input("Enter the n number from the user: "))

# i = 1
# while i <= 10:
#     print(n, "*", i, "==", n*i)
#     i += 1

# 4.
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(nums):
#     print(i,'==', nums[i])
#     i+=1

# 5.
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# search_idx = int(input("Enter number for searching index: "))

# i = 0
# while i < len(nums):    
#     if(nums[i] == search_idx): 
#        print("Found at idx", i, "and find number is", nums[i])            
#        break
#     else:
#         print("finding...")
#     i+=1
# print("end of loop")

# Continue statement
# i = 0
# while i < 10:
#     if(i%2 == 0):
#        i+=1  
#        continue #Skip     
#     print(i)
#     i+=1

# for Loop
# 1.
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# for el in nums:
#     print(el)
#  2.
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25)
# x = 25
# idx = 0
# for el in nums:
#     if(el == x):
#         print("Number Found at idx", idx)
#         break
#     idx+=1    

# range(start?, stop, step?): method:
# 1.
# for i in range(1, 101):
#     print(i, end=", ")

#2.
# for i in range(100, 0, -1):
#     print([i], end=", ")
# 3.
# n = int(input("Enter number: "))
# for i in range(1, 11, 1):
#     print(n*i)


# pass statement:-
# pass is a null statement that does nothing. It is used as a placeholder for future code
# for i in range(10):
#     # empty
#     pass

# print("End the loop")

# practice set:= 
# 1.
# n = 5
# sum = 0
# i = 1
# while i <= 5:
#     sum += i 
#     i+=1
# print("Total sum == ", sum)    

# 2.
n = 3 
fact = 1
for i in range(n, 0, -1):
    fact *= i
print("fact of 5 is", fact)    