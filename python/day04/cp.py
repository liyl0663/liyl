import os

src_fname = '/bin/ls'
dst_fname = '/tmp/lscp'
src_fobj = open(src_fname,'rb')
dst_fobj = open(dst_fname,'wb')

while True:
    data = src_fobj.read(4096)
    if len(data) == 0:
        break
    dst_fobj.write(data)
src_fobj.close()
dst_fobj.close()

# src_md5 = os.system("md5sum -c /bin/ls /tmp/lscp")
# print(src_md5)
# if src_md5 == 0:
#     print('yes')
# else:
#     print('no')