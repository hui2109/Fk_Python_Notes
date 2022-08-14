import MyCrazyitProtocol


def server_target(s, clients: dict):
    try:
        while True:
            line = s.recv(2048).decode('utf-8')
            print(line)

            if line.startswith(MyCrazyitProtocol.USER_ROUND) and \
                    line.endswith(MyCrazyitProtocol.USER_ROUND):
                user_name = line[MyCrazyitProtocol.PROTOCOL_LEN:
                                 -MyCrazyitProtocol.PROTOCOL_LEN]
                if user_name in clients:
                    print('重复')
                    s.send(MyCrazyitProtocol.NAME_REP.encode('utf-8'))
                else:
                    print('成功')
                    s.send(MyCrazyitProtocol.LOGIN_SUCCESS.encode('utf-8'))
                    clients[user_name] = s
            elif line.startswith(MyCrazyitProtocol.PRIVATE_ROUND) and line.endswith(MyCrazyitProtocol.PRIVATE_ROUND):
                user_and_msg = line[MyCrazyitProtocol.PROTOCOL_LEN:-MyCrazyitProtocol.PROTOCOL_LEN]
                user = user_and_msg.split(MyCrazyitProtocol.SPLIT_SIGN)[0]
                msg = user_and_msg.split(MyCrazyitProtocol.SPLIT_SIGN)[1]

                clients[user].send((clients.key_from_value(s) + '悄悄对你说：' + msg).encode('utf-8'))
            else:
                msg = line[MyCrazyitProtocol.PROTOCOL_LEN:-MyCrazyitProtocol.PROTOCOL_LEN]
                for client_socket in clients.values():
                    client_socket.send((clients.key_from_value(s) + '说：' + msg).encode('utf-8'))
    except Exception:
        clients.remove_by_value(s)
        print(len(clients))
        if s is not None:
            s.close()
