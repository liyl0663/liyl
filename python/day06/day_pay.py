import time
import pickle
money_list={'money':10000}

# def rw_money():
#     prompt = """(0)开销:
# (1)收入:
# (2)返回:
# Please input your choice(0/1/2)"""
#     choice = input(prompt).strip()[0]
#     if choice not in '012':
#         print("Invalid choice")
#     if choice == '2':
#         menu()
def money_in():
    try:
        money = int(input('number:'))
    except (ValueError,ZeroDivisionError):
        print("无效的数字")
    else:
        money_list['money'] += money
        with open('/tmp/money.data', 'wb') as fobj:
            pickle.dump(money_list,fobj)
        print(money_list)


def money_out():
    print('out')

def  add_xinxi():
    print('xinix')

def view():
    print('view')

def show_menu():
    prompt="""(0)收入
(1)开销
(2)记账
(3)查看
(4)退出
请输入你的选择(0/1/2/3/4):"""
    cmds = {'0':money_in, '1':money_out, '2':add_xinxi, '3':view}
    while True:
        choice = input(prompt).strip()[0]

        if choice not in '01234':
            print('错误的选择')
            continue
        if choice == '4':
            break

        cmds[choice]()


if __name__ == '__main__':
    show_menu()
