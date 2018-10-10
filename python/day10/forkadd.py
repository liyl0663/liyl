import time
import os

def add():
    result = 0
    for i in range(1,500000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(4):
        pid = os.fork()
        if not pid:
            add()
            exit()
    for i in range(4):
        os.waitpid(-1,0)

    end = time.time()
    print(end - start)
