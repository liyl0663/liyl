import random

def fun_sort(alist):
    if len(alist) < 2:
        return alist
    middle = alist[0]
    larger = []
    smaller = []
    for i in alist[1:]:
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)
    return fun_sort(smaller) + [middle] + fun_sort(larger)

if __name__ == '__main__':
    alist = [random.randint(1,100) for i in range(10)]
    #print(alist)
    print(fun_sort(alist))