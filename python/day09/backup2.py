import os
import time
import pickle
import hashlib
import tarfile

def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def full_back(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_full_%s' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir,fname)
    md5dict = {}

    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()

    for path,folders,files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
         pickle.dump(md5dict,fobj)

def incr_full(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir,fname)
    md5dict = {}

    with open(md5file,'rb') as fobj:
        oldmd5file = pickle.load(fobj)

    for path,folders,files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

    tar = tarfile.open(fname,'w:gz')
    for key in md5dict:
        if oldmd5file.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    srcdir = '/tmp/security'
    dstdir = '/tmp/backup'
    md5file = '/tmp/backup/md5.data'
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)
    if time.strftime('%a') == 'Mon':
        full_back(srcdir,dstdir,md5file)
    else:
        incr_full(srcdir,dstdir,md5file)
