import random
import string

def guess_num():
    result = random.randint(1,100)
    count = 0
    while True:
        if count == 10:
            print('Game Over!The answer is %s' % result)
            break
        try:
            answer = int(input('Please iuput a number:'))
        except:
            print('Invalid input.')
            count += 1
        else:
            if answer > result:
                print('Too big.Try again!')
                count += 1
            elif answer < result:
                print('Too small.Try again!')
                count += 1
            else:
                print('You win!')

def games():
    all_choice = ['石头','剪刀','布']
    win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
    prompt = """(0)石头
(1)剪刀
(2)布
请选择(0/1/2):"""
    c_count = 0
    p_count = 0
    while True:
        if c_count ==2 or p_count ==2:
            break
        else:
            computer = random.choice(all_choice)
            ind = int(input(prompt))
            player = all_choice[ind]
            print('your choices is %s,computer is %s' % (player,computer))
            if player == computer:
                print('\033[32;1m平局\033[0m')
            elif [player,computer] in win_list:
                print('\033[31;1mYou WIN!!!\033[0m')
                p_count += 1
            else:
                print('\033[31;1mYou LOSE!!!\033[0m')
                c_count += 1

def feibonaqi():
    fib = [0,1]
    number = int(input('Please input the number(0-20):'))
    for i in range(number):
        fib.append(fib[-1] + fib[-2])
    print(fib)

def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s x %s = %s ' % (i,j,i*j),end='')
        print()

def gen_password():
    n = int(input("Please enter a number:"))
    str = string.ascii_letters + string.digits
    result = ''
    for i in range(n):
        ch = random.choice(str)
        result += ch
    return result



if __name__ == '__main__':
    prompt = """(0)guess num
(1)games
(2)斐波那契数列
(3)9*9
(n)quit
Please input your choice:"""
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123n':
            print('Invalid choice!')
        if choice == 'n':
            break
        if choice == '0':
            guess_num()
        if choice == '1':
            games()
        if choice == '2':
            feibonaqi()
        if choice == '3':
            jiujiu()

