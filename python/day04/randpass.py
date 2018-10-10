import random
import string
def getpass(n=8):
    result = ''
    str = string.ascii_letters + string.digits
    for i in range(n):
        num = random.choice(str)
        result += num
    return  result

if __name__ == '__main__':
    print(getpass())
    print(getpass(120))


# def getpassword(n=8):
#     result =''.join(random.sample(string.ascii_letters + string.digits,n))
#     return result
#
# print(getpassword(100))