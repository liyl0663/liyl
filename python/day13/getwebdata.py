from urllib import request
import os
import re

def get_webdata(url,fname):
    html = request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)


if __name__ == '__main__':
    if not os.path.exists('/tmp/163'):
        os.mkdir('/tmp/163')
    get_webdata('http://www.163.com', '/tmp/163/163.html')
    img_urllist = []
    img_patt = r'(http|https)://[\w/\.-]+\.(jpg|jpeg|png)'
    with open('/tmp/163/163.html','rb') as fobj:
        for line in fobj:
            line = line.decode('GBK')
            m = re.search(img_patt, line)
            if m:
                img_urllist.append(m.group())

    for img_url in img_urllist:
        fname = img_url.split('/')[-1]
        fname = os.path.join('/tmp/163',fname)
        try:
            get_webdata(img_url,fname)
        except:
            pass