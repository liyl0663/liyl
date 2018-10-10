# def add(x,y):
#     return {'num':x+y}
# if __name__ == '__main__':
#     print(add(10,20))
#     a = lambda x,y:[x+y,x-y]
#     print(a(20,30))

from random import randint

def mydiv(x):
    return x % 2

def fun1(x):
    return x * 2 +1


if __name__ == '__main__':
    alist = [randint(1,100) for i in range(10)]
    print(alist)
    print(list(filter(mydiv,alist)))
    print(list(filter(lambda x:x % 2,alist)))
    print(list(map(fun1,alist)))
    print(list(map(lambda x:x * 2 +1,alist)))
