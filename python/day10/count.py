import re
import sys

def count_patt(fname,patt):
    cpatt = re.compile(patt)
    result = {}

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                result[key] = result.get(key,0) + 1

    return result
if __name__ == '__main__':
    fname = sys.argv[1]
    ip = '^(\d+\.){3}\d+'
    print(count_patt(fname,ip))
    br = 'Firefox|MSIE|Chrome'
    print(count_patt(fname,br))