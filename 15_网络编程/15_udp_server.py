import socket
from Get_IP import extract_ip

PORT = 30000
DATA_LEN = 4096

books = (
    '疯狂Python讲义',
    '疯狂Kotlin讲义',
    '疯狂Android讲义',
    '疯狂Swift讲义'
)

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind((extract_ip(), PORT))

for i in range(1000):
    data, addr = s.recvfrom(DATA_LEN)
    print(data.decode('utf-8'))
    send_data = books[i % 4].encode('utf=8')
    s.sendto(send_data, addr)
s.close()
