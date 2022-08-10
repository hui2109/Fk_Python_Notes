from asyncio import events
import threading,time

event=threading.Event()
def cal(name):
    print('%s 启动'%threading.currentThread().name)
    print('%s 准备开始计算状态'%name)
    event.wait()

    print('%s 收到通知了。'%threading.currentThread().name)
    print('%s 正在开始计算!'%name)

threading.Thread(target=cal,args=['甲']).start()
threading.Thread(target=cal,args=['乙']).start()

time.sleep(2)

print('--------------------------------')

print('主线程发出事件')
event.set()


