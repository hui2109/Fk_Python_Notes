import sched,time
import threading

s=sched.scheduler()

def print_time(name='default'):
    print('%s 的时间:%s'%(name,time.ctime()))
print('主线程',time.ctime())

s.enter(10,1,print_time)

s.enter(5,2,print_time,('位置参数',))

s.enter(5,1,print_time,kwargs={'name':'关键字参数'})

s.run()
print('主线程: ',time.ctime())