import os
import requests
import sys
import hashlib
import tarfile

def check_version(remote_ver, local_ver):
#判断服务器上是否有新版本，有则返回True，否则返回False
    if not os.path.exists(local_ver):
        return True

    r = requests.get(remote_ver)
    with open(local_ver) as fobj:
        version = fobj.read()

    if version != r.text:
        return True

    return False

def check_md5(md5_url, local_fname):
    r = requests.get(md5_url)
    m = hashlib.md5()
    with open(local_fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    if m.hexdigest() == r.text.strip():
        return True

    return False

def download(url, dst_name):
    r = requests.get(url)
    if r.status_code != 200:
        return False
    else:
        with open(dst_name, 'wb') as fobj:
            fobj.write(r.content)
        return True

def deploy(pkg, ver):
    dst_path = '/var/www/packages'
    s_link = '/var/www/html/mysite'
    os.chdir(dst_path)
    tar = tarfile.open(pkg, 'r:gz')
    tar.extractall()
    tar.close()
    src_fname = '%s/mp-%s' % (dst_path,ver)
    if os.path.exists(s_link):
        os.unlink(s_link)
    os.symlink(src_fname, s_link)

if __name__ == '__main__':
    remote_ver = 'http://192.168.4.12/deploy/live_version'
    local_ver = '/var/www/packages/live_version'
    new_ver = check_version(remote_ver, local_ver)
    if not new_ver:
        sys.exit(0)

    r = requests.get(remote_ver)
    ver = r.text.strip()
    soft_url = 'http://192.168.4.12/deploy/packages/mp-%s.tar.gz' % ver
    local_fname = '/var/www/packages/mp-%s.tar.gz' % ver
    file_exist = download(soft_url, local_fname)
    if not file_exist:
        sys.exit(1)

    md5_url = 'http://192.168.4.12/deploy/packages/mp-%s.tar.gz.md5' % ver
    file_ok = check_md5(md5_url, local_fname)
    if not file_ok:
        sys.exit(2)

    download(remote_ver, local_ver)
    deploy(local_fname,ver)