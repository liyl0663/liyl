def fun_info(name,age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    user = ['bob',22]
    user2 = {'name':'tot1', 'age':23}
    fun_info(*user)
    fun_info(**user2)