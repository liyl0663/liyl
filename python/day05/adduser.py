import sys
import subprocess
import random
import string

def getpassword():
    str = string.ascii_letters + string.digits
    password = ''
    for i in range(8):
        ch = random.choice(str)
        password += ch
    return password

def adduser(username,password,file):
    info = """ user information:
username: %s
password: %s
""" % (username,password)
    subprocess.call('useradd %s' % username,shell=True)
    subprocess.call(
        'echo %s| passwd --stdin %s' % (password,username),
        shell=True
    )
    with open(file,'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    file = '/tmp/userinfo.txt'
    username = sys.argv[1]
    password = getpassword()
    adduser(username,password,file)