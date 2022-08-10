import multiprocessing,os

def foo(q):
    print('被启动的新进程:(%s)'%os.getpid())
    q.put('python')

if __name__=='__main__':
    ctx=multiprocessing.get_context('fork')
    q=ctx.Queue()
    mp=ctx.Process(target=foo,args=[q])
    mp.start()
    print(q.get())
    mp.join()