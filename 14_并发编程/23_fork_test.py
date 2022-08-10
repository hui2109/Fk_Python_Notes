import os

print('父进程(%s)开始执行'%os.getpid())
pid=os.fork()
print('进程进入:%s'%os.getpid(),pid)
if pid==0:
    print('子进程,其ID为(%s),父进程ID为(%s)'%(os.getpid(),os.getppid()))
    print(__name__)
else:
    print('我(%s)创建的子进程ID为(%s).'%(os.getpid(),pid))
    print(__name__)
print('进程结束:%s'%os.getpid())