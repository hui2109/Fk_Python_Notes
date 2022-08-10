import multiprocessing
import os

class MyProcess(multiprocessing.Process):
    def __init__(self,max):
        self.max=max
        super().__init__()
    def run(self):
        for i in range(self.max):
            print('(%s)子进程(父进程:(%s)):%d'%
                (os.getpid(),os.getppid(),i))

if __name__ == '__main__':
    for i in range(100):
        print('(%s)主进程:%d'%(os.getpid(),i))
        if i==20:
            mp1=MyProcess(100)
            mp1.start()

            mp2=MyProcess(100)
            mp2.start()

            mp2.join()
    print('主进程执行完成!')
