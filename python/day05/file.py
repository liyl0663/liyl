import os
def get_fname():
    while True:
        fname = input("请输入文件名：")
        if not os.path.exists(fname):
            break
        print('%s已存在，请重试' % fname)
    return fname

def get_content():
    content = []
    input("请输入文件内容(输入end结束)")
    while True:
        line = input('> ')
        if line == 'end':
            break
        content.append(line)
    return content

def wfile(fname,content):
    with open(fname,'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname,content)