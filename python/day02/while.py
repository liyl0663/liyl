# result = 0
# counter = 1
#
# while counter <= 100:
#     result += counter
#     counter += 1
#
# print(result)
#############################################################################
# import random
#
# #随机生成数字1-10
# number = random.randint(1,100)
# #running = True
# count = 0
#
# while count < 3:
#     answer = int(input('guess the number:'))
#     if answer > number:
#         print('\033[33m猜大了！\033[0m')
#     elif answer < number:
#         print('\033[34m猜小了！\033[0m')
#     else:
#         print('\033[35m猜对了！\033[0m')
#     count += 1
#############################################################################
# while True:
#     yn = input('continue(y/n)?')
#     if yn in ['n','N']:
#         break
#     print('working......')
#######################################################################
# count = 0
# result = 0
# while count < 100:
#     count += 1
#     if count % 2: ##counter % 2 的结果不是0就是1，1为True,0为False
#         continue
#     result += count
# print(result)
##########################################################################

import random
number = random.randint(1,10)
counter = 0

while counter < 5:
    answer = int(input('guest the number:'))
    if answer > number:
        print('too big')
    elif answer < number:
        print('too small')
    else:
        print('yes')
        break
else:
    print('The number:',number)