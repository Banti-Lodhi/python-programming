# g = raw_input("Enter your name: ")
# print(g)


# 1.
# file = open("Ashok.txt", "r")
# print(file.read())

# or
# file = open("lorem.txt", "r")
# print(file.read(5))

# Creating a file using write mode:-
# file = open('lorem.txt', 'w')
# file.write("This is the write command.")
# file.write("It allows us to write in a particular file")
# file.close()

# Working of append() mode:

# file = open('lorem.txt', 'a')
# file.write("This will writes & add the next lines")
# file.close()

# auto cleanup:-
# with open("lorem.txt") as file:
#     data = file.read()

# with() function :-
# with open("Project_file.html", "w") as f:
#     f.write("Hello World!!")

# split using file handling:-
# with open("Project_file.html", 'r') as file:
#    data = file.readlines()
#    for line in data:
#       word = line.split()
#       print(word)

# os.pipe():-
# import os

# r, w = os.pipe()
# pid = os.pipe()
# if pid > 0:
#     os.close(r)
#     print("Parent process is writting")
#     text = b"Hello child Process"
#     os.write(w, text)
#     print("Written text:", text.decode())
# else:
#     os.close(w)
#     print("\nChild Process is reading")
#     r = os.fdopen(r) 
#     print("Read text:", r.read())
       

# Handling io Exception:-
# import sys


# def whatever():
#     try:
#       f = open("lorem.txt", 'r')
#     except IOError as e:
#        print(e)
#        print(sys.exc_type)
#        whatever()
    

# file = open("banti.txt", "w") 
# print(file.write("Hi, i'm banti kumar lodhi."))   
# file.close()

# with open("banti.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)

# import os

# r, w = os.pipe()
# pid = os.pipe()
# if pid > 0:
#     os.close(r)
#     print("Parent process is writing")
#     text = b"Hello child process"
#     os.write(w, text)
#     print("Written text:", text.decode())
# else:
#     os.close(w)
#     print("\nChild Process is reading")
#     r = os.fdopen(r)
#     print("Read text:", r.read())

import sys

# def whatever():
#     try:
#         f = open("banti.txt", "r")
#     except IOError:
#       print(f)
#       print(sys.exc_type())
#       whatever()
        
with open("banti.txt", "r") as file:
    data=file.readlines()  
    list = []
    for i in data:
       print([i])        
        
          
     