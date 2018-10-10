import re
from collections import Counter

def count_patt(fname,patt):
    #patt_dict = {}
    result = Counter()
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                result.update([key])
                #patt_dict[key] = patt_dict.get(key,0) + 1
    #return patt_dict
    return result


if __name__ == '__main__':
    log_file = 'access_log'
    ip = '^(\d+\.){3}\d+'
    print(count_patt(log_file,ip))
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(log_file,br))