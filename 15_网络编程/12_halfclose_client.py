import socket

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('192.168.1.223', 30000))
while True:
    # 从socket读取数据
    line = s.recv(2048).decode('utf-8')
    if line is None or line == '':
        break
    print(line)
s.send("客户端的第1行数据".encode('utf-8'))
s.send("客户端的第2行数据".encode('utf-8'))
s.close()
