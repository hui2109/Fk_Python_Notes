import socket
from Get_IP import extract_ip

PORT = 30000
DATA_LEN = 4096
DEST_IP = extract_ip()

s = socket.socket(type=socket.SOCK_DGRAM)
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    data = line.encode('utf=8')
    s.sendto(data, (DEST_IP, PORT))
    data = s.recv(DATA_LEN)
    print(data.decode('utf-8'))
s.close()
