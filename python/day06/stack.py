stack = []
def push_it():
    item = input('item to push:')
    stack.append(item)

def pop_it():
    stack.pop()


def view_it():
    print(stack)

def show_menu():
    cmds = {'0':push_it, '1':pop_it, '2':view_it}
    prompt = """(0)push it
(1)pop it
(2)view it
(3)quit
Please input your choice(0/1/2/3):"""
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid choice,Try again')
            continue
        if choice == '3':
            break
        # if choice == 1:
        #     push_it()
        # elif choice == 2:
        #     pop_it()
        # else:
        #     view_it()
        cmds[choice]()
if __name__ == '__main__':
    show_menu()