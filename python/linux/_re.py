import re

if __name__ == '__main__':

    str = '<div class="nam">中国</div>'
    res = re.findall('<div class=".*">(.*)?</div>',str)
    print(res)