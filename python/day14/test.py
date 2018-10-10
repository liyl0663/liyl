import requests
import re

url = 'http://192.168.4.12/deploy/packages/mp-1.0.tar.gz'
r = requests.get(url)
print(r.status_code)
