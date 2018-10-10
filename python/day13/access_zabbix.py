import json
import requests

token = 'cc04043a1efd11a664aa78433e25c2c8'
# url = 'http://192.168.4.10/api_jsonrpc.php'
# header = {'Content-Type':'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
#
# r = requests.post(url,headers=header,data=json.dumps(data))
# print(r.json())
#######################################################################
# url = 'http://192.168.4.10/api_jsonrpc.php'
# header = {'Content-Type':'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1,
#     "auth": None
# }
# r = requests.post(url,headers=header,data=json.dumps(data))
# print(r.json()['result'])

#########################################################################
# url = 'http://192.168.4.10/api_jsonrpc.php'
# header = {'Content-Type':'application/json-rpc'}
# data = {
# "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Zabbix server",
#                 "Linux server"
#             ]
#         }
#     },
#     "auth": "cc04043a1efd11a664aa78433e25c2c8",
#     "id": 1
# }
# r = requests.post(url,headers=header,data=json.dumps(data))
# alist = r.json()['result']
# print(alist[0])
# for key in alist[0]:
#     print(key,":",alist[0][key])
#########################################################################
# url = 'http://192.168.4.10/api_jsonrpc.php'
# header = {'Content-Type':'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.create",
#     "params": {
#         "host": "Zabbix server1",
#         "interfaces": [
#             {
#                 "type": 1,
#                 "main": 1,
#                 "useip": 1,
#                 "ip": "192.168.4.12",
#                 "dns": "",
#                 "port": "10050"
#             }
#         ],
#         "groups": [
#             {
#                 "groupid": "1"
#             }
#         ],
#         # "templates": [
#         #     {
#         #         "templateid": "20045"
#         #     }
#         # ],
#         "inventory_mode": 0,
#         "inventory": {
#             "macaddress_a": "01234",
#             "macaddress_b": "56768"
#         }
#     },
#     "auth": "cc04043a1efd11a664aa78433e25c2c8",
#     "id": 1
# }
# r = requests.post(url,headers=header,data=json.dumps(data))
# print(r.json())
########################################################################
url = 'http://192.168.4.10/api_jsonrpc.php'
header = {'Content-Type':'application/json-rpc'}
data = {
     "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                "Zabbix servers"
            ]
        }
    },
    "auth": token,
    "id": 1
}
r = requests.post(url,headers=header,data=json.dumps(data))
print(r.json()['result'])