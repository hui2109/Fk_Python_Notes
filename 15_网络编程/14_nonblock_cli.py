import selectors
import socket
import threading

sel = selectors.DefaultSelector()


def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print(data.decode('utf-8'))
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


s = socket.socket()
s.connect(('192.168.1.223', 30000))
s.setblocking(False)
sel.register(s, selectors.EVENT_READ, read)


def keyboard_input(s):
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        s.send(line.encode('utf-8'))


threading.Thread(target=keyboard_input, args=(s,)).start()

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
