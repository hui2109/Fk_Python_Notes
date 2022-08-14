import socket

s = socket.socket()
s.bind(('192.168.1.223', 30000))
s.listen()
while True:
    c, addr = s.accept()
    print(c)
    print('连接地址，', addr)
    c.send('您好，您收到了服务器的新年祝福！'.encode('utf-8'))
    c.close()
