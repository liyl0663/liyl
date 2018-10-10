from random import choice,randint
import string
strs = string.ascii_letters + string.digits
sum = ''
for i in range(5):
    num = choice(strs)
    sum += num
print(sum)

a = choice([randint(1,100) for i in range(10)])
print(a)

str = '你好'
print(str.encode('utf8'))
b = str.encode('utf8')
print(b.decode('utf8'))