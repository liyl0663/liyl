import requests
import json
url = 'http://192.168.4.10/api_jsonrpc.php'
header = {'Content-Type':'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1,
    "auth": None
}
r = requests.post(url,headers=header,data=json.dumps(data))
token = r.json()['result']

#获取特定主机信息
print('Host list:')
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "host": [
        #         "Zabbix server",
        #     ]
        # }
    },
    "auth": token,
    "id": 1
}
r = requests.post(url, headers=header, data=json.dumps(data))
alist = r.json()['result']
for i in alist:
    print(i)

# 获取主机组信息
print('#' * 60)
print('hostgroup list:')
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "name": [
        #         "Linux servers"    # 2
        #     ]
        # }
    },
    "auth": token,
    "id": 1
}
r = requests.post(url, headers=header, data=json.dumps(data))
alist = r.json()['result']
for i in alist:
    #print(i)
    print(i['name'],":",i['groupid'])

# 获取模板信息
print('#' * 60)
print('Template list:')
data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "host": [
        #         "Template OS Linux",   # 10001
        #     ]
        # }
    },
    "auth": token,
    "id": 1
}
r = requests.post(url, headers=header, data=json.dumps(data))
for i in r.json()['result']:
    print(i['host'],":",i['templateid'])