print('hello world')
print('hello' + 'world')
print('hello', 'world')
print('hello', 'world', 'python', sep='****') #指定分隔符*
#print默认在打印结束后加上一个回车,可以使用end=重置结束符
print('hello world', end='###')

n = input('number: ')
print(n)
#a = n + 10
a = int(n) + 10
print(a)
b = n + str(10)
print(b)