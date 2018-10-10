for i in range(1,10):
    for j in range(1,i+1):
        sum = i * j
        print('%sX%s=%s'% (j,i,sum),end=' ')
    print()
