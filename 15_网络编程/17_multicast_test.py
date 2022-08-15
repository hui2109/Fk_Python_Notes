import socket
import threading

from Get_IP import extract_ip

SENDERIP = extract_ip()
SENDERPORT = 30000
MYGROUP = '230.0.0.1'

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('0.0.0.0', SENDERPORT))
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
             socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))


def read_socket(sock):
    while True:
        data = sock.recv(2048)
        print('信息', data.decode('utf-8'))


threading.Thread(target=read_socket, args=(s,)).start()

while True:
    line = input('')
    if line is None or line == 'exit':
        break
    s.sendto(line.encode('utf-8'), (MYGROUP, SENDERPORT))
