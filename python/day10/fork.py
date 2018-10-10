import os
print('starting')
pid = os.fork()
print(pid)
if pid:
    print('hello from parent')
else:
    print('hello from child')

print('hello from both')