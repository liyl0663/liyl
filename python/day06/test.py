adict = {'name':'zs','age':23}

for key in adict:
     print('%s:%s' % (key,adict[key]))
print('%(name)s:%(age)s' % adict)

adict['name'] = 'zhangsan'
print(adict)
adict['email'] = 'zhangsan@tedu.com'
print(adict)