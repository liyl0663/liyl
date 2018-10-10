import re
from collections import Counter

class CountPatt:
    def __init__(self,patt):
        self.cpatt = re.compile(patt)

    def count_patt(self,fname):
        result = Counter()
        with open(fname) as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    result.update([m.group()])
        return result
if __name__ == '__main__':
    ipcount = CountPatt('(\d+\.){3}\d+')
    a = ipcount.count_patt('access_log')
    print(a)