import getpass

username = input('please input your name:')
password = getpass.getpass('please input your password:')
print(username,password)
if username == 'bob' and password == 123456:
    print('Login successful')
else:
    print('Login faild')