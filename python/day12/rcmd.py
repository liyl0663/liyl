import paramiko
import sys
import getpass
from threading import Thread
import os

def rcmd(host,passwd,command,user='root',port='22'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=user,password=passwd,port=port)
    stdin,stdout,stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('%s:[OUT]\n%s' % (host,out.decode()))
    if err:
        print('%s:[ERROR]\n%s' % (host,err.decode()))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage:%s ipfile "command"' % sys.argv[0])
        sys.exit(1)
    ipfile = sys.argv[1]
    command =sys.argv[2]
    passwd = getpass.getpass()
    if not os.path.isfile(ipfile):
        print('Files not found:',ipfile)
        sys.exit(2)
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = Thread(target=rcmd,args=(ip,passwd,command))
            t.start()