import json
from urllib import request


html = request.urlopen('http://www.weather.com.cn/data/sk/101280101.html ')
data = html.read()
data = json.loads(data)
print(data)
print('%s:%s' % (data['weatherinfo']['city'],data['weatherinfo']['temp']))


