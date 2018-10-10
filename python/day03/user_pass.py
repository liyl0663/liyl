import getpass

username = input('username:')
password = getpass.getpass('password:')

if username == 'bob' and password == '123':
    print('Login sucessfull!')
else:
    print('Login incorrect!')
