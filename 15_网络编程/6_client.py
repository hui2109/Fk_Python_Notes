import socket

s = socket.socket()
s.connect(('192.168.1.223', 30000))
print('--%s--' % s.recv(1024).decode('utf-8'))
s.close()
