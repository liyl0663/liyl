import time
import os

print('starting...')
pid = os.fork()
print(pid)
if pid:
    print('in parent.')
    time.sleep(60)
else:
    print('in child')
    time.sleep(15)
##########################################
# print('starting...')
# pid = os.fork()
# print(pid)
# if pid:
#     print('in parent.')
#     print(os.waitpid(-1,0))
#     print('go on...')
# else:
#     print('in child')
#     time.sleep(5)
###########################################
# print('starting...')
# pid = os.fork()
# print(pid)
# if pid:
#     print('in parent.')
#     print(os.waitpid(-1,1))
#     print('go on...')
# else:
#     print('in child')
#     time.sleep(10)
#     print('child go on...')