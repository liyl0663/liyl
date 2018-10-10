import socket
import os

host = ''
port = 12345
addr =(host,port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)

while True:
    cli_sock,cli_addr = s.accept()
    print('clent:',cli_addr)
    while True:
        data = cli_sock.recv(1024).decode()
        if data.strip() == b'quit':
            break
        print(data,end='')
        rdata = input('> ') + '\r\n'
        cli_sock.send(rdata.encode())
        #cli_sock.send(os.system('reboot'))
    cli_sock.close()
s.close()
