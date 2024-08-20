# 30.
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
#             print("*", end = "")
#         else:
#             print(end=" ")
#     print()            

# 31.
# for row in range(7):
#     for col in range(5):
#         if (col == 0) or (col == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()        

# 32.a
# n=5
# for row in range(n):
#     for col in range(row):
#       print("*", end="  ")
#     print()   
# for row in range(n, 0, -1):
#     for col in range(row):
#         print("*", end="  ")   
#     print() 

# 32b.
# n=10
# for row in range(10):
#     for col in range(row):
#         print(row, end=" ")
#     print()  

# 32c.

# for row in range(8):
#     for col in range(8):
#         if ((row+col == 7) and (row != 0 or row != 7)) or ((row==0 and col!=0) or (row==7 and col!=7)):
#             print("*", end="  ")
#         else:
#             print(end="   ")
#     print()        

# 32d.
# for row in range(7):
#     for col in range(3):
#         if ((col == 0 or col == 2) and (row != 3)) or ((row == 3) and (col>0 and col<2)):
#             print("*", end="  ")
#         else:
#             print(end="   ")
#     print() 

# 32.e
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (row != 6)) or ((row==6) and (col>0 and col<4)) :
#             print("*",end="  ")
#         else:
#             print(end="   ")
#     print()        

# 32(f):-
# for row in range(8):
#     for col in range(5):
#         if ((col == 0 or row == 0) and (row != 3)) or ((row == 3) and (col<4)):
#             print("*", end="  ")
#         else:
#             print(end="   ")
#     print()

# 32(g):
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0) and (col > 0 and col < 4)) or ((row == 6) and (col > 0 and col < 4)):
#             print("*", end="  ")
#         else:
#             print(end="   ")
#     print() 

# *
# *****
# *
# *
# ****
#     *
#     *
# *****

