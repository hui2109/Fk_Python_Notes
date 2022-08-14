import MyCrazyitProtocol
import socket
import sys
import threading
import time

SERVER_PORT = 30000


def read_send(s: socket.socket):
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        if ':' in line and line.startswith('//'):
            line = line[2:]
            s.send((MyCrazyitProtocol.PRIVATE_ROUND + line.split(':')[0] + MyCrazyitProtocol.SPLIT_SIGN +
                    line.split(':')[1] + MyCrazyitProtocol.PRIVATE_ROUND).encode('utf-8'))
        else:
            s.send((MyCrazyitProtocol.MSG_ROUND + line + MyCrazyitProtocol.MSG_ROUND).encode('utf-8'))


def client_target(s: socket.socket):
    try:
        while True:
            line = s.recv(2048).decode('utf-8')
            if line is not None:
                print(line)
    finally:
        s.close()


s = socket.socket()
try:
    s.connect(('192.168.1.223', SERVER_PORT))
    tip = ''
    while True:
        user_name = input(tip + '输入用户名：\n')
        s.send((MyCrazyitProtocol.USER_ROUND + user_name + MyCrazyitProtocol.USER_ROUND).encode('utf-8'))
        time.sleep(0.2)
        result = s.recv(2048).decode('utf-8')
        if result is not None and result != '':
            if result == MyCrazyitProtocol.NAME_REP:
                tip = '用户名重复，请重新输入！'
                continue
            if result == MyCrazyitProtocol.LOGIN_SUCCESS:
                break
except Exception:
    print('网络异常，请重新登录！')
    s.close()
    sys.exit(-1)

threading.Thread(target=client_target, args=(s,)).start()
read_send(s)
