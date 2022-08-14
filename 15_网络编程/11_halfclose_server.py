import socket

s = socket.socket()

s.bind(('192.168.1.223', 30000))
s.listen()
skt, addr = s.accept()
skt.send('服务器的第一行数据'.encode('utf-8'))
skt.send('服务器的第二行数据'.encode('utf-8'))
skt.shutdown(socket.SHUT_WR)
while True:
    line = skt.recv(2048).decode('utf-8')
    if line is None or line == '':
        break
    print(line)
skt.close()
s.close()
