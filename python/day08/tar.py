import os
import tarfile

# os.chdir('/etc/')
# tar = tarfile.open('/tmp/mytest.tar.gz','w:gz')
# tar.add('security')
# tar.add('hosts')
# tar.close()

os.mkdir('/tmp/mydemo')
os.chdir('/tmp/mydemo')
tar = tarfile.open('/tmp/mytest.tar.gz','r:gz')
tar.extractall()
tar.close()
