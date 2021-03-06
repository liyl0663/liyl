import sys
import re

def setip(fname,ip_addr,if_ind):
    content = """TYPE=Ethernet
BOOTPROTO=none
NAME=eth%s
DEVICE=eth%s
ONBOOT=yes
IPADDR=%s
PREFIX=24
""" % (if_ind,if_ind,ip_addr)
    with open(fname,'w') as fobj:
        fobj.write(content)
def check_ip(ip_addr): #判断IP地址是不是x.x.x.x格式
    res = re.match(r'(\d{1,3}\.){3}\d{1,3}$',ip_addr)
    if not res:
        return False
    return True
def show_menu():
    prompt = """configure IP Address:
(0)eth0
(1)eth1
(2)eth2
(3)eth3
Your choice(0/1/2/3):"""
    try:
        if_ind = input(prompt).strip()[0]
    except:
        print('Invalid input.')
        sys.exit(1)
    if if_ind not in '0123':
        print('Wrong selection.Use 0/1/2/3')
        sys.exit(2)
    fname = '/etc/sysconfig/network-scripts/ifcfg-eth%s' % if_ind
    ip_addr = input('ip address:').strip()
    result = check_ip(ip_addr)
    if not result:
        print('Invalid ip address')
        sys.exit(3)
    setip(fname,ip_addr,if_ind)
    print('\033[32;1mConfigure ip address done. Please execute "systemctl restart NetworkManager"\033[0m')
if __name__ == '__main__':
    show_menu()