import subprocess
import os
import threading
import time
def ping(host):
    rc = subprocess.call(
        'ping -c2 %s > /dev/null' % host,
        shell=True
    )
    if rc == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)


if __name__ == '__main__':
    ips = ['176.121.207.%s' % i for i in range(1,255)]
    for ip in ips:
        #ping(ip)
        t = threading.Thread(target=ping,args=(ip,))
        t.start()
        # pid = os.fork()
        # if not pid:
        #     ping(ip)
        #     exit(0)
