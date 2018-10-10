from random import randint

def qsort(num_list):
    if len(num_list) < 2:
        return num_list

    middle = num_list[0]
    smaller = []
    larger = []
    for i in num_list[1:]:
        if i <= middle:
            smaller.append(i)
            print(smaller)
        else:
            larger.append(i)
            print(larger)
    return qsort(smaller) + [middle] + qsort(larger)
if __name__ == '__main__':
    alist = [randint(1,100) for i in range(10)]
    print(alist)
    print(qsort(alist))