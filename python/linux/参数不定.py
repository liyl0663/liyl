def demo(args_f,*args_v):
    print(args_f)
    for x in args_v:
        print(x)
def demo2(**agrs_v):
    for k,v in agrs_v.items():
        print(k,v)

if __name__ == '__main__':
    demo('a','b','d','e')
    demo2(name='tom',age=12)
