import shutil
import os
import sys
# def copy(src_fname,dst_fname):
#     shutil.copy(src_fname,dst_fname)

def copy(src_fname,dst_fname):
    shutil.copytree(src_fname,dst_fname)

def menu(src_fname,dst_fname):
    if not os.path.exists(src_fname):
        print('源文件不存在')
    else:
        copy(src_fname,dst_fname)
        # if os.path.isfile(src_fname):
        #     copy(src_fname,dst_fname)
        # else:
        #     copy2(src_fname,dst_fname)

if __name__ == '__main__':
    src_fname = sys.argv[1]
    dst_fname = sys.argv[2]
    menu(src_fname,dst_fname)

