import socket
import threading

socket_list = []

ss = socket.socket()
ss.bind(('192.168.1.223', 30000))
ss.listen()


def read_from_client(s: socket.socket):
    try:
        return s.recv(2048).decode('utf-8')
    except Exception:
        socket_list.remove(s)


def server_target(s: socket.socket):
    try:
        while True:
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client_s in socket_list:
                client_s.send(content.encode('utf-8'))
    except Exception as e:
        print(e.strerror)


while True:
    s, addr = ss.accept()
    socket_list.append(s)
    threading.Thread(target=server_target, args=(s,)).start()
