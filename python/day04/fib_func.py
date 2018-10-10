def gen_fib(l):
    fib = [0,1]
    for ind in range(l - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

a = gen_fib(10)
print(a)

n = int(input('length:'))
b = gen_fib(n)
print(b)
c = print([i * 2 for i in b])