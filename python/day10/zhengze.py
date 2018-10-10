import re
m = re.match('f..','food')
print(m)
print(m.group())
m = re.search('f..','seafood')
print(m.group())
m = re.findall('f..','seafood is food')
print(m)
m = re.finditer('f..','seafood is food')
print(list(m))
for i in m:
    print(i.group())

print(re.sub('f..','abc','fish is food'))
print(re.split('\.|-','hello-world.tat=gz'))

patt = re.compile('f..')
m = patt.search('seafood')
print(m.group())
