# dict = {
#     "name":"Banti Kumar",
#     "cgpa":9.8,
#     "marks":[98, 97, 96],
# }
# # print(dict)
# print(dict["name"])

# dict["name"] = "Sonu Singh"
# print(dict)

# nested dictionary:-
# Student = {
#     "name":"Banti kumar",
#     "roll no":495003,
#     "age":18,
#     "score":{
#         "math":95,
#          "sci":97,
#          "chem":96
#     }, 
#     "is_adult":True, 
#     12.32:45 

# }
# Student.update({"city":"dehli"})

# new_dict = {"name":"Sonu Singh", "city":"dehli", "age":19}
# Student.update(new_dict)
# print(Student)


# print("hi")
# print("hello")
# print("Welcome")
# print(Student.get("name2")) #no error -> return none
# print(Student["name2"]) #error
# print(Student["score"]["math"])
# print(len(list(Student.keys())))
# print(list(Student.values()))
# print(Student.items())
# print(Student.get("name"))

# null dictionary:=
# null_dict = {}
# null_dict["name"] = "College University"
# print(null_dict)

# set function:=
# collection = {1, 2, 3, 4, "hello", "world", "world", 5}
# print(collection)
# print(len(collection)
# collection = set() #empty set
# print(type(collection))
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(4)
# collection.add(5)
# collection.add("vishal")
# collection.add("Ruchi")
# collection.add("Sohan")
# collection.add("subham")
# collection.add("Rani")
# collection.add((7, 8, 9))

# # collection.clear()
# print(len(collection))
# # print(collection.remove(3))

# set = {"hello", "college", "codding", "world"}
# print(set.pop())
# print(set.pop())
# print(set.pop())


# set1 = {2, 3, 1, 7, 8}
# set2 = {1, 2, 3, 5, 4} 
# union = set1.union(set2)
# print("union == ", union)

# Intersection = set1.intersection(set2)
# print("Intersection ==", Intersection) 


# Practice;-
# 1.
# dict = {
#     "cat":"a small animal", 
#     "table":["a piece of furniture", "list of facts & figure"]
# }

# print(dict)

# # 2.
# classroom = {
#     "python", "java", "c++", "python", "javascript",
#       "java", "python", "java", "C++", "C"}

# print("Needed classroom == ", len(classroom))


# # 3.
# marks = {}
# x = int(input("ent4er phy : "))
# marks.update({"phy" : x})

# x = int(input("enter chem : "))
# marks.update({"chem" : x})

# x = int(input("enter math : "))
# marks.update({"math" : x})

# print(marks)

# 4.
value = {
    ("int", 9), 
    ("float", 9.0)
    }
print(value)