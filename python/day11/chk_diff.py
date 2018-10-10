import difflib
import sys

def readline(filename):
    try:
        fileHandle = open(filename,'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()

if __name__ == '__main__':
    try:
        textfile1 = sys.argv[1]
        textfile2 = sys.argv[2]
    except Exception as e:
        print('Error:' + str(e))
        print('Usage:%s filename1 filename2' % sys.argv[0])
        sys.exit()