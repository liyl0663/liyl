# def mygen():
#     yield 'hello world'
#     a = 10 + 20
#     yield a
#     yield {'name':'tom','age':22}
#     yield [100,200]
#
# for i in mygen():
#     print(i)
# def gen_block(fobj):
#     lines = []
#     counter = 0
#     for line in fobj:
#         lines.append(line)
#         if counter == 10:
#             yield lines
#             lines = []
#             counter = 0
#     if lines:
#         yield lines
# if __name__ == '__main__':
#     fobj = open('/tmp/mima')
#     for block in gen_block(fobj):
#         print(block)
#     fobj.close()

# def foo():
#     def bar():
#         print('yes')
#     return bar
# def bar():
#     print('ss')
# if __name__ == '__main__':
#     a = foo()
#     a()
#     bar()

def counter(start=0):
    count = start
    def incr():
        nonlocal count
        count += 1
        return  count
    return incr

if __name__ == '__main__':
    a = counter()
    print(a())
    b = counter(10)
    print(b())
    b = counter()
    print(b())
    print(b())