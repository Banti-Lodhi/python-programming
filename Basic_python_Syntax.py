# 1. Python is Dynamically Typed:-

# x=6
# print(type(x))
# x='Hello'
# print(type(x))


# Accessing Value in Strings:-
# str = "Preetam Singh"
# l = len(str)//2
# leave str to end the half string and after remainder string to print!
# print(str[l::])


# var1 = "Preetam Singh"
# result = var1[5:] #(same=>result = var1[8::]) Leave the first five character from a string and next all character prints
# print(result)

# result = var1[:-8] #Leave the last eight character from a string and remainder all character prints
# print(result)


# print(result)

# var2 = "Sanjay Singh"
# print(var1[0:7])
# print(var2[7:12])
# print(var1[0::2]) #one print and one leave word print statement := PetmSnh
# print(var2[-1::-1]) #reverse name
# print(var1[-1::-2])

# Updating Strings:-
# var1 = "Preetam Singh"
# print(var1[:7]+" Data Scientist")

# Escape Characters:-
# print("1 Preetam\aSingh")
# print("2 Preetam\bSingh")
# print("3 Preetam\cx Singh")
# print("4 Preetam\C-x Singh")
# print("5 Preetam\e Singh")
# print("6 Preetam\f Singh")
# print("7 Preetam\M-\C-x Singh")
# print("8 Preetam\n Singh")
# print("9 Preetam\nnn Singh")
# print("10 Preetam\r Singh")
# import time


# def update_progress(progress):
#     # Move cursor to the beginning of the line using \r
#     print("\rProgress: [{:<50}] {:.2f}%".format("=" * int(progress * 50), progress * 100), end='', flush=True)

# def long_running_task():
#     for i in range(101):
#         update_progress(i / 100)
#         time.sleep(0.1)

#     print("\nTask completed.")

# long_running_task()

# print("11 Preetam\s Singh")
# import re

# Sample text containing whitespace
# text = " This is some text   with     various    whitespace."

# # Using regular expression to split the text based on whitespace
# words = ('\s', text)

# # Printing the words
# print(words)


# print("12 Preetam\t Singh")
# print("13 Preetam\v Singh")
# print("14 Preetam\x Singh")
# print("15 Preetam\xnn Singh")

## String  Methos:-

# name = "prEeTaM"
# # result = name.capitalize()

# result = name.casefold()
# print(result)

# txt = "Mango"
# result = txt.center(20)

# print(txt.center(20, "O"))
# print(result)

# print(txt.encode())

# print("Sonu".encode())

# Unicode string():-
# print(u'Asign publishers')

# txt = "Hello, Welcome my world."
# x=txt.endswith(".")
# print(x)

# txt = "H\te\tl\tl\to"
# print(txt)
# x = txt.expandtabs(2)
# print(x)

# str = "Preetam Singh Sanjay Sohany Mohany"
# print(str.find("Sanjay"))

# txt = "For only {price:.2f} dollslrs"

# print(txt.format(price = 49))

# txt1 = "My name is {fName}, I'm {age}.".format(fName="Preetam Singh", age=20)
# txt2 = "My name is {1}, I'm {0}.".format(23, "Surendr Singh")
# txt3 = "My name is {}, I'm {}.".format("Hemant Singh", 25)
# print(txt1)
# print(txt2)
# print(txt3)

# format_map():-
# txt1 = {'x':'Preetam', 'y':'Data Scientist'}
# print("{x}'s last_name is {y}".format_map(txt1))

# Index():-
# str = ("Preetam Singh", "Sanjay", "Mohany", "Himanshu", "Sooryansh", "Banti kumar")
# result = str.index("Mohany")
# print(result)

# More activity of format function:-

# Left side space
# txt = "We have {:<8} Phones"
# print(txt.format(45))

# Right  side space
# txt = "We have {:>8} Phones"
# print(txt.format(45))

# Center side space
# txt = "We have {:^8} Phones"
# print(txt.format(45))

# To place the plus/minus sign at the left most position:-
# txt = "The temp is {:=8} deg celsius"
# print(txt.format(-23))

# txt = "The temp is between {:+} and {:+} deg celsius"
# print(txt.format(-23, 26))

# txt = "The temp is between {:-} and {:-} deg celsius"
# print(txt.format(-3, 28))

# txt = "The temp is between {: } and {: } deg celsius"
# print(txt.format(3, 26))

# txt = "The universe is {:,} yeras old."
# print(txt.format(2000000000))

# txt = "The universe is {:_} yeras old."
# print(txt.format(5000000000))

# txt = "The binary version of {0} is {0:b}"
# print(txt.format(2))

# txt = "The decimal version of binary number is {:d}"
# print(txt.format(0b1010))

# Convert the decimal into scientific format :-
# txt = "We have more than from {:e} cars"
# print(txt.format(130000000))

# txt = "We have more money from {:.2f} dollors"
# print(txt.format(126))

# txt = "The octal version of {0} is {0:o}"
# print(txt.format(10))

# "Use 'x' to convert number into hex format"
# txt = "The hexadecimal number  version of {0} is {0:x}"
# print(txt.format(254))

# Use '%' to convert the number into pecentage format:-
# txt = "The percentage number version of {0} is {0:%}"
# print(txt.format(0.25))

# txt = "Company12"
# txt1 = "Company124@gmail.com"
# print(txt.isalnum())
# print(txt1.isalnum())

# str = "PreetamSingh"
# print(str.isalpha())

# num = "1225"
# print(num.isdecimal())
# print(num.isdigit())

# str = "Preetam_Singh"
# print(str.isidentifier())

# str = "preetam"
# print(str.islower())


# str = "1245"
# print(str.isnumeric())

# str = "bantikumar05092005@gmail.com"
# print(str.isprintable())

# txt = "Mi casa, Su casa"
# print(txt.rfind("casa"))

# txt = "Mi casa, Su casa"
# print(txt.rindex("casa"))

# txt = "banana"
# x=txt.rjust(20)
# print(x, "is my favorite fruit!")

# txt = "I could eat bananas all day, bananas are my favorite fruit"
# print(txt.rpartition("bananas"))

# txt = "apple, bananas, cherry"
# print(txt.rsplit(", "))

# txt = "Welcome to the jungle"
# print(txt.split())
# A = ['Welcome', 'to', 'the', 'jungle']
# print(type(A))
# txt = "Thank you for the music\nWelcome to the jugle"
# print(txt.splitlines())

# txt = "Hello, welcome to my world."
# print(txt.startswith("Hello"))

# txt = "       banana      "
# print("of all fruits", txt.strip(), "is my favoite")

# txt = "Hello My Name Is PETER"
# print(txt.swapcase())

# txt = "Welcome to my world"
# print(txt.title())

# mydict = {83: 80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))


# txt = "Hello my friends"
# print(txt.upper())


# txt = "50"
# print(txt.zfill(10))

# a = 'Hello'
# print(a[1:8])

# print('H' in a)
# print('M' not in a)
# print(a[::-1])


# s='4'
# c = ord(s)
# print("After converting ch. to integer: ", end = "")
# print(c)

# c = hex(56)
# print("After 56 ch. to hex: ", end = "")
# print(c)
# c = oct(56)
# print("After 56 ch. to oct: ", end = "")
# print(c)
# s = {'s', 'a', 'i', 'n'}
# print(type(s))

# p = 'Preetam Singh'
# print(list(p))
# print(type(p))

# dic = (("Preetam", 101), ("Sanjay", 102), ("Mohany", 103), ("Sohany", 104))
# print(dict(dic))
# print(str("Preetam"))

# print(complex(1, 3))

# g = input("Enter your name:")
# print(g)

# print("My first name is %s and last name is %s"%('Preetam Singh', 'data science'))
# print("My first name is %c and last name is %c"%('Preetam Singh', 'data science'))
# x=lambda a : a + 10
# print(x(5))
# username = raw_input("Enter username:")
# print("Username is: " + username)

# x = lambda a : a+3
# print(x(10))


# Exercize:-

# 3.
# string = "abcdefghij"
# length = len(string)
# print(length)
# length = length//2 -1
# print(length)
# print(string[length:length+3])

# 4:-
# s1 = "Preetam"
# s2 = "sanjay"
# l = len(s1)//2
# print(s1[0:l]+s2+s1[l::])


# 5:-

# def function(s1, s2):
#   l1 = len(s1)//2
#   l2 = len(s2)//2

#   s = (s1[0]+s2[0]+s1[l1]+s2[l2]+s1[-1]+s2[-1])
#   return s
# print(function("Preetam", "sanjay"))


# #6.
# st1 = input()
# # lower casee
# s = ''
# # Upper case
# S = ''
# for i in st1:
#     if i.islower():
#         s+=i
#     elif i.isupper():
#         S+=i
# # print(sorted(s)+sorted(S) )
# print(s+S)

# 7.
# chars = 0
# digits = 0
# symbol = 0

# str1 = 'Bantikumar05092005@#$%^&*@gmail.com'
# for i in str1:
#     if i.islower() or i.isupper():
#         chars+=1
#     elif i.isnumeric():
#         digits+=1
#     else:
#         symbol+=1
# print("chars: ",chars) 
# print("digits: ",digits)
# print("symbol: ", symbol)


# 8.
# s = 'Abc'
# s1 = 'Xyz'
# s2 = ''
# for i in range(len(s)):
#     s2+=s[i]
#     s2+=s1[-i-1]
# print(s2)    
       
# 9.
# s = "Preetam"
# for i in range(len(s)):
#     print(i)
    
# 10.
# s1 = 'Preetam Singh'
# s2 = 'Sanjay singh'

# for i in s1:
#     if s2 in i:
#         res = True
#     else:
#         res = False
#         break
# print(res)

# 10.
# s1 = 'Preetam Singh'
# l = len(s1)
# print(l)

# 10.
# def char_frequency(str1):
#   dict = {} 
#   for n in str1:
#       keys = dict.keys()
#       if n in keys:
#         dict[n] += 1
#       else:
#         dict[n] = 1
#   return dict
# print(char_frequency('google.com'))

# 11.
# def function(str):  
#   if len(str)<2:
#     return "Instead of the empty string" 
  
#   return (str[0:2]+str[-2:])    

# print(function("Hello numasate"))
# print(function("b"))
# print(function("Sy"))

# 12.
# def function(str):
#     char = str[0]
#     print(char)
#     str = str.replace(char, '$')
#     print(str)
#     str = char + str[1:]
#     return str
# print(function("restart"))

# 13.
# a = 'xyz'
# b = 'abc'
# print('Before swap : ', a , b)
# a1 = a[:2]+b[2:]
# a2 = b[:2]+a[2:]
# print('After swap : ', a1 , a2)

# 14:-

# def add_string(str):
#     length = len(str)
#     if length > 2:
#       if str[-3:] == 'ing':
#         str += 'ly'
#       else:
#         str += 'ing'
#     return str
# print(add_string("preetam")) 
# 
# 15.
# def not_poor(str1):
#     snot = str1.find('not')
#     spoor = str1.find('poor') 


#     if spoor > snot and snot>0 and spoor>0:
#         str1 = str1.replace(str1[snot:(spoor+4)], 'good')
#         return str1
#     else:
#         return str1 
# print(not_poor('The lyrics is not that poor!'))
# print(not_poor('The lyrics is poor!'))


# 16.
# def LongetstLength(a):
#     max1 = len(a[0])
#     temp = a[0]

# #for loop to traverse the list
#     for i in a:
#         if(len(i)>max1):
            
#             max1 = len(i)
#             temp = i

#     print("The word with longest length is :", temp, "and length is", max1)             

# a = ["Preetam", "Sanjay", "Sohany", "Mohany", "Polytechnic"]
# LongetstLength(a)

# 17.

# def char_remove(str, n):
#     first_part = str[:n]
#     last_part = str[n+1:]
#     return first_part+last_part
# print(char_remove('python', 0))
# print(char_remove('python', 2))
# print(char_remove('python', 3))

# or

# declaring a string variable
# str = "Geeksforgeeks is fun."
 
# # index to remove character at
# n = 4
 
# # declaring an empty string variable for storing modified string
# modified_str = ''
 
# # iterating over the string
# for char in range(0, len(str)):
 
#     # checking if the char index is equivalent to n
#     if(char != n):
#         # append original string character
#         modified_str += str[char]
 
# print("Modified string after removing ", n, "th character ")
# print(modified_str)


# 18.
# def change_str(str1):
#     return str1[-1:]+str1[1:-1]+str1[:1]
# print(change_str('shakuntala'))
# print(change_str('125475'))

# # 19.
# def odd_values_str(str1):
#     result = " "
#     for i in range(len(str1)):
#         if (i % 2) == 0:
#             result += str1[i]
#     return result
        
# print(odd_values_str('Santosh Lodhi'))        

#20.
# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word]=1
            
#     return counts
# print(word_count("the quick brown for jumps over the lazy dog."))

# 21.
# user_input = input("What's your favorite language?\n ")
# print("My favorite language is ", user_input.upper())
# print("My favorite language is ", user_input.lower())

# 22.
# items = input("Input a comma separated sequence of words\n")

# words = [word for word in items.split(", ")]
# print(", ". join(sorted(list(set(words)))))

# 23.
# def insert_string_middle(str, word):
#     return str[:2]+word+str[2:]
# print(insert_string_middle('[[]]', 'python'))
# print(insert_string_middle('{{}}', 'php'))
# print(insert_string_middle('<<>>', 'HTML'))

# # 24.
# def insert_end(str):
#     copies = str[-2:]
#     return copies*4
# print(insert_end('python'))    
# print(insert_end('Exercize'))    
# print(insert_end('S'))    

#25.
# def count_ch_position(str1):
#     count_chars = 0
#     for i in range(len(str1)):
#         if((i == ord(str1[i])- ord('A')) or (i == ord(str1[i])- ord('a'))):
#             count_chars += 1
#     return count_chars         
# str1 = input("Input a string: ")
# print("Number of characters of the said string at same position as in english alphabet:")
# print(count_ch_position(str1))

# 26.type casting 
# n = 2
# print(float(n)) 
# print(bool(n))
# print(ord('6'))

# # 26.
# print (4-2*2)
# print(9/3)
# print(9%3)
# print(10%3)
# print(10**4)
# print(10**2*2)

# str="Umbrella"

# if 'e' in str:
#     print("e is present in the", str, "at the index is", str.index('e'))
# else:
#     print("Not present in the", str, "string")


# 29.
# str = "Hello", "Good", "Morning", "World"
# print(", ".join(str))

# # 30>
# vowels=0
# consonents=0
# digits=0
# whitespace=0
# Special_character = 0
# str = input("Enter a string:\n")

# #length function is used to count
# #number of characters in the string
# for i in range(0, len(str)):
#     ch = str[i]

#     if((ch>='a'and ch<='z') or
#        (ch>='A'and ch<='Z')):
#         # To convert upper case in lower case
#         ch = ch.lower()
#         if(ch == 'a' or ch == 'e' or ch == 'i' or
#            ch == 'o' or ch == 'u'):
#             vowels += 1
#         else:
#             consonents+=1
#     elif(ch>='0' and ch <= '9'):
#         digits+=1
#     elif(ch == " "):
#         whitespace+=1
#     else:
#         Special_character+=1              
# print("string:", str)        
# print("Vowels:", vowels)
# print("Consonennts:", consonents)
# print("Digits",digits)
# print("White space", whitespace)
# print("Special_character:", Special_character)


# 31.
# a = ['a','e','i','o','u','A','E','I','O','U',' ']  
# b = "Hello, have a good day"
# c = " "
# for i in b:
#     if i not in a:
#        continue
#     else:
#         c+=i 
# print(c) 


# 32.
# def name(str):
# #split the string into a list     
#     l = str.split()
#     new = ""

# #traverse in the list 
#     for i in range(len(l)-1):
#         str = l[i]

# #         adds the capital first character]
#         new += (str[0].upper()+'.')
# #         l[-1] gives last item of list 1. we
# # use title to print first character in capital
#     new += l[-1].title()

#     return new
# print(name("data scientist Preetam"))

# 33.
# def isPalindrome(str):
#     return str == str[::-1]                

# # Driver code
# str = "malayalam"
# ans = isPalindrome(str)
# if ans:
#     print('yes')
# else:
#     print('No')

# # 34.
# a = "This is the lion in the cage"
# a = a.split()
# for i in a:
#     if i == 'the':
#         del(a[a.index(i)])
# print(a)
# print(" ".join(a))   

# 35.
# a = "This is an umbrella"
# a = a.split()
# max = a[0]
# max_len = len(a[0])
# for i in a:
#     if len(i)>max_len:
#         max_len = len(i)
#         max = i
# print(max)         
                
