# f = open('/tmp/abc.txt')
# data = f.read()
# f.close()
# print(data)
#################################
# f1 = open('/tmp/abc.txt')
# data1 = f1.read()
# print('data1:',data1)
# data1 = f1.read()
# print('data1:',data1)
# f1.close()
#################################
# f = open('/tmp/passwd')
# data = f.read(2242)
# count=0
# for i in data:
#     #print(i)
#     count+=1
# print(count)
# print(data)
# f.close()
# print('#'*20)
#
# #####################################
# f = open('/tmp/passwd')
# print(f.readline())
# f.close()
# ####################################
# f = open('/tmp/passwd')
# print(f.readlines())
# f.close()
####################################
# f = open('/tmp/passwd')
# for li in f:
#     print(li,end='')
# print(f)
#####################################
# f = open('/tmp/list','rb')
# print(f.read(10))
# f.close()
######################################
# f = open('/tmp/abc.txt','w')
# f.write('hello world\n')
# f.flush()
# f.writelines(['2nd line.\n','3rd line.\n'])
# f.close()
# f = open('/tmp/abc.txt')
# data = f.read()
# print(data)
#######################################
# with open('/tmp/abc.txt','w') as f:
#     f.write('my test.\n')
#     f.write('my ttoo.\n')
#######################################
# f = open('/tmp/passwd','rb')
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.read(5))
# print(f.seek(3,0))
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# print(f.seek(10,1))
# print(f.read(5))
# print(f.seek(-6,2))
# print(f.read())
# f.close()
#######################################
# import sys
# b = sys.stdin.readline()
# print(b)
# sys.stdout.write('hello world!\n')
# sys.stderr.write('hello world!\n')
#######################################

