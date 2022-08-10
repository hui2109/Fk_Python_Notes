import multiprocessing,os

def foo(q):
    print('被启动的新进程:(%s)'%os.getpid())
    q.put('python')

if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    q=multiprocessing.Queue()
    mp=multiprocessing.Process(target=foo,args=[q])
    mp.start()
    print(q.get())
    mp.join()

    