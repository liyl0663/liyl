import random
import os
computer = random.randint(1,100)
count = 0
while count < 1:
    answer = int(input("Please enter a num(0-100):"))
    if answer > computer:
        print("too big!")
    elif answer < computer:
        print("too small!")
    else:
        print("you win!")
        count = 1
print('the number:',computer)