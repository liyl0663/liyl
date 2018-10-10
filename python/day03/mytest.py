# print('hello world','#' * 50)
# print('how are you?')
#
# number = input("Please enter a word:")
# print(number)
# print(type(number))
#
# print(int(number)+10)
##########################################
# sentence = '\033[31mtom\'s pet is a cat\033[0m'
# sentence2 = "\033[32mtom's pet is a cat\033[0m"
# sentence3 =  "\033[33mtom said:\"hello world!\"\033[0m"
# sentence4 = '\033[34mtom said:"hello world!\033[0m"'
# print(sentence + '\n' + sentence2 + '\n' + sentence3 + '\n' + sentence4)
#
# words = """
# \033[35mhello
# world
# lili\033[0m"""
# print(words)
###########################################
# py_str = 'python'
# print(len(py_str))
# print(py_str[0])
# print('python'[0])
# print(py_str[-1])
# print(py_str[-3:-1])
# print(py_str[2:4])
# print(py_str[2:])
# print(py_str[:4])
# print(py_str[::2])
# print(py_str[1::2])
# print(py_str[::-1])
# print(py_str + 'is good')
# print(py_str * 3)
# print('t' in py_str)
# print('th' in py_str)
# print('to' in py_str)
# print('to' not in py_str)
############################################
# adict={'name':'bob','age':22}
# print(len(adict))
# print('name' in adict)
# print('bob' in adict)
# print(adict['name'])
# adict['email'] = 'liyl@qq.com'
# print(adict)
# adict['age'] = 24
# print(adict)
###########################################
# if -0.0:
#     print('yes')
# print('no')
#
# if [1,2]:
#     print('yes')
# if " ":
#     print('yes')
###########################################
# a = 10
# b = 20
#
# if a > b:
#     small = b
# else:
#     small = a
# print(small)
#
# s = a if a < b else b
# print(s)
#
# print(10//3)
import urllib.request
response = urllib.request.urlopen("https://www.python.org")
#print(response.read().decode('utf-8'))
#print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))