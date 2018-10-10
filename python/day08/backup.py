import os

#print(list(os.walk('/etc/security')))
for path,folders,files in os.walk('/etc/security'):
    for each_file in files:
        print(os.path.join(path,each_file))