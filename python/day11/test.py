print(sum(range(1,101)))

a = 5
def fun():
    global a
    a = 4
    print(a)

fun()
print(a)

dict = {'name':'tom', 'age':22, 'email':211}
dict2 = {'name':'ls','dd':22222}
# print(dict)
# del dict['email']
dict.update(dict2)
print(dict)

# print(dict)