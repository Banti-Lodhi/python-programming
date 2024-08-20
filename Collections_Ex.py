# 1.
# from collections import Counter

# c = Counter(a=2, s=3, g=5, f=-2, d=0)
# print(list(c.elements()))

# 2.
# from collections import Counter

# s = 'lkseropewdssafsdfafkpwe'

# print("Original string :"+s)
# print("three most common characters of the said string!")
# print(Counter(s).most_common(5))

# 3.
# from collections import deque

# dq = deque('preetam singh')

# for element in dq:
#     print(element)


# import re
# # 4.
# from collections import Counter

# text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit
# corporation that holds the intellectual property rights behind
# the Python programming language. We manage the open source licensing
# for Python version 2.1 and later and own and protect the trademarks
# associated with Python. We also run the North American PyCon conference
# annually, support other Python conferences around the world, and
# fund Python related development with our grants program and by funding
# special projects."""

# words = re.findall('\w+', text)
# print(Counter(words).most_common(10))


# 5.
# from collections import Counter, OrderedDict


# class OrderedCounter(Counter, OrderedDict):
#     pass

# word_array = []

# n = int(input("Input number of words: "))

# print("Input the words: ")
# for i in range(n):
#     word_array.append(input().strip())

# word_ctr = OrderedCounter(word_array)

# print(len(word_ctr))

# for word in word_ctr:
#     print(word_ctr[word], end=' ')

# 6.
# import collections
# import re

# n = int(input('Number of subjects: '))

# item_order = collections.OrderedDict()

# for i in range(n):
#     sub_marks_list = re.split(r'(\d+)$', input("Input Subjects name and marks: ").strip())
#     subject_name = sub_marks_list[0]
#     item_price = int(sub_marks_list[1])

#     if subject_name not in item_order:
#        item_order[subject_name] = item_price
#     else:
#        item_order[subject_name] = item_order[subject_name] + item_price
# for i in item_order:
#     print(i + str(item_order[i]))
#
# 7.
# import collections

# color_deques = collections.deque(['red', 'blue', 'green', 'yellow'])
# print('append color  in right side= \n')
# color_deques.append('black')
# print(color_deques)

# print('append color  in left side= \n')
# color_deques.appendleft('white')
# print(color_deques)


# print('pop color  in right side= \n')
# color_pop = color_deques.pop()
# print(color_pop)

# print('pop color  in right side= \n')
# color_pop = color_deques.popleft()
# print(color_pop)

# reverse_deque = color_deques.reverse()
# print('reverse deques is =', reverse_deque)

# 8.
# import collections

# even_num = (2, 4, 6)

# print("Print original number:", even_num)
# print(type(even_num))

# # insert the string into left side
# even_num_deque = collections.deque(even_num)

# print('\n print orginal deque', even_num_deque)

# # Append the numbers 8, 10, 12 to the right of the deque
# even_num_deque.append(8)
# even_num_deque.append(10)
# even_num_deque.append(12)
# print("the origina; deque is, ")
# # Append the numbers 0 to the left of the deque
# even_num_deque.appendleft(0)

# # print the update deque
# print(even_num_deque)
# print(type(even_num_deque))

# 9.
# inserting a tuple


# even_num = (2, 4, 6)
# print("the original tuple",even_num)
# even_deque = collections.deque(even_num)
# more_even_num = (8, 10, 12, 14, 16)

# even_deque.extend(more_even_num)
# print("print original deque", even_deque)

# 10.
# deque_list = ([2, 4, 6, 8, 10, 12, 14, 16])
# print('Print original deque:', deque_list)
# print('length of the deque is %d' % (len(deque_list)))
# print('length of the deque is:', len(deque_list))
# deque_list.clear()
# print(deque_list)

# 11.
# dq1 = ([2, 4, 6, 8, 10, 12, 14, 16])
# dq2 = dq1.copy()
# print("content of deque1",dq1)

# print("id of deque", id(dq1))

# print("content of deque2",dq2)

# print("id of deque", id(dq2))

# # checking the shalow copying:
# print("first element of deque1", id(dq1[0]))
# print("first element of deque2", id(dq2[0]))


# tuple = (2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 6, 9, 8, 7, 4, 5, 1, 2, 5, 4)
# # convert the tuple into deque
# deq_list = collections.deque(tuple)
# print("count the number in deque is:", deq_list.count(1))
# print("count the number in deque is:", deq_list.count(2))
# print("count the number in deque is:", deq_list.count(3))
# print("count the number in deque is:", deq_list.count(4))
# print("count the number in deque is:", deq_list.count(5))
# print("count the number in deque is:", deq_list.count(6))
# print("count the number in deque is:", deq_list.count(7))
# print("count the number in deque is:", deq_list.count(8))
# print("count the number in deque is:", deq_list.count(9))
# print("count the number in deque is:", deq_list.count(10))

# 13.
# obj_dq = collections.deque()
# obj_dq.append(2)
# obj_dq.append(3)
# obj_dq.append(5)
# obj_dq.append(6)
# obj_dq.append(7)
# obj_dq.append(8)
# obj_dq.append(9)
# obj_dq.append(1)

# print("print the element before the rotate function:", obj_dq)
# # rotate after 0 positive rotation
# obj_dq.rotate()
# print(obj_dq)

# # rotate after 2 positive rotation
# obj_dq.rotate(2)
# print(obj_dq)

# 14.
# obj_dq = collections.deque()
# obj_dq.append(2)
# obj_dq.append(3)
# obj_dq.append(5)
# obj_dq.append(6)
# obj_dq.append(7)
# obj_dq.append(8)
# obj_dq.append(9)
# obj_dq.append(1)

# print("print the element before the rotate function:", obj_dq)
# # rotate after 1 negative rotation
# obj_dq.rotate(-1)
# print(obj_dq)

# # rotate after 2 negative rotation
# obj_dq.rotate(-2)
# print(obj_dq)

# 15.
# from collections import Counter

# list = [2, 3, 4, 5, 6, 7, 8, 9, 1, 5, 6, 7, 8, 9, 2, 6, 6]
# print("oiginal list:", list)

# cnt = Counter(list)

# print("print the most common element:", cnt.most_common(1)[0][0])


# 16.
# import collections

# c1 = collections.Counter([2, 3, 4, 5, 6, 7])
# c2 = collections.Counter([4, 6, 8, 9, 2, 3])
# print("C1", c1)
# print("C2", c2)

# print('Combine string:', c1 + c2)
# print('Substraction:', c2 - c1)
# print('Intersection(taking positive minimum):', c1 & c2)
# print('Union(taking maximum):', c2 | c1)

# # 17.
# def printValues():
#   # create a empty list
#   l = list()
#   for i in range(1, 30):
#     l.append(i**2)
#     # print the first five element of the list
#   print('square', l[:5])
#   # print the last five element of the list
#   print('square', l[-5:])
# printValues()

# 18.
# import itertools

# print('All possible combinatin in list of integer:\n')
# print(list(itertools.permutations([1, 2, 3])))

# 19.
# l1 = [1, 3, 5, 7, 9]
# l2 = [1, 2, 4, 6, 7, 8]
# diff_l1_l2 = list(set(l1)-set(l2))
# diff_l2_l1 = list(set(l2)-set(l1))
# total_diff = diff_l1_l2+diff_l2_l1
# print('Total diff:'+str(total_diff))
#
# 20.
# l=[4, 2, 3, 9, 5, 6, 8]

# # Use a 'for' loop with 'enumerate' to iterate through 'nums' and obtain both
# #  the index and value of each element
# for e_index, e_num in enumerate(l):
#   print('print number with index=>',e_index , e_num)

#   # 21.
# ch = ['a', 'b', 'c', 'd', 'e']
# str = ', '.join(ch)
# print(str)

# 22.
# list = ['java', 'python', 'css', 'html', 'c++']

# print(list.index('python'))

# 23.
# import itertools

# orginal_num = ([7,4, 3], [2, 3, 6], [9], [8, 7, 5])

# print(list(itertools.chain(*orginal_num)))

# 24.
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [6, 5, 4, 9, 8, 7]

# # l1.extend(l2)
# # print(sorted(l1))
# # or
# append_num = l1+l2
# print(append_num)

# 25.
# import random

# l=[4, 5, 6, 9, 7, 2]
# print(random.choice(l))

# or
# from random import choice


# def random_element(lst):
#     return choice(lst)
# print(random_element(['red', 'blue', 'green', 'yellow', 'Orange']))

# 26
# list1 = [10, 10, 10, 0, 0]
# list2 = [10, 10, 0, 0, 10]
# list3 = [1, 10, 10, 0, 0]

# print('Compare the element of list1 and list2\n')

# print(''.join(map(str, list2)) in ''.join(map(str, list1*2)))


# print('Compare the element of list1 and list3\n')

# print(''.join(map(str, list3)) in ''.join(map(str, list1*2)))


# python Code:
# def secoud_smallest(numbers):
#     if len(numbers)<2:
#         return
#     if len(numbers) == 2 and numbers[0] == numbers[1]:
#         return

#     dup_items = set()
#     uniq_items = []

#     for x in numbers:
#         if x not in dup_items:
#             uniq_items.append(x)
#             dup_items.add(x)

#     uniq_items.sort()

#     return uniq_items[1]
# print(secoud_smallest([1, 2, -8, -2, 0, -2]))
# print(secoud_smallest([1, 1, 0, 0, 2, -2, -2]))
# print(secoud_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(secoud_smallest([2, 2]))
# print(secoud_smallest([1, 2]))

# 29.
# my_list = [10, 20, 30, 40, 20, 10, 60, 50, 30]

# print("Original list : ", my_list)
# my_set = set(my_list)
# my_new_list = list(my_set)
# print("Print Unique Value : ", my_new_list)

# 30.
# import collections

# list = [10, 20, 30, 40, 50, 60, 70, 80, 10, 20, 10, 30, 40, 50, 10, 20, 30, 50]
# print("orginal : ", list)

# ctr = collections.Counter(list)
# print("Count the the number in list : ", ctr)

# # 31.
# def count_range_in_list(li, min, max):

#     ctr = 0

#     for x in li:
#         if min <= x <= max:
#             ctr += 1
#     return ctr

# list1 = [10, 20, 30, 40, 50, 60, 70, 80, 99]
# print(count_range_in_list(list1, 40, 100))
# list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(count_range_in_list(list2, 'c', 'g'))

# 32.
# def is_Sublist(l, s):
#     sub_set = False
#     if s == []:
#         sub_set = True
#     elif l == s :
#         sub_set = True
#     elif len(s) > len(l):
#         sub_set = False
#     else:
#         for i in range(len(l)):
#             if l[i] == s[0]:
#                 n = 1
#                 while (n < len(s)) and (l[i+1] == s[n]):
#                     n += 1
#                 if n == len(s):
#                     sub_set = True

#     return sub_set
# a = [2, 4, 3, 5, 9, 8]
# b = [5, 9]
# c = [4, 8]
# print("Subset is:", is_Sublist(a, b))
# print("Subset is:", is_Sublist(a, c))

# 33.
# from itertools import combinations


# def sub_lists(my_list):
#     Subs = []
#     for i in range(0, len(my_list)+1):
#       temp = [list(x) for x in combinations(my_list, i)]
#       if len(temp) > 0:
#          Subs.extend(temp)
#     return Subs
# l1 = [10, 20, 30, 40]
# l2 = ['a', 'b', 'c']
# print('Original list1:', l1)

# print('sublist_of_list1 is:', sub_lists(l1))

# print('Original list2:', l2)

# print('sublist_of_list2 is:', sub_lists(l2))

# 34.
# def prime_aratosthene(n):
#     prime_list = []

#     for i in range(2, n+1):
#         if i not in prime_list:
#             print(i)
#         for j in range(i*i, n+1, i):
#             prime_list.append(j)
# prime_aratosthene(100)

# 35.
# from collections import Counter

# x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})

# print(x.most_common())

# 36.
# from collections import defaultdict

# list_value = ['class-V', 'class-VI', 'class-VII', 'class-VIII']
# list_id = [1, 2, 3, 4]

# temp = defaultdict(set)

# for c, i in zip(list_value, list_id):
#     temp[c].add(i)
# print(temp)

# 37.
# def sum_math_V_VI(list_of_dicts):
#     for d in list_of_dicts:
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V1 + V2'] = (n1+n2)
#     return list_of_dicts
# Student_details = [
#     {'id':1, 'Subject':'Math', 'V':70, 'VI':82},
#     {'id':2, 'Subject':'Math', 'V':73, 'VI':74},
#     {'id':3, 'Subject':'Math', 'V':75, 'VI':86}
# ]
# print(sum_math_V_VI(Student_details))

# 38.
# x = {'key1':1, 'key3':2, 'key2':3}
# y = {'key1':1, 'key2':2}

# for (key, value) in set(x.items()) & set(y.items()):
#     print('%s: %s is present in both x & y' %(key, value))


# 39.
# d = {
#     'students': [
#         {'firstName':'Nikki', 'lastName':'Rosyden'},
#         {'firstName':'Mervin', 'lastName':'Friedland'},
#         {'firstName':'Aron', 'lastName':'Wilkins'}
#         ],
#     'teachers':[
#         {'firstName':'Amberly', 'lastName':'Calico'},
#         {'firstName':'Regine', 'lastName':'Agtarap'}
#         ]
# }
# print('Original dictionary:', d)
# print(type(d))

# import json

# with open('dictionary', "w") as f:
#     json.dump(d, f, indent=4, sort_keys=True)
# print('\n json file to dictionary:')

# with open('dictionary') as f:
#     data = json.load(f)
# print(data)
#
# 40.
# from pprint import pprint

# dict_nums = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))

# pprint(dict_nums)

# print(dict_nums["x"][4])
# print(dict_nums["y"][4])
# print(dict_nums["z"][4])


# for k, v in dict_nums.items():
#     print(k, "has value", v)


# 41.
# l = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]

# print([t[:-1]+(100,) for t in l])

# 42.

# sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# L = [t for t in sample_data if t]
# print(L)

# 43.
# s_d = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# sorted_s_d = sorted(s_d, key=lambda x: float(x[1]), reverse=True)
# print(sorted_s_d)

# 44.
# num = [10, 20, (12, 13), 30, 40]

# ctr = 0

# for n in num:
#     if isinstance(n, tuple):
#         break
#     ctr+=1
# print(ctr)


# 45.
# setx = set(["green", "blue", "yellow", "red"])
# sety = set(["green", "yellow","black", "brown"])
# print("Original colorx:", setx)
# print("Original colory:", sety)
# setz = setx & sety
# print("print insertion(∩) set:-", setz)

# 46.
# setx = set(["green", "blue", "yellow", "red"])
# sety = set(["green", "yellow","black", "brown"])
# print("Original colorx:", setx)
# print("Original colory:", sety)
# setz = setx | sety
# print("print Union(∪) set:-", setz)

import faulthandler

47.
# setx = set(["green", "blue", "yellow", "red"])
# sety = set(["green", "yellow","black", "brown"])
# # print("Original colorx:", setx)
# # print("Original colory:", sety)
# # setz = setx - sety
# # print("print Diffrence set:-", setz)
# r1 = setx.difference(sety)
# print("difference in setx:", r1)

# r2 = sety.difference(setx)
# print("difference in sety:", r2)

# # 48.
# setx = set(["green", "blue", "yellow", "red"])
# sety = set(["green", "yellow","black", "brown"])

# r1 = setx.symmetric_difference(sety)
# r2 = sety.symmetric_difference(setx)
# print("Print the symmetric_diffrence_x:", r1)
# print("Print the symmetric_diffrence_y:", r2)

# n1 = set([1, 3, 5, 7, 9, 11, 13, 15])
# n2 = set([2, 4, 6, 8, 10, 12, 14, 16])

# s1 = n1.symmetric_difference(n2)
# s2 = n2.symmetric_difference(n1)
# print("Print the symmetric_diffrence_n1:", s1)
# print("Print the symmetric_diffrence_n2:", s2)

# p1 = set([0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 33, 37])
# p2 = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 11, 13, 17, 19, 23])
# k1 = p1 ^ p2
# k2 = p2 ^ p1
# print("Print the symmetric_diffrence_P1:", k1)
# print("Print the symmetric_diffrence_P2:", k2)

# 49.
# setx = set(["Mango", "Orange"])
# sety = set(["Orange", "blue"])
# setz = set(["Orange"])

# print("If setx is a subset of sety")
# print(setx <= sety)
# print(setx.issubset(sety))

# print("If setx is a subset of setz")
# print(setx <= setz)
# print(setx.issubset(setz))

# print("If sety is a subset of setz")
# print(sety <= setz)
# print(sety.issubset(setz))

# print("If sety is a subset of setx")
# print(sety <= setx)
# print(sety.issubset(setx))

# print("If setz is a subset of setx")
# print(setz <= setx)
# print(setz.issubset(setx))

# print("If setz is a subset of sety")
# print(setz <= sety)
# print(setz.issubset(sety))

# # 50.
# setp = set(["green", "red"])
# setq = set(["brown", "red"])

# setr = setp.copy()

# print(setr)


# 51.
# set = {'Ashok', 'shiva', 'Ruchi', 'shivani', 'Khushi', 'Abhishek'}
# print("ORIGINAL SET: ", set)
# print(type(set))
# set.clear()
# print("print after clear:", set)

# 52.
# x = frozenset([1, 2, 3, 4, 5])
# y = frozenset([3, 4, 5, 6, 7])
# print(x.isdisjoint(y))
# print(y.isdisjoint(x))
# print(x.difference(y))
# print(x | y)

# 53.
# p = {4, 5, 3, 2, 8, 9, 41, 25, 48, 26, 45}

# print(max(p))
# print(min(p))

# print('len of a set:', len(p))

# 54.(a)
# D = dict()
# for x in enumerate(range(2)):
#   D[x[0]] = x[1]
#   D[x[1]+7] = x[0]
# print(D)

# (b).
# D = {1: 1, 2: '2', '1': 1, '2': 3}
# D['1'] = 2
# print(D[D[D[str(D[1])]]])

# (c).
# D = {1: {'A':{1: "A"}, 2: "B"}, 3:"C", 'B': "D", "D": 'E'}
# print(D[D[D[1][2]]], end =" ")
# print(D[D[1]["A"][2]])

# D.
# D = dict()
# for i in range(3):
#   for j in range(2):
#     D[i] = j
# print(D)

# e.
# D = {1: [1, 2, 3], 2:(4, 6, 8)}
# D[1].append(4)
# print(D[1], end='')
# L = list(D[2])
# L.append(10)
# D[2] = tuple(L)
# print(D[2])

# # f.
# List = [True, 50, 10]
# List.insert(2, 5)
# print(List, 'Sum is', sum(List))

# # G.
# T = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(T[T.index(5)], end=' ')
# print(T[T[T[6]-3]-6])

# # h.
# L = [1, 3, 5, 7, 9]
# print(L.pop(-3), end=' ')
# print(L.remove(L[0]), end=' ')
# print(L)

# i.
# def REVERSE(L):
#   L.reverse()
#   return(L)
# def YKNJS(L):
#   List = list()
#   List.extend(REVERSE(L))
#   print(List)
# L = [1, 3.1, 5.31, 7.531]
# YKNJS(L)

# (j):
# from math import sqrt

# l1 = [x**2 for x in range(10)].pop()
# l1 += 19
# print(sqrt(l1), end=' ')
# l1 = [x**2 for x in reversed(range(10))].pop()
# l1 += 16
# print(int(sqrt(l1)))

# (k)
# l1 = list()
# l1.append([1, [2, 3], 4])
# l1.extend(7, 8, 9)
# print(l1[0][1][1]+l1[2])

# (l):
# l1 = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
# val1, val2 = 0,''
# for x in l1:
#   if(type(x) == int or type(x) == float):
#     val1 += x
#   elif(type(x) == str):
#     val2 += x
#   else:
#     break
#   print(val1, val2)

# m.
# l1 = [1, 2, 3, 4]
# l2 = l1
# l3 = l1.copy()
# l4 = list(l1)
# l1[0] = [5]
# print(l1, l2, l3, l4)

# n.
# import sys

# l1 = tuple()
# print(sys.getsizeof(l1), end=' ')
# l1 = (1, 2)
# print(sys.getsizeof(l1), end=' ')
# l1 = (1, 3, (4, 5))
# print(sys.getsizeof(l1), end=' ')
# l1 = (1, 2, 3, 4, 5, [3, 4], 'p', '8', 9.777, (1, 3))
# print(sys.getsizeof(l1))

# o.
T1 = (1)
T2 = (3, 4)
T1 += 5
print(T1)
print(T1, T2)
