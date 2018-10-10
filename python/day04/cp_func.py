import sys
def funcp(f1,f2):
    src_fname = f1
    dst_fname = f2
    src_fobj = open(src_fname,'rb')
    dst_fobj = open(dst_fname,'wb')

    while True:
        data = src_fobj.read(4096)
        if len(data) == 0:
            break
        dst_fobj.write(data)
    src_fobj.close()
    dst_fobj.close()
funcp(sys.argv[1],sys.argv[2])


