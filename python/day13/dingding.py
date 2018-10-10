import json
import os
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['13123110069']  # 特殊提醒要查看的人,就是@某人一下
    url = 'https://oapi.dingtalk.com/robot/send?access_token=ea124c5a10e4cdfefc39bc16a4109916af5bba7348111e271ae2e1be805c5f0d'
    print(send_msg(url, reminders, msg))