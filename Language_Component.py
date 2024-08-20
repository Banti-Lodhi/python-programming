# # 1.
# for i in range(1500, 2700):
#     if(i%7==0)and(i%5==0):
#         print('result is', i)

# 2.
# #formula c/5=(f-32)/9
# # >60cel = 140f
# # >45f == 7cel

# # change celsius into Fareneheit:-
# cel = 60
# faherneheit = ((9*cel)//5)+(32)
# print("Value in fareneheit:",faherneheit,"°F")

# # change Fareneheit into celsius:-
# faherneheit = 45
# cel = 5*(faherneheit-32)//9
# print("Value in celsius:", cel,"°C")

# OR:-
# temp = input("Input temperature you like to convert?(e.g.45F, 102C etc):")
# degree = int(temp[:-1])
# o_convention = temp[-1]

# if o_convention.upper() == "C":
#     result = int(round((9*degree)/5+32))
#     i_convention = "Fareneheit"
# elif o_convention.upper() == "F":
#     result = int(round((degree-32) * 5/9))
#     i_convention = "Celcius"
# else:
#     print("Input proper convention.")
#     quit()
# print("The temperature in", i_convention, "is", result, "degrees.")


# 6.
# import random

# target_num, guess_num = random.randint(1, 10), 0

# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
#     print('Well guessed')

# 7.
# str = input("Enter a accepts a word \n")
# rev = str[::-1]
# print(str, "word is reverse word equal to: => ",rev)

# 8.
# num = int(input("Enter the number:\n"))

# odd_num = 0
# even_num = 0

# for num1 in range(1, num+1):
#     print(num1)
#     if num1 % 2 == 0:
#         even_num += 1
        
#     else:
#         odd_num += 1
      
# print("The total even number are equal to => ", even_num)
# print("The total odd number are equal to => ", odd_num)

# 9.
# datalist = [1452, 11.23, 1+2j, True, 'Asian Publishers', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for item in datalist:
#     print("Type of", item,"is", type(item))

# # 10.
# for i in range(6):
#     if (i==3 or i==6):
#         continue  
#     print(i, end=' ') 
# print("\n")   

# # 11.
# x, y=0,1
# while y<9:
#     print(y, end = " ")
#     x,y = y, x+y

# # 12=>
# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0  and fizzbuzz % 5 == 0:
#         print("FizzBuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("Fizz")  
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("Buzz")
#         continue 
#     print(fizzbuzz)     

# # 13.
# row_num = int(input("Input number of rows:\n"))
# col_num = int(input("Input number of columns:\n"))

# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#   for col in range(col_num):
#     multi_list[row][col] = row*col

# print(multi_list)

# 14.
# lines = []
# while True:
#   l = input()
#   if l:
#     lines.append(l.upper())
#   else:
#     break

# for l in lines:
#   print(l)    

# 15.
# items = []
# num = [x for x in input().split(',')]
# for p in num:
#   x = int(p, 2)
#   if not x%5:
#     items.append(p)
# print("divisible of 5 binary number =>",','.join(items))    

# 16.
# str = input("Input a String\n")
# L=D=0

# for c in str:
#   if c.isdigit():
#     D+=1
#   elif c.isalpha():
#     L+=1
#   else:
#     pass
# print("Total letter", L)
# print("Total Digit", D)  

# # 17.
# items = []
# for i in range(100, 401):
#   s = str(i)

#   if(int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
#     items.append(s)
# print(",".join(items))     

# 18.
# alpha = str(input("Enter a alphabet\n"))
# if alpha in ('a', 'e', 'i', 'o', 'u'):
#     print("%s is a vowel." %alpha)
# elif alpha == 'y':
#     print("Sometimes letter y stand for vowels, Sometimes stand for Consonants")
# else:
#     print("%s is a consonant."%alpha)

# 19.
# print("Name of month: January, February, March, April, May, June, July, August, September, Octubar, November, December")

# Month_name = input("Input the name of month?")

# if Month_name == 'February':
#     print("No. of days: 28/29 days")
# elif Month_name in ('April', 'June', 'September', 'November'):
#     print("No. of days: 30 days")
# elif Month_name in ('January', 'March', 'May', 'July', 'August', 'Octubar', 'December'):
#     print("No. of days: 31 days")
# else:
#     print("Invalid month choose your")
    
# 20.
# def sum(x, y):
#     sum = x+y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
# print(sum(10, 6))
# print(sum(10, 2))       
# print(sum(10, 9))       
# print(sum(10, 14))       
# print(sum(45, 12))       

# 21.
# text = input("Input a string\n")
# text = text.strip()
# if len(text) < 1:
#     print("Input a valid text")
# else:
#     if all(text[i] in "0123456789" for i in range(len(text))):
#         print("The string is an integer.")
#     elif (text[0] in "+-") and \
#           all(text[i] in "0123456789" for i in range(1, len(text))):
#           print("The string  is an integer")
#     else:
#          print('The string is not an integer') 

# 22->
# print("Input lengths of the tringale sides: ")
# while True:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     z = int(input("z: "))
#     if x == y == z:
#         print("Equivalent triangle\n")
#     elif x == y or y == z or z == x:
#         print("Isoscles triangle\n")
#     elif x != y or y != z or z != x:
#         print("Scalence triangle\n")
#     else:
#         print(exit)

# 23.
# Month = input("Input the month(e.g. January, February): ")
# Day = int(input("Input the day: ")) 

# if Month in ('January', 'February', 'March'):
#     season = 'Winter'
# elif Month in('April','May' 'June'):
#     season = 'Spring'
# elif Month in ('July', 'August', 'September'):
#     season = 'Summer'
# else:
#     season = 'Autumn'

# if (Month == 'March') and (Day > 19):
#     season = 'Spring'
# elif (Month == 'June') and (Day > 20):
#     season = 'Summer'
# elif (Month == 'September') and (Day > 21):
#     season = 'Autumn'
# elif (Month == 'December') and (Day > 20):
#     season = 'Winter'

# print("Season is ", season)    


# 24.
# day = int(input("Input birthday: "))
# month = input("Input month of birth (e.g. march, july etc.): ")
# if month == 'december':
#     astro_sign = 'Sagittrius' if(day < 22) else 'capricorn'
# elif month == 'january':
#     astro_sign = 'Capricon' if(day<20) else 'aquarius'
# elif month == 'february':
#     astro_sign = 'Aquarius' if(day<19) else 'pisces'
# elif month == 'march':
#     astro_sign = 'Pisces' if(day<21) else 'aries'
# elif month == 'april':
#     astro_sign = 'Aries' if(day<20) else 'taurus'
# elif month == 'may':
#     astro_sign = 'Taurus' if(day<21) else 'gemini'
# elif month == 'june':
#     astro_sign = 'Gemini' if(day<21) else 'cancer'
# elif month == 'july':
#     astro_sign = 'Cancer' if(day<23) else 'leo'
# elif month == 'august':
#     astro_sign = 'Lio' if(day<23) else 'virgo'
# elif month == 'september':
#     astro_sign = 'Virgo' if(day<23) else 'libra'
# elif month == 'october':
#     astro_sign = 'Libra' if(day<23) else 'scorpio'
# elif month == 'november':
#     astro_sign = 'Scorpio' if(day<22) else 'sagisttarius'
# print("Your Astrological sign is :", astro_sign)   

# 25.
# year = int(input("Input your birth year: "))
# if (year - 2000) % 12 == 0:
#     sign = 'Dragon'
# elif (year - 2000) % 12 == 1:
#     sign = 'Snake'
# elif (year - 2000) % 12 == 2:
#     sign = 'Horse'
# elif (year - 2000) % 12 == 3:
#     sign = 'sheep'
# elif (year - 2000) % 12 == 4:
#     sign = 'Monkey'
# elif (year - 2000) % 12 == 5:
#     sign = 'Rooster'
# elif (year - 2000) % 12 == 6:
#     sign = 'Dog'
# elif (year - 2000) % 12 == 7:
#     sign = 'Pig'
# elif (year - 2000) % 12 == 8:
#     sign = 'Rat'
# elif (year - 2000) % 12 == 9:
#     sign = 'Ox'
# elif (year - 2000) % 12 == 10:
#     sign = 'Tiger'
# else:
#     sign = 'Hare'    

# print("your Zodiac sign :", sign)    


# 26.
# str1 = float(input("Input the first number: "))
# str2 = float(input("Input the second number: "))
# str3 = float(input("Input the third number: "))

# if (str1 > str2) and (str1 < str3):
#     print("median number :", str1)
# elif (str1 < str2) and (str2 < str3):
#     print("median number :", str2)
# else:
#     print("median number :", str3)

# # 27.
# year = int(input("Input a year: "))

# if(year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif(year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False

# month = int(input("Input a month [1 - 12]: "))
# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30

# day = int(input("Input a day [1-31]: "))

# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is [yyyy-mm-dd] %d-%d-%d." %(year, month, day))        


# 28.
# print("Input the number of sum and average of n integer numbers(input 0 to exit the function")

# count = 0
# sum = 0.0
# number = 1
# while number != 0:
#     number = float(input(" "))
#     sum +=number
#     count+=1
# if count == 0:
#         print("sum of total number\n")
# else:
#     print("Average of the number is =>", sum / (count-1), "sum is =>", sum)

# 29.
num = int(input("Enter the number\n"))  
i=1
while True:
  while(i<=10):
    print("multiplication table:", num, "*", i, "=>", num*i)
    i+=1
