import requests

url1 = 'http://www.baidu.com'

r = requests.get(url1)
print(r.text)
print(r.encoding)
r.encoding = 'utf8'
print(r.text)
data = r.content
print(type(data))
print('#' * 100)

url2 = 'http://www.weather.com.cn/data/sk/101010100.html'
r1 = requests.get(url2)
r1.encoding = 'utf8'
print(r1.json())

url3 = 'https://www.python.org/static/img/python-logo.png'
r2 = requests.get(url3)
with open('/tmp/py.png','wb') as fobj:
    fobj.write(r2.content)

url4 = 'http://www.baidu.com/s'
r3 = requests.get(url4,params={'wd':'Python'})
r3.encoding = 'utf8'
print(r3.text)
with open('/tmp/py.html','wb') as fobj:
    fobj.write(r3.content)

url5 = 'http://192.168.4.10'
r4 = requests.get(url5)
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
r4 = requests.get(url5,headers=header)
print(r4.status_code)
print(requests.codes.not_found)
print(requests.codes.forbidden)
print(requests.codes.ok)