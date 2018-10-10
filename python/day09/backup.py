import os
import hashlib
import time
import pickle
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

def full_backup(src_dic,dst_dic,md5file):
    fname = os.path.basename(src_dic.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dic,fname)
    md5dict = {}
    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dic)
    tar.close()

    for path,folders,files in os.walk(src_dic):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

def incr_backup(src_dic,dst_dic,md5file):
    fname = os.path.basename(src_dic.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dic,fname)
    md5dict = {}

    with open(md5file,'rb') as fobj:
        oldmd5 = pickle.load(fobj)

    for path,folders,files in os.walk(src_dic):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

    tar = tarfile.open(fname,'w:gz')
    for key in md5dict:
        if oldmd5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src_dic = '/tmp/security'
    dst_dic = '/tmp/backup'
    md5file = '/tmp/backup/md5.data'
    if not os.path.exists(dst_dic):
         os.mkdir(dst_dic)
    if time.strftime('%a') == 'Mon':
        full_backup(src_dic,dst_dic,md5file)
    else:
        incr_backup(src_dic,dst_dic,md5file)