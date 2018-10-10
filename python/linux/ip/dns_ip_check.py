import dns.resolver
import os
import http.client
import re

iplist = []
appdomain = 'www.baidu.com'

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')
    except Exception as e:
        print('dns resolver error:'+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
                iplist.append(j)
    return True

if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist) > 0:
        #patt = re.compile('(\d+\.){3}\d+')
        #m = patt.search(iplist)
        for ip in iplist:
            print(ip)