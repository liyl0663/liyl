# try:
#     n = int(input('number:'))
#     result = 100/n
#     print(result)
# except ValueError:
#     print('Invalid number')
# except ZeroDivisionError:
#     print('Invalid number')
# except KeyboardInterrupt:
#     print("\nctrl+c")
# except EOFError:
#     print("\nctrl+d")
try:
    n = int(input('number:'))
    result = 100/n
    #print(result)
except (ValueError,ZeroDivisionError):
    print('无效的数字')
except (KeyboardInterrupt,EOFError):
    print('\n用户中断')
else:
    print(result)
finally:
    print('Done')