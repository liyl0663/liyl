##方法一
alist = [1,2,3,3,4,2,4,5,6,1]
blist = []
for num in alist:
    if num not in blist:
        blist.append(num)
print(blist)

##方法二
clist = [1,2,3,3,4,2,4,5,6,1]
dlist = list(set(clist))
print(dlist)

