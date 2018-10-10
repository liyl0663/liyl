import psutil

#free -m | grep Mem |awk '{print $2}'   //total
#free -m | grep Mem |awk '{print $4}'   //free

###################内存#############################
mem = psutil.virtual_memory()
print('total:%s' % (mem.total))
print('used:%s' % (mem.used))
print('free:%s' % (mem.free))
print('available:%s' % (mem.available))
####################cup###########################
print(psutil.cpu_times().user)
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
####################磁盘############################
disk = psutil.disk_partitions()
print(disk)
print(psutil.disk_usage('/'))  #根分区信息
print(psutil.disk_io_counters(perdisk=True))
#####################网络###########################
list = psutil.net_io_counters(pernic=True)
print(list['enp1s0'])

######################登陆用户##########################
print(psutil.users())

######################进程#############################
print(psutil.pids())
p = psutil.Process(20)
print(p.name())
print(p.exe())
print(p.cwd())