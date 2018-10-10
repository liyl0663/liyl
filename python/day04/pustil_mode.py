import psutil
mem = psutil.virtual_memory()
print(mem.total,mem.used,mem.free)

cpu =psutil.cpu_times()
print(cpu)
print(psutil.cpu_times().user)
print(psutil.cpu_count(logical=False))
