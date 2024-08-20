# # 1.
# import datetime
# import time

# # (a):
# x = datetime.datetime.now()
# print('Current date and time ' ,x)
# # (b):
# print('Current year: ', datetime.date.today().strftime("%Y"))
# # (c)
# print('Month of  year: ', datetime.date.today().strftime("%B"))
# # (d)
# print('Week number of the year: ', datetime.date.today().strftime("%W"))
# # (e)
# print('Weekday of the week', datetime.date.today().strftime('%w'))
# #(f)
# print('Day of year: ', datetime.date.today().strftime("%j"))
# #(g)
# print('Day of the month:', datetime.date.today().strftime("%d"))
# #(h)
# print('Day of week', datetime.date.today().strftime("%A"))


# # 2.
# def leap_year(y):
    
#     if y % 400 == 0:
#         return True
#     if y % 100 == 0:
#         return False
#     if y % 4 == 0:
#         return True
#     else:
#         return False

# print('Year is a leap year :',leap_year(1900))
# print('Year is a leap year :',leap_year(2023))
# print('Year is a leap year :',leap_year(2024))

# # 3.
# from datetime import datetime

# date_object = datetime.strptime('Jan 1 2024 2:43PM', '%b %d %Y %I:%M%p')
# print(date_object)

# 4.
# import datetime

# print('Current time: ', datetime.datetime.now().time())

# 5.
# from datetime import date, timedelta

# dt = date.today()-timedelta(5)

# print('current time:', date.today())
# print('5 days before current date:', dt)


# 6.
# Unix time stamp string
# import datetime

# print(
#     datetime.datetime.fromtimestamp(
#         int("1284105682")
#     ).strftime('%Y-%m-%d %H:%M:%S')
# )

# 7.
# import datetime

# today = datetime.datetime.today()

# yesterday = today-datetime.timedelta(days=1)

# tomarrow = today+datetime.timedelta(days=1)

# print('Today', today)
# print('Yesterday', yesterday)
# print('tomarrow:', tomarrow)

# 8.
# from datetime import date, datetime

# dt = date.today()

# print(datetime.combine(dt, datetime.min.time()))

# 9.
# import datetime

# current_date = datetime.datetime.today()
# print('Current time:', current_date)
# for x in range(0, 5):
#   print('print next', x, 'days starting from today:', current_date+datetime.timedelta(days=x))

# 10.
# import datetime

# x = datetime.datetime.now()
# y = x + datetime.timedelta(0, 5)

# print('currrent time:', x.time())
# print('5 sec add after print the time:', y.time())

# 11.
# import datetime

# today = datetime.datetime.now()

# day_of_year = (today-datetime.datetime(today.year, 1, 1)).days+1
# print(day_of_year)

# 12.
# import time

# milli_sec = int(round(time.time() * 1000))
# print(milli_sec)

# # 13.
# import datetime

# print(datetime.date(2015, 6, 16).isocalendar()[1])


# 14.
# import time

# print(time.asctime(time.strptime('2015 50 1', '%Y %W %w')))

# # 15.
# from datetime import date, timedelta

# def all_sundays(year):
#     # January 1st of the given year
#     dt = date(year, 1, 1)
#     # First Sunday of the given year

#     dt += timedelta(days=6 - dt.weekday())

#     while dt.year == year:
#         yield dt
#         dt += timedelta(days=7)

# for s in all_sundays(2000):
#     print('print total sunday is: ', s)      

  
# 16.
# import datetime
# from datetime import date

# def addYears(d, years):
#     try:
#         # Return same day of current year
#         return d.replace(year = d.year + years)
#     except ValueError:
#         return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1)) 

# print(addYears(datetime.date(2015, 1, 1), -1))    
# print(addYears(datetime.date(2015, 1, 1), 0))    
# print(addYears(datetime.date(2015, 1, 1), 2))    
# print(addYears(datetime.date(2015, 1, 1), 1))    
# print(addYears(datetime.date(2015, 1, 1), 3))
# 
#17.
# import datetime

# drop_microsecounds = datetime.datetime.today().replace(microsecond=0)
# print()
# print(drop_microsecounds)
# print()
        
# 18.
# from datetime import date

# a = date(2000, 2, 28)
# b = date(2001, 5, 18)

# print('days=', b-a)

# # 19.
# from datetime import date, timedelta

# today = date.today()

# offset = (today.weekday()-1) % 7

# last_tuesday = today - timedelta(days=offset)

# print(last_tuesday)

# # 20.
# from datetime import datetime


# def t_third_tues(s):
#    d = datetime.strptime(s, '%b %d, %Y')
#    return d.weekday() == 1 and 14 < d.day < 22
# print(t_third_tues('jun 22, 2023'))
# print(t_third_tues('jun 25, 2024'))
# print(t_third_tues('jun 24, 2022'))
# print(t_third_tues('jun 16, 2015'))
# print(t_third_tues('jun 25, 2027'))
# print(t_third_tues('jul 21, 2015'))

# 21.
# import calendar

# year = 2015
# month = 9

# print(calendar.monthrange(year, month)[1])

# 22.
# from calendar import monthrange

# year = 2016
# month = 2

# print(monthrange(year, month))

# 23.
# import calendar
# from datetime import date, timedelta

# start_date = date(2014, 12, 25)
# days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
# print(start_date+timedelta(days=days_in_month))

# 24.
# import datetime
# from datetime import datetime
# monday1 = 0
# months = range

# # 25.
# import datetime
# from datetime import datetime

# monday1 = 0
# months = range(1, 13)
# for year in range(2015, 2017):
#     for month in months:
#         if datetime(year, month, 1).weekday() == 0:
#             monday1 += 1
# print(monday1)            
        
# # 25.
# import time

# x = 0

# while x < 5:
#     print('preetam singh\n')

#     time.sleep(2)

#     x += 1

# 26.
# import datetime

# print((datetime.date.today()+datetime.timedelta(6*365/12)).isoformat())


# 27.
# import datetime


# def every_20_days(date):
#     print('Starting Date: {d}'.format(d=date))
#     print("Next 12 days :")
#     for _ in range(12):
#         date=date+datetime.timedelta(days=20)
#         print('{d}'.format(d=date))

# dt = datetime.date(2016, 8, 1)
# every_20_days(dt) 

# 28.
# from datetime import date, timedelta

# current_date = date.today().isoformat()

# days_before = (date.today() - timedelta(days=30)).isoformat()

# days_after = (date.today() + timedelta(days=30)).isoformat()

# print('\nCurrent Date: ', current_date)
# print('\n30 before current date: ', days_before)
# print('\n30 after current date', days_after)

 # 29.
# import time
# from time import gmtime, strftime

# print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
# print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))


# # 30.
# import datetime

# import time

# now = datetime.datetime.now()

# print()
# print(time.mktime(now.timetuple()))
# print()

# 31.
# import datetime
# import time

# s = '05/09/2005'

# print()
# print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))

# 32.
# import datetime
# from datetime import date


# def differ_days(date1, date2):
#     a = date1
#     b = date2
#     return (a-b).days
# print()
# print(differ_days(date(2016, 10, 12), date(2015, 12, 10)))
# print(differ_days(date(2016, 3, 23), date(2017, 12, 10)))
# print()

# 33.
# import datetime
# from datetime import datetime


# def differ_days(date1, date2):
    
#     a = date1
#     b = date2
#     return (a-b).days
# print()
# print(differ_days(datetime(2016,10,12), datetime(2015,12,10)))
# print(differ_days(datetime(2016,3,23), datetime(2017,12,10)))
# print()

# 34.\
# import time

# print()
# print(time.ctime())
# print()

# 35.
# import datetime
# import time

# dt = datetime.datetime(2016, 2, 25, 3, 23)
# print()
# print("Unix Timestamp: ", (time.mktime(dt.timetuple())))
# print()

# 36.
# from datetime import datetime, time


# def date_diff_in_s(dt2, dt1):
#     timedelta = dt2-dt1
#     return timedelta.days* 24 * 3600 + timedelta.seconds
# # Specified date
# date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
# # current date
# date2 = datetime.now()
# print("\n%d seconds "%(date_diff_in_s(date2, date1)))
# print(284500756  / (3600 * 24 * 365))

# 37.
# from datetime import datetime, time


# def date_diff_in_seconds(dt2, dt1):
#     timedelta = (dt2-dt1)
#     return timedelta.days * 24 * 3600 + timedelta.seconds

# def dhms_from_seconds(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     days, hours = divmod(hours, 24)
#     return(days, hours, minutes, seconds)

# # Specified date
# date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

# # Current date
# date2 = datetime.now()

# print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
# print()

# 38.
# import os
# import time


# def last_modified_fileinfo(filepath):
    
#     filestat = os.stat(filepath)
#     date = time.localtime(filestat.st_mtime)
#     # Extract year, month and day from the date
#     year = date[0]
#     month = date[1]
#     day = date[2]

#     # Extract hour, minute, second
#     hour = date[3]
#     minute = date[4]
#     second = date[5]
#     # Year 
#     strYear = str(year)[0:]
#     # Month
#     if(month <= 9):
#         strMonth = '0'+str(month)
#     else:
#         strMonth = str(month)

#     # Date
#     if (day <= 9):
#         strDay = '0'+str(day)
#     else:
#         strDay = str(day)

#     return (strYear+"_"+strMonth+"-"+strDay+" "+str(hour)+":"+str(minute)+":"+str(second))    

# print()

# print(last_modified_fileinfo('Ashok.txt'))

# 39.
# from datetime import date


# def calculate_age(dtob):
#     today = date.today()
#     return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
# print()
# print(calculate_age(date(2006, 10, 12)))
# print(calculate_age(date(2005, 9, 5)))

# 40.
# import datetime
# import time

# print()

# print("Time in seconds the epoch: %s" %time.time())
# print("Current date and time: ", datetime.datetime.now())
# print("Alternate date and time: ", datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month: ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))
# print()

# 41.
# import datetime

# now = datetime.datetime.now()

# print()

# print("In string: ", now.strftime("%Y-%m-%d %H:%M:%S %p"))

# 42.
# import calendar

# cal = calendar.TextCalendar(calendar.SUNDAY)
# print('First Month - 2024')
# print(cal.prmonth(2022, 1))


# # 43
# import calendar

# # year: 2022, column width: 2, lines per week: 1
# # number of spaces between month columns: 1

# cal = calendar.TextCalendar(calendar.SUNDAY)
# print(cal.formatyear(2024, 4, 2, 3, 4))

# # 44.
# import calendar

# cal = calendar.LocaleTextCalendar()
# print(cal.prmonth(2024, 9))


# 45.
# import datetime

# curr_week = datetime.date(2005, 9, 5)
# year, week_num, day_of_week = curr_week.isocalendar()
# print()
# print("Year %d, Week Number %d, Day of the Week %d" %(year, week_num, day_of_week))
# print()

# 46.

# import calendar

# htmlcal = calendar.HTMLCalendar(calendar.MONDAY)

# print(htmlcal.formatmonth(2020, 12))

# 47.
# import calendar

# for month in range(1, 3):
#     cal = calendar.monthcalendar(2024, month)

#     first_week = cal[0]
#     second_week = cal[1]
#     third_week = cal[2]

#     if first_week[calendar.SATURDAY]:
#         holi_day = second_week[calendar.SATURDAY]
#     else:
#         holi_day = third_week[calendar.SATURDAY]

#     print('%3s: %2s' %(calendar.month_abbr[month], holi_day))
# 

# 48.
# import calendar

# year = int(input("Enter the year:")) #Here , it will take the year

# month = int(input("Enter the month")) #Here , it will take the month

# # Now, we will show the calender.

# print("The calender of", calendar.month(year, month))

# 49.
# from datetime import datetime

# str = "22 February, 2024 11:31AM"
# result = datetime.strptime(str, "%d %B, %Y %I:%M%p")
# print(result)
# print(type(result))
# 50.
# from datetime import date, timedelta


# def daterange(date1, date2):
#     for n in range(int((date2-date1).days)+1):
#         yield date1 + timedelta(n)

# start_dt = date(2015, 12, 20)
# end_dt = date(2016, 4, 7)

# for dt in daterange(start_dt, end_dt):
#     print([dt.strftime("%Y-%m-%d")])

# # 51.
# from datetime import datetime, timezone

# local_time = datetime.now(timezone.utc).astimezone()
# print()
# print(local_time.isoformat())
# print()

# # 52.
# import datetime

# print("First secound: ", datetime.time.min)
# print("second secound: ", datetime.time.max)


# 53.
# import random

# results = {
#     'heads' : 0,
#     'tails' : 0,
# }


# sides = list(results.keys())

# for i in range(10000):
#     results[random.choice(sides)] += 1

# print('Heads:', results['heads'])
# print('Tails:', results['tails'])    

# import random

# results = {
#     'heads': 0,
#     'tails': 0,
# }
# sides = list(results.keys())

# for i in range(10000):
#     results[random.choice(sides)] += 1

# print('Heads:', results['heads'])
# print('Tails:', results['tails'])

# 54.  
# import random

# with open('/usr/share/dict/words', 'rt') as fh:
#     words = fh.readlines()
# words = [w.rstrip() for w in words]
# for w in random.sample(words, 7):
#     print(w)

# 55.
# import random

# list = ["red" "blue", "black", "pink", "Orange", "Yellow", "Green"]

# print(random.choice(list))
            
# 56.
# import math

# print(math.fabs(-2.1))
# print(math.fabs(-0.0))
# print(math.fabs(10.1))
# print(math.fabs(0.0))

# 57.
# Data = [4, 2, 5, 8, 6]

# sum = 0
# for i in range(len(Data)):
#     sum += Data[i]
# print("Standard Deviation:", sum/len(Data))    

# 58.
# import math
# import sys


# def sd_calc(data):
#     n = len(data)

#     if n <= 1:
#         return 0.0
#     mean, sd = avg_calc(data), 0.0

#     #calculate stan. dev.
#     for el in data:
#         sd += (float(el) - mean)**2
#     sd = math.sqrt(sd / float(n-1)) 

#     return sd
# def avg_calc(ls):
#     n, mean = len(ls), 0.0

#     #calculate average
#     for el in ls:
#         mean = mean + float(el)
#     mean = mean / float(n)
#     return mean
# data = [4, 2, 5, 8, 6]
# print("Sample Data: ", data)
# print("Standard Deviation : ", sd_calc(data))    

# import math

# print('{:^7} {:^8} {:^17}'.format('Manatissa', 'Exponent', 'Floating point value'))
# print('{:-^8} {:-^8} {:-^20}'.format('', '', ''))

# for m, e in [ (0.7, -3),
#               (0.3, 0),
#               (0.5, 3),
#               ]:
#     x = math.ldexp(m, e)

#     # returns x * (2**i) of the given numbers x and i

#     print('{:7.2f} {:7d} {:7.2f}'.format(m, e, x))

# # 59.
# import math

# print('            (F)  (I)')
# for i in range(6):
#     print('{}/2 == {} {}'.format(i, i/2, math.modf(i/2.0)))

# print(math.modf(100.13))

# 60.
# import ast

# def recurse(node):
#     if isinstance(node, ast.BinOp):
#         if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
#             print('(', end='')
#         recurse(node.left)
#         recurse(node.op)
#         recurse(node.right) 
#         if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
#             print(')', end='')
#     elif isinstance(node, ast.Add):
#         print('+', end='')

#     elif isinstance(node, ast.Sub):
#         print('-', end='') 

#     elif isinstance(node, ast.Mult):
#         print('*', end='') 

#     elif isinstance(node, ast.Div):
#         print('/', end='')  
        
#     elif isinstance(node, ast.Num):
#         print(node.n, end='')
        
#     else:
#         for child in ast.iter_child_nodes(node):
#             recurse(child)

# def search_expr(node):
#     returns = []
#     for child in ast.iter_child_nodes(node):
#         if isinstance(child, ast.Expr):
#             return child
#         returns.append(search_expr(child))
#     for ret in returns:
#         if isinstance(ret, ast.Expr):
#             return ret
#     return None 

# formula = '4+5*7/2+45/89-9'
# a = ast.parse(formula)

# expr = search_expr(a)
# if expr is not None:
#     recurse(expr)
# print()    

# 61.
# Define the data

# data = set()
# count = int(input("Enter the number of data points: "))

# for i in range(count):
#     x=float(input("X"+str(i+1)+": "))
#     y=float(input("Y"+str(i+1)+": "))
#     data.add((x, y))
# # Find the average x and y
# avgx = 0.0
# avgy = 0.0
# for i in data:
#     avgx += i[0]/len(data)
#     avgy += i[1]/len(data)

# #Find the sums
# totalxx = 0
# totalxy = 0

# for i in data:
#     totalxx += (i[0]-avgx)**2
#     totalxy += (i[0]-avgx)*(i[1]-avgy)

# #Slope/intercept form
# m = totalxy/totalxx
# b = avgy-m*avgx

# print("Best fit line: ")
# print("y = "+str(m)+"x + "+str(b))

# x = float(input("Enter a value to calculate: "))
# print("y = "+str(m*x+b))


# 62.
# import math


# def calculate_polygons(startx, starty, endx, endy, radius):

#     s1 = (2 * radius) * math.tan(math.pi / 6)

#     p = s1 * 0.5
#     b = s1 * math.cos(math.radians(30))
#     w = b * 2
#     h = 2 * s1

#     startx -= w
#     starty -= h
#     endx += w
#     endy += h

#     orgin = startx
#     orgin = starty

#     xoffset = b
#     yoffset = 3 * p

#     polygons = []
#     row = 1
#     counter = 0

#     while starty < endy:
#         if row % 2 == 0:
#             startx = orgin + xoffset
#         else:
#             startx = orgin
#         while startx < endx:
#             p1x = startx
#             p1y = starty + p
#             p2x = startx + p
#             p2y = starty + (3 * p)
#             p3x = startx + b
#             p3y = starty + h
#             p4x = startx + w
#             p4y = starty + (3 * p)
#             p5x = startx + w
#             p5y = starty + p
#             p6x = startx + b
#             p6y = starty

#             poly = [
#                 (p1x, p1y),
#                 (p2x, p2y),
#                 (p3x, p3y),
#                 (p4x, p4y),
#                 (p5x, p5y),
#                 (p6x, p6y),
#                 (p1x, p1y),
#             ]
#             polygons.append(poly)
#             counter += 1
#             startx += w
#         starty += yoffset
#         row += 1
#     return polygons
# print(calculate_polygons(1, 1, 4, 4, 3))        
# 63.
# import random


# def display_intro():
#     title = "** A Simple Math Quiz **"
#     print("*"*len(title),'\n')
#     print(title,'\n')
#     print("*"*len(title),'\n')

# def display_menu():
#     list_opr= ["1. Addition", "2. Subtraction", "3. Multipication", "4. Integer Division", "5. Exit"]
#     for i in range(len(list_opr)):
#         print(list_opr[i])

# def display_seperator():        
#     print("-"*24)

# def get_user_input():
#     user_input = int(input("Enter your choice: "))
#     while user_input > 5 or user_input <= 0:
#         print("Invalid menu option..")
#         user_input = int(input("please try again..:" ))
#     else:
#         return user_input
   
# def get_user_solution(problem):
#     print("Enter your answer..")
#     print(problem, end="")
#     result = int(input(" = "))
#     return result


# def check_solution(user_solution, solution, count):
#     if user_solution == solution:
#         count += 1
#         print("correct..")
#         return count
#     else:
#         print("Incorrect..")
#         return count
    
# def menu_option(index, count):
#     number_one = random.randrange(1, 21)
#     number_two = random.randrange(1, 21)

#     if index is 1:
#         problem = str(number_one)+ "+" +str(number_two)
#         solution = number_one + number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
    
#     elif index is 2:
#         problem = str(number_one)+ "-" +str(number_two)
#         solution = number_one - number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
    
#     elif index is 3:
#         problem = str(number_one)+ "*" +str(number_two)
#         solution = number_one * number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count
    
#     else:
#         problem = str(number_one)+ "//" +str(number_two)
#         solution = number_one // number_two
#         user_solution = get_user_solution(problem)
#         count = check_solution(user_solution, solution, count)
#         return count

# def display_result(total, correct):

#     if total > 0:
#         result = correct/total
#         percentage = round((result*100), 2)
#     if total == 0:
#         percentage = 0
#     print("You answered", total, "question with", correct, "correct.")
#     print("Your score is", percentage, "% thank you.", sep="")

# def main():
#     display_intro()
#     display_menu()
#     display_seperator()

#     option = get_user_input()
#     total = 0
#     correct = 0

#     while total != 5:
#         total += 1
#         correct = menu_option(option, correct)
#         option = get_user_input()
        
#         print("Exit the Quiz.")
#         display_seperator()
#         display_result(total, correct)
# main()        

# 65.
# import math


# def volume_tetraherdron(num):
#     volume = (num**3 /(6 * math.sqrt(2)))

#     return round(volume, 2)
# print(volume_tetraherdron(10))    

# 65.

# import math


# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)

# def e(EPS):
#     v1 = 2
#     v2 = v1 + float(1.0/fact(2))
#     i =3
#     while math.fabs(v1-v2) >= EPS:
#         v1 = v2

#         v2 += float(1.0/fact(i))
#         i+=1
#     return v2

# print("The mathmatical constants e")

# print(e(0.00000001))

# print(math.e)
    
# from math import cos, radians, sin
# # 66.
# from time import sleep

# #increase 40 to get more wave
# for n in range(1, 40):
#     circle_1 = 50 * (1 + sin(radians(n*10)))
#     circle_2 = 50 * (1 + cos(radians(n*10)))
#     print("#".center(int(circle_1)))
#     print("#".center(int(circle_2)))
#     sleep(0.05)


# 67.
# import sys

# from math import cos, radians

# for i in range(1000):
#     print(' '*int(10*cos(radians(i))+10)+'.')


# 68.
# from math import sqrt

# print('Pythagorean theorem calculator! Calculate your triangle sides.')
# print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
# formula = input('Which side (a, b, c) do you wish to calculate? side> ')

# if formula == 'c':
# 	side_a = int(input('Input the length of side a: '))
# 	side_b = int(input('Input the length of side b: '))

# 	side_c = sqrt(side_a * side_a + side_b * side_b)
	
# 	print('The length of side c is: ' )
# 	print(side_c)

# elif formula == 'a':
#     side_b = int(input('Input the length of side b: '))
#     side_c = int(input('Input the length of side c: '))
    
#     side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
#     print('The length of side a is' )
#     print(side_a)

# elif formula == 'b':
#     side_a = int(input('Input the length of side a: '))
#     side_b = int(input('Input the length of side c: '))
        
#     side_c = sqrt(side_b * side_b - side_a * side_a)
    
#     print('The length of side b is')
#     print(side_c)

# else:
# 	print('Please select a side between a, b, c')
	

# 69.
# import math


# def roundup(a, digits=0):
#     n=10**-digits
#     return round(math.ceil(a/n) * n, digits)

# x = 123.01247
# print("Original Number:", x)
# print(roundup(x, 0))
# print(roundup(x, 1))
# print(roundup(x, 2))
# print(roundup(x, 3))

# 70.
# import math
# import random

# limit = 1000
# acc = 0
# results = []
# exp = 1000

# for i in range(exp):
#     color = 0
#     amount = 10000
#     max_amount = amount
#     bid = 1
#     count = 0 
#     while count < limit and amount > 0:
#         amount = amount - bid
#         next = random.randint(0, 1)
#         if next == color:
#             amount = amount + bid + bid
#             bid = 1
#             #color = 1 if color == 0 else 0
#             if amount > max_amount:
#                 max_amount = amount
#         else:
#             bid = bid + bid
#         count = count + 1
#     acc = acc + max_amount
#     results.append(max_amount)
#     print("Exp {}".format(i))

# avg = acc / exp
# acc = 0
# for i in range(len(results)):
#     acc = acc+math.pow(results[i] - avg, 2)
# std = math.sqrt(acc/exp)
# print("Average max amount earned {} with standard deviation {}".format(avg, std))

# 71.
# def reversed_range(start, stop=None, step=1):
#     if stop is None:
#         return range(start-step, -step, -step)
#     else:
#         new_start = stop - ((stop-start-1) % step + 1)
#         new_end = new_start - (stop-start+step-1) // step * step
#         if (stop - start) % step == 0 and step < 0: new_start -= step
#         return range(new_start, new_end, -step)
    
# print(reversed_range(1, 10, 2))
# print(reversed_range(1, 5, 1))

# 72.
# def frange(x, y, jump=1.0):
#     i=0.0
#     x=float(x)
#     y=float(y)
#     x0 = x
#     epsilon = jump / 2.0
#     yield x
#     while x + epsilon < y:
#         i+=1.0
#         x = x0 + i * jump
#         yield x
# print(list(frange(0.0, 1.0, 0.1)))

# # 73.
# def generateMatrix(n):
#     if n <= 0:
#         return []
    
#     matrix = [row[:] for row in [[0]*n]*n]

#     row_st = 0
#     row_ed = n-1

#     col_st = 0
#     col_ed = n-1
#     current = 1

#     while (True):
#         if current>n*n:
#             break
#         for c in range(col_st, col_ed+1):
#             matrix[row_st][c]=current
#             current += 1
#         row_st += 1

#         for r in range(row_st, row_ed+1):
#             matrix[r][col_ed] = current
#             current+=1
#         col_ed-=1

#         for c in range(col_ed, col_st-1, -1):
#             matrix[row_ed][c] = current
#             current+=1
#         row_ed-=1

#         for r in range(row_ed, row_st-1, -1):
#             matrix[r][col_st] = current
#             current+=1
#         col_st+=1  

#     return matrix
# print(list(generateMatrix(3)))  
   
# 74.
# import random

# from datetime import date

# start_dt = date.today().replace(day=1, month=1).toordinal()
# end_dt = date.today().toordinal()
# random_day = date.fromordinal(random.randint(start_dt, end_dt))
# print(random_day)

# # 75.
# import math


# def distance(a,b):
#     x=float(a[0])-float(b[0])
#     x=x*x
#     y=float(a[1])-float(b[1])
#     y=y*y
#     dist=round(math.sqrt(x+y), 2)
#     return dist

# def minimum(matrix):
#     p=[0,0]
#     mn=1000
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             if (matrix[i][j]>0 and matrix[i][j]<mn):
#                 mn=matrix[i][j]
#                 p[0]=i
#                 p[1]=j
#     return p

# def newpoint(pt):
#     x=float(pt[0][0])+float(pt[1][0])
#     x=x/2
#     y=float(pt[0][1]+float[1][1])
#     y=y/2
#     midpoint=[x,y]
#     return midpoint

# if __name__ == '__main__':
#     n=int(input("Input numbers of points.> "))
#     points=list()
#     outline='['
#     i=0

#     while(i<n):
#         s=input("Input point (eg. 1,1)"+chr(65+i)+"> ")
#         c=s.split(",")
#         points.append(c)
#         i=i+1

#     names={}

#     for i in range(0, len(points)):
#         names[str(points[i])]=chr(65+i)
#     l=0    
#     while(len(points)>1):
#         l=l+1
#         matrix=list()
#         print('Distance matrix no. '+str(l)+': ')
#         for i in range(0, len(points)):
#             m=[]
#             for j in range(0, len(points)):
#                 m.append(0)

#             for j in range(0, len(points)):
#                 m[j]=distance(points[i], points[j])
#             print(str(m))
#             matrix.append(m)

#         m=minimum(matrix)
#         pts=list()
#         p1=points[m[0]]
#         pts.append(p1)
#         points.remove(p1)
#         p2=points[m[1]-1]
#         pts.append(p2) 
#         points.remove(p2)

#         midpoint=newpoint(pts)
#         points.append(midpoint)
#         c1=names.pop(str(p1))
#         c2=names.pop(str(p2))
#         names[str(midpoint)]="["+str(c1)+str(c2)+"]"
#         outline=names[str(midpoint)]   
#     print("Cluster is :", names[str(midpoint)])        


# import math


# def distance(a,b):
#     x=float(a[0])-float(b[0])
#     x=x*x
#     y=float(a[1])-float(b[1])
#     y=y*y
#     dist=round(math.sqrt(x+y),2)
#     return dist

# def minimum(matrix):
#     p=[0,0]
#     mn=1000
#     for i in range(0,len(matrix)):        
#         for j in range(0,len(matrix[i])):            
#             if (matrix[i][j]>0 and matrix[i][j]<mn):
#                 mn=matrix[i][j]
#                 p[0]=i
#                 p[1]=j
#     return p 
            
# def newpoint(pt):
#     x=float(pt[0][0])+float(pt[1][0])
#     x=x/2
#     y=float(pt[0][1])+float(pt[1][1])
#     y=y/2
#     midpoint=[x,y]
#     return midpoint

# if __name__ == '__main__':    
#     n=int(input("Input number of points.> "))
#     points=list()
#     outline='['
#     i=0

#     while(i<n):
#         s=input("Input point (eg. 1,1)"+chr(65+i)+"> ")
#         c=s.split(",")
#         points.append(c)
#         i=i+1

#     names={}

#     for i in range(0,len(points)):
#         names[str(points[i])]=chr(65+i)
#     l=0
#     while(len(points)>1):
#         l=l+1
#         matrix=list()
#         print('Distance matrix no. '+str(l)+': ')
#         for i in range(0,len(points)):
#             m=[]
#             for j in range(0,len(points)):
#                 m.append(0)
#             for j in range(0,len(points)):
#                 m[j]=distance(points[i],points[j])
#             print(str(m))
#             matrix.append(m)
        
#         m=minimum(matrix)
#         pts=list()
#         p1=points[m[0]]
#         pts.append(p1)
#         points.remove(p1)
#         p2=points[m[1]-1]
#         pts.append(p2)
#         points.remove(p2)   
#         midpoint=newpoint(pts)
#         points.append(midpoint)    
#         c1=names.pop(str(p1))
#         c2=names.pop(str(p2))
#         names[str(midpoint)]="["+str(c1)+str(c2)+"]"    
#         outline=names[str(midpoint)]
        
#     print("Cluster is :",names[str(midpoint)])

# 76.
# from math import *


# def eucild_algo(x, y, verbose=True):
#     if x < y: #We want x >= y
#         return eucild_algo(y, x, verbose)
#     print()
#     while y != 0:
#         if verbose:
#             print('%s = %s * %s + %s'%(x, floor(x/y), y, x%y))
#         (x, y) = (y, x % y)

#     if verbose: print('gcd is %s'%x)
#     return x

# eucild_algo(150, 304)
# eucild_algo(1000, 10)
# eucild_algo(150, 9)

# # 77.
# def rgb_to_hsv(r, g, b):
#     r, g, b = r/255.0, g/255.0, b/255.0
#     mx = max(r, g, b)
#     mn = min(r, g, b)
#     df = mx-mn
#     if mx == mn:
#         h=0
#     elif mx==r:
#         h=(60*((g-b)/df)+360) % 360
#     elif mx==g:
#         h=(60*((b-r)/df)+120) % 360
#     elif mx==b:
#         h=(60*((r-g)/df)+240) % 360
#     if mx==0:
#         s = 0
#     else:
#         s = (df/mx)*100
#     v = mx*100
#     return h, s, v
# print(rgb_to_hsv(255, 255, 255))
# print(rgb_to_hsv(0, 215, 0))

# 78.
# def squares(a, b):

#     lists = []
#     for i in range(a, b+1):
#         j=1
#         while j*j <= i:
#             if j*j == i:
#                 lists.append(i)
#             j += 1
#         i+=1
#     return lists
# print(squares(1, 30))            


# 79.
# import math

# x = (5, 6, 7)
# y = (8, 9, 9)

# distance = math.sqrt(sum([(a-b) ** 2 for a, b in zip(x, y)]))
# print("Euclidean distance from x to y:", distance)

# 80.
# for i in range(1, 10):
#     print(i, '-->', format(i, '#04x'))


# 81.
# import random

# choices = list(range(100))
# random.shuffle(choices)
# print(choices.pop())
# while choices:
#     if input('Want another random number?(Y/N )').lower() == 'n':
#         break
#     print(choices.pop())

# 82.
# from fractions import Fraction

# value = 0.214
# z = Fraction(value).limit_denominator()
# print(z)

# 84.
# print(dir())
# import math
# import random

# # print(dir())

# # print(dir(random))
# print(help(list))
