# astr = 'hello'
# alist = ['bob','tom']
# atuple = (100,200,300)
# adict = {'name':'zhangsan','age':25}
#
# for ch in astr:
#     print(ch,end='#')
#
# for name in alist:
#     print(name)
#
# for i in atuple:
#     print(i)
#
# for key in adict:
#     print('%s:%s' %(key,adict[key]))
##########################################
# for i in range(10):
#     print(i)
# print('#' * 20)
#
# for i in range(6,11):
#     print(i)
# print('#' * 20)
#
# for i in range(2,11,2):
#     print(i)
# print('#' * 20)
#
# for i in range(1,10,2):
#     print(i)
# print("#" * 20)
#
# for i in range(10,0,-1):
#     print(i)
#################################
# alist = ['tom','bob','harry','lucy','lili','petter']
# for ind in range(len(alist)):
#     print('%s:%s' % (ind,alist[ind]))
#################################
print([3+2])
print([3+2 for i in range(5)])
print([3+i for i in range(5)])
print([3+i for i in range(1,10)])
print([3+i for i in range(1,10) if i % 2 == 0])

print(['192.168.4.%s'% i for i in range(1,255)])