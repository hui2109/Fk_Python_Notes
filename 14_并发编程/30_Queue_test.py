import multiprocessing

def f(q):
    print('(%s)进程开始放入数据...'%multiprocessing.current_process().pid)
    q.put('Python')

if __name__ == '__main__':
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=f,args=(q,))
    p.start()
    print('(%s)进程开始取出数据...'%multiprocessing.current_process().pid)
    print(q.get())
    p.join()

