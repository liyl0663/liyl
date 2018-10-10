import shutil

f1 = open('/etc/hosts','rb')
f2 = open('/tmp/zhuji','wb')
shutil.copyfileobj(f1,f2)
f1.close()
f2.close()


shutil.copyfile('/etc/hosts','/tmp/zj')
#shutil.copyfile('/etc/hosts','/tmp/')  #错误

shutil.copy('/etc/hosts','/tmp')
shutil.copy2('/etc/passwd','/tmp/')

#shutil.move('/tmp/hosts2','/var/tmp/')

#shutil.copytree('/etc/security','/tmp/anquan')
shutil.rmtree('/tmp/anquan')