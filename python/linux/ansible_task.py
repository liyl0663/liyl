#!/usr/bin/env python3
#coding:utf8

"""
模块功能：
namedtuple用于创建自定义的元组数据类型
DataLoader用于分析yaml/json/ini文件
VariableManager用于ansible的变量
InventoryManager用于管理主机清单
Play用于创建Playbook对象，还能自动创建任务对象
TaskQueueManager用于管理任务队列
CallbackBase不是必须的，用于自定义输出
ansible.constants定义ansible使用的一些常量
"""

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
#from ansible.plugins.callback import CallbackBase
import ansible.constants as C
import sys

def AnsibleTask(forks_num,host_path,host_list,module_name,module_args):
    # class ResultCallback(CallbackBase):
    #     def v2_runner_on_ok(self, result, **kwargs):
    #         host = result._host
    #         print(json.dumps({host.name: result._result}, indent=4))

    ###############################################################################
    # connection是连接的类型：分别有local(本地执行任务)、ssh(远程执行任务)、smart(智能判断)
    # module_path，除默认的模块路径以外的、自定义的模块目录
    # forks，指定创建多少子进程
    # become，使用become执行操作，不明确提示密码
    # become_method，切换用户的方法，如su、sudo
    # become_user，切换成哪个用户
    # check，不真正执行命令，只是检查是否会有改变
    # diff，如果小文件有改动，显示改动部分
    ################################################################################
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=forks_num, become=None, become_method=None, become_user=None, check=False, diff=False)

    loader = DataLoader()
    #定义各种密码，没有密码则使用空字典
    passwords = dict()

    #results_callback = ResultCallback()
    # 定义主机清单文件，sources可以使用主机配置文件路径，也可以使用逗号隔开的所有主机
    inventory = InventoryManager(loader=loader, sources=host_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source =  dict(
            name = "Ansible Play",  #Play的名字
            hosts = host_list,    #在哪些主机上执行命令
            gather_facts = 'no',    #不收集主机信息
            tasks = [
                dict(action=dict(module=module_name, args=module_args), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )

    #实例化Play
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    #实例化任队列管理器
    tqm = None
    try:
        tqm = TaskQueueManager(
                  inventory=inventory,
                  variable_manager=variable_manager,
                  loader=loader,
                  options=options,
                  passwords=passwords,
                  #stdout_callback=results_callback,
              )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()    #清理任务
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)   #删除临时目录
if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('Usage:%s forks_num host_path host_list module_name module_args' % sys.argv[0])
        sys.exit(1)
    forks_num =  int(sys.argv[1]) #子进程数量
    host_path = sys.argv[2]       #主机配置文件路径
    host_list = sys.argv[3]       #在哪些主机上执行命令
    module_name = sys.argv[4]     #模块名称
    module_args = sys.argv[5]     #模块参数
    # forks_num = 4
    # host_path = '/root/myansi/hosts'
    # host_list = 'web'
    # module_name = 'shell'
    # module_args = 'tail -1 /etc/passwd'
    try:
        AnsibleTask(forks_num,host_path,host_list,module_name,module_args)
    except:
        print("invalid parameter")
        sys.exit(2)
