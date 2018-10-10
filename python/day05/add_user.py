import string
import random
import os
def adduser():
    uesr = input("请输入用户名:")
    return uesr

def addpass():
    str = string.ascii_letters + string.digits
    password = ''
    for i in range(8):
        ch = random.choice(str)
        password += ch
    return password

def wfile(content):
    content = [user,password]
    file = '/tmp/user.txt'
    with open(file,'a') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    user = adduser()
    password = addpass()
    content = [user,password]
    # content = ['%s\n' % line for line in content]
    wfile(content)