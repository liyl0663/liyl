import socket

host = ''
port = 123456
addr = (host,port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
s.bind(addr)
s.listen(1)

cli_sock,cli_addr = s.accept()
print('client connect from:',cli_addr)
print(cli_sock.recv(1024))
cli_sock.send(b'hello\r\n')
cli_sock.close()
s.close()