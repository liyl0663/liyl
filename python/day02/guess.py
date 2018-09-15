import random

#随机生成数字1-10
number = random.randint(1,10)
print(number)

answer = int(input('guess the number:'))
if answer > number:
    print('too big!')
elif answer < number:
    print('too small!')
else:
    print('you guess!')