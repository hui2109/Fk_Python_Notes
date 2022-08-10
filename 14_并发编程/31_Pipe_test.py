import multiprocessing

def f(conn):
    print('(%s)进程开始发送数据...'%multiprocessing.current_process().pid)
    conn.send('Python')

if __name__ == '__main__':
    parent_conn,child_conn=multiprocessing.Pipe()
    p=multiprocessing.Process(target=f,args=(child_conn,))
    p.start()
    print('(%s)进程开始取出数据...'%multiprocessing.current_process().pid)
    print(parent_conn.recv())
    p.join()