# f = open("sample.txt", "+a")
# f.write("abc")
# print(f.read())
# f.close()

# 2.
# with open("demo.txt", "r") as f:
#     point = f.read()
#     print(point)

# 3.
# with open("demo.txt", "w") as f:
#     f.write("new content add only this directory")

# remove file
# import os

# rem = os.remove("sample.txt")
# print(rem)


# practice set
# 1
# f = open("practice.txt", "w")
# f.close()

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O")
#     f.write("using Java.\nI like Programming in Java.")
# f.close()

# 2.
# with open("practice.txt", "r") as f:
#     read = f.read() 
# read_func = read.replace("Java", "Python")
# print(read_func)    
# f.close()      

# 3.
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()

#     if(data != -1):
#         print("Found")
#     else:
#         print("Not Found")

# 4.
# def check_for_line():
#     word = "learning"

#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()

# 5.
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    # or
    # count = 0
    # nums = data.split(",")
    # # print(nums)
    # for val in nums:
    #     if (int(val) % 2 == 0):
    #         count += 1
    # print(count)        


# 5.
# def read_last_line(fname, N):

#     with open(fname) as file:

#         for line in  (file.readlines() [-N:]):
#             print(line, end='')

# if __name__ == '__main__':
#     fname = 'banti.txt'
#     N=2
#     try:
#         str = read_last_line(fname, N)
#         print(str)
#     except:
#         print("File not found.")


# 5.
# def file_read(fname):
#     with open(fname) as f:
#         content_list = f.readlines()
#         print(content_list)

# file_read('banti.txt')


# 6.
# def file_read(fname):
#     with open(fname, 'r') as f:
#         content_list = f.readlines()
#         print(content_list)

# file_read('banti.txt')

# 7.
# def file_name(fname):
#     arr = []

#     with open(fname, 'r') as f:
#         words = f.read().split()
#     max_len = len(max(words, key=len))

#     for line in words:
#         if len(line) == max_len:
#             return line

# print(file_name("banti.txt"))           

# 9.
# def file_name(fname):
    
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass

#     return i+1
       
# print("The length of the file: ", file_name("banti.txt"))           

# 10.
# from collections import Counter


# def word_count(fname):
#     with open(fname) as f:        
#         return Counter(f.read().split())
        
# print("Number of word in file :", word_count("banti.txt"));    
    
# 11.
# def file_size(fname):
#     import os
#     statinfo = os.stat(fname)
#     return statinfo.st_size
# print("File size in bytes of a plain file: ", file_size("banti.txt"))    
     
     
# 12.
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open("banti.txt", "w") as myfile:
#     for c in color:
#         myfile.write("%s\n"% c)
# content = open('banti.txt')
# print(content.read())
     
     
#  13.
# from shutil import copyfile

# copyfile("banti.txt", "shiva.txt")

# with open("shiva.txt", "r") as f:
#     f1 = f.read()
#     print(f1)       

# 14.

# with open("banti.txt") as fh1, open("Shiva.txt") as fh2:
    
#     for line1, line2 in zip(fh1, fh2):
#         print(line1+line2) 

# 15.
# import random


# def random_file(fname):
#    lines = open(fname).read().splitlines()
#    return random.choice(lines)
# print(random_file("banti.txt"))

       
       
# 16.
# f = open("banti.txt") 
# print(f.close())
# f.close()
# print(f.close())

# # 17.
# def remove_newline(fname):
#     flist = open(fname).readlines() 
#     return [s.rstrip('\n') for s in flist]
# print(remove_newline("banti.txt"))

# 18.
# def count_words(filepath):
#     with open(filepath) as f:
#         data = f.read()
#         data.replace(",", " ")
#         return len(data.split(" "))
# print(count_words("banti.txt"))

# 19.

# import glob

# char_list = []
# files_list = glob.glob("*.txt")
# for file_elem in files_list:
#     with open(file_elem, "r") as f:
#         char_list.append(f.read())
# print(char_list)        


# 20. 
# import os

# import string

# if not os.path.exists("letters"):    
#     os.makedirs("letter"); 
      
# for letter in string.ascii_uppercase:
#     with open(letter+".txt", "w") as f:
#         f.writelines(letter)
    
    
# 21.
import string


def file_letter_line(n):
    with open("shiva.txt", "w") as f:
        Alphabet = string.ascii_uppercase
        letters = [Alphabet[i:i+n] + "\n" for i in range(0, len(Alphabet), n)]
        f.writelines(letters)
file_letter_line(3)        