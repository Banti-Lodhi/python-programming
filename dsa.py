# import time

# start = time.time()

# # for i in range(1, 101):
# #     print(i)
# i=1
# while i<101:
#     print(i)
#     i+=1
# print(time.time()-start)
def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print('Average is:', sum/len(numbers))
average(5, 8, 9)    