import socket
import threading

s = socket.socket()

s.connect(('192.168.1.223', 30000))


def read_from_server(s: socket.socket):
    while True:
        print(s.recv(2048).decode('utf-8'))


threading.Thread(target=read_from_server, args=(s,)).start()

while True:
    line = input('')
    if line is None or line == 'exit':
        break
    s.send(line.encode('utf-8'))
