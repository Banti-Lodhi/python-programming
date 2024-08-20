# Student_info = ["Vishal", 17, 84.56, "math"]
# print(Student_info)

# # String Immutable
# str = "hello"
# print(str[0])

# str[0] = "Python" #String can be immutable and its string given a error
# print(str[0])

# List is mutable and any change in list string
# Student_info = ["Vishal", 17, 84.56, "math"]
# # print(Student_info[5]) #list index out of range
# print(Student_info)
# Student_info[0] = "Arjun"
# print(Student_info)


# Slicing Lists:=
# marks = [12, 13, 14, 15, 16]
# print(marks[1:4])
# print(marks[1:])
# print(marks[-4:-1])
# print(marks[:-1])
# print(marks[-1::-1]) #reverse string

# List Methods:=
# list = [12, 6, 5, 1, 8, 3]
# print(list.append(7))
# print(list.sort())

# print(list)
# print(list.sort(reverse=True))

# str = ["aim", "apple", "ant", "account", "art", "amazon"]
# print(str.sort())
# print(str)
# print(str.sort(reverse=True))
# print(str)

# print(str.reverse()) #complete string can be reverse
# str.insert(3, "Pineapple")
# print(str)

# str.remove("apple")#str.remove(string)
# print(str)

# print(str)
# str.pop(3) #str.pop(index)
# print(str)


# Tuple String:=
# tup1 = (3) #it is not tuple
# tup = (3,) #it is tuple

# print(type(tup1))
# print(type(tup))

# tup = (4, 5, 6, 8, 4, 4, 4)
# print(tup.index(6))
# print(tup.count(4))

# Practice:-
# 1.
# movies = []
# mov1 = input("Enter 1st movie ")
# mov2 = input("Enter 2st movie ")
# mov3 = input("Enter 3st movie ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# 2.
# list = [1, 2, 3, 2, 1]

# list_copy = list.copy()

# if(list == list_copy):
#     print("plindrome")
# else:
#     print("Not plindrome")

# 3.
# print(grade.count("A"))
# grade.sort()
# print(grade)
# grade = ["C", "D", "A", "A", "B", "B", "A"]
# try:
#    ets = grade.remove(10)
#    print(ets)
# except Exception:
#   print("value Error")

# try:
#   list = grade.pop(-10)
#   print(list)
# except Exception:
#   print("Error Handling")

tup1 = (1, 2, 7, 3)
tup2 = (5, 4, 3, 7)

res = sum((tup1, tup2), ())
print(res)

str = (1, 2, 7, 3, 5, 4, 3, 7)
print(str)