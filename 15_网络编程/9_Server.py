import MyCrazyitDict
import socket
import threading

from server_thread import server_target

SERVER_PORT = 30000

clients = MyCrazyitDict.CrazyitDict()
ss = socket.socket()
try:
    ss.bind(('192.168.1.223', SERVER_PORT))
    ss.listen()
    while True:
        c, addr = ss.accept()
        threading.Thread(target=server_target, args=(c, clients)).start()
except Exception:
    print('服务器启动失败，是否端口%d已被占用？' % SERVER_PORT)
