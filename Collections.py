# list1 = ['Physics', 'chemistry', 'Maths']
# list2 = [1, 2, 3, 4, 5, 6, 7, 9]
# list3 = ['a', 'b', 'c', 'd', 'e']

# list1.append('Hindi')
# list1.append('English')
# list1.append('History')
# list1.append('Biology')

# list1.insert(0, 'Excel book')
# print(list1)
# print(sorted(list1))
# list3.extend(['f', 'g', 'n', 'o', 'p', 'q', 'h', 'i', 'j', 'k', 'l', 'm'])
# print(list3)
# print(sorted(list3))
# list3.remove('m')
# print(list3)
# list2.pop(-4)
# print(list2)


# methods1:Using + operator:
# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = "a", "b", "c", "d"
# res=tup1+tup2
# print(res)

# Using sum() function :-
# assian_tup1 = (1, 2, 5)
# assian_tup2 = (4, 6)
# res = sum((assian_tup1, assian_tup2), ())
# print(res)

# Using zip() + nested generation expression:-
# test_tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
# test_tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))
# print(str(test_tup1))
# print(str(test_tup2))
# res = tuple(tuple(a+b for a,b in zip(tup1, tup2))
#             for tup1, tup2 in zip(test_tup1, test_tup2))
# print("the resultant tuple afetr summation: ", str(res))  

# tuple = (0, 1)
# print(len(tuple)) 
# del tuple
# print(tuple)

# Converting list  into tuple:-
# list = [0, 1, 2, 3]
# print(tuple(list))
# print(tuple('python'))

# Dictionary
# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)
# Dict[1] = "Asian"
# {Dict[2] = "Publishers"
# Dict[3] = "1"
# print("\nDictionary after adding 3 elemnts: ")
# print(Dict)
# Dict['Value_set'] = 2, 3, 4
# print("\nDictionary after adding 3 elemnts: ")
# print(Dict)
# Dict[2] = "Welcome"
# print("\nUpdated key value: ")
# print(Dict)
# Dict[5] = {'Nested':{'1':'Life', '2':'Asian'}}
# print("\nAdding a Nested key: ")
# print(Dict)

# Removing element from the string:
# Dict = {5:'Welcome', 6:'To', 7:'Asian publishers',
#         'A':{1:'Asian', 2:'publishers', 3:'Mujapharnagar'},
#         'B':{1:'Asian', 2:'publishers'}
#         }
# print("Intial dictionary")
# print(Dict)

# del Dict[6]
# print('\n deleting a specific key:')
# print(Dict)

# del Dict['A'][2]
# print("deleting a key from the nested dict")
# print(Dict)
     
# Using pop method
# Dict = {1:'ram', 'Name':'For', 2:'ram'}
# pop_ele = Dict.pop(1)
# print('\n print after deletion '+str(Dict))
# print("\n popped key is:"+str(pop_ele))


#Using popitem() method:- 
# Dict = {1:'ram', 'Name':'For', 3:'ram'}
# pop_ele = Dict.popitem()
# print('\nDictionary after deletion '+str(Dict))
# print("\n The Arbitrary pair returned is:"+str(pop_ele))

# Sorting Dictinary:-
# dict = {1:2, 3:2, 2:1, 5:4, 7:6}
# print(sorted(dict.keys()))
# print(sorted(dict.values()))
# print(sorted(dict.items()))

# dict = {1:2, 2:3, 3:4, 4:5, 6:7}
# print(sorted(dict.values(), reverse=True))
       
#copying collections
import copy

# li1 = [1, 2, [3, 4], 5, 6]
# li2 = copy.copy(li1)
# li3 =  copy.deepcopy(li1)
# print(li1)
# print(li2)
# print(li3)

# deep copy:-
# li1 = [1, 2, [3, 4], 5, 6]
# li2 = copy.deepcopy(li1)
# print("the elements before deepcopy")
# for a in range(0, len(li1)):
#     print(li1[a], end=' ')
# print('\r')
# li2[2][0] = 7
# print('The new list after deepcoping')
# for a1 in range(0, len(li1)):
#     print(li2[a1], end=' ')
# print('\r')
# print("the elements after deepcopy")
# for a in range(0, len(li1)):
#     print(li1[a], end=' ')    
    


# shawlow copy:-
li1 = [1, 2, [3, 4], 5, 6]
li2 = copy.copy(li1)
print("the elements before shallow copying")
for a in range(0, len(li1)):
    print(li1[a], end=' ')
print('\r')
li2[2][0] = 7
print('The new list after shallow copying')
for a1 in range(0, len(li1)):
    print(li1[a1], end=' ')
   
    


