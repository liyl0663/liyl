import random
st = "石头"
jd = "剪刀"
bu = "布"
computer = random.choice([st,jd,bu])
print(computer)
person = input("请你出拳：")
print("you choice: %s computer choice: %s" % (person,computer))
if person == st:
    if computer == st:
        print('平局')
    elif computer == jd:
        print('you win!!')
    else:
        print('you lose!!')
elif person == jd:
    if computer == st:
        print('you lose!!')
    elif computer == jd:
        print('平局')
    else:
        print('you win!!')
else:
    if computer == st:
        print('you win!!')
    elif computer == jd:
        print('you lose!!')
    else:
        print('平局')

