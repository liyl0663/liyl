fib = [0,1]
l = int(input('length:'))
for ind in range(l - 2):
    fib.append(fib[-1] + fib[-2])
print(fib)