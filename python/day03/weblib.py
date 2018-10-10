import webbrowser
import os
import time
count = 0
while count < 10:
    count +=1
    webbrowser.open_new_tab('http://www.baidu.com')
    os.system('killall firefox')
    print(count)
print('ok')
