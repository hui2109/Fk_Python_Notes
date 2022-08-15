import selectors
import socket

sel = selectors.DefaultSelector()


def read(skt, mask):
    try:
        data = skt.recv(1024)
        if data:
            for s in socket_list:
                s.send(data)
        else:
            print('关闭', skt)
            sel.unregister(skt)
            skt.close()
            socket_list.remove(skt)
    except Exception:
        print('关闭', skt)
        sel.unregister(skt)
        skt.close()
        socket_list.remove(skt)


def accept(sock, mask):
    conn, addr = sock.accept()
    socket_list.append(conn)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


socket_list = []
sock = socket.socket()
sock.bind(('10.68.0.238', 30000))
sock.listen()
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
