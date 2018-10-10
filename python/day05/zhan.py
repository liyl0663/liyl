stack = []
def push_it():
    item = input('item to push:')
    stack.append(item)

def pop_it():
    if stack:
        print('\033[33mfrom stack poped %s\033[0m' % stack.pop())

def view_it():
    print(stack)

def show_menu():
    cmd = {'0':push_it,'1':pop_it,'2':view_it}
    prompt = """(0)push it
(1)pop it
(2)view it
(3)exit
please input your choice(0/1/2/3):"""
    while True:
        choice = input(prompt).strip()
        if choice not in '0123':
            print('invalid input,try again')
            continue
        if choice == '3':
            break
        cmd[choice]()

if __name__ == '__main__':
    show_menu()
