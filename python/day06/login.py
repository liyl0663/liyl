import getpass
userdb = {}
def register():
    username = input('username:')
    if username in userdb:
        print('%s already exits.' % username)
    else:
        password = input('password:')
        userdb[username] = password

def login():
    username = input('username:')
    password = getpass.getpass('password:')
    if userdb.get(username) != password:
        print('faild login!')
    else:
        print('login sucessful!')
        exit()

def show_menu():
    cmds = {'0':register, '1':login}
    prompt = """(0) register
(1) login
(2) quit
Please input your choice(0/1/2):"""
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print("Invalid choice,Try again.")
        if choice == '2':
            break
        cmds[choice]()
if __name__ == '__main__':
    show_menu()