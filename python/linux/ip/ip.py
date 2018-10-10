from IPy import IP
# ip = IP('192.168.0.0/16')
# print(ip.len())
# for x in ip:
#     print(x)

print('192.168.1.100' in IP('192.168.1.0/24'))
print(IP('192.168.1.0/24') in IP('192.168.0.0/16'))
