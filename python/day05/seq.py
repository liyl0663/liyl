from random import randint
#alist = [randint(1,100) for i in range(10)]
alist = ['zhangsan','list','wangwu','tom']
for ind in range(len(alist)):
    print('%s %s' % (ind,alist[ind]))

print(list(enumerate(alist)))

for item in enumerate(alist):
    print('%s %s' % (item[0],item[1]))
print('#' * 20)
for ind,val in enumerate(alist):
    print('%s %s' % (ind,val))

print(list(reversed(alist)))
for name in reversed(alist):
    print('%s %s' % (name,name))

print(sorted(alist[0]))
for i in sorted(alist):
    print(i)
