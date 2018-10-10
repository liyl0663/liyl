import sys
def cp_file_function(src_fname,dst_fname):
    src_fobj = open(src_fname,'rb')
    dst_fobj = open(dst_fname,'wb')
    while True:
        data = src_fobj.read(4096)
        if len(data) == 0:
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

cp_file_function(sys.argv[1], sys.argv[2])

#if __name__ == '__main__':
#     cp_file_function('/bin/ls','/tmp/lssl')
#     print(__name__)

