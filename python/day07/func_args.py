def myfunc(*args):
    print(args)

def myfunc2(**kye):
    print(kye)

if __name__ == '__main__':
    myfunc()
    myfunc('bob')
    myfunc('tom',123)
    myfunc2(name='zhangsan')
    myfunc2(name='zhangsan',age=20,sex=1)