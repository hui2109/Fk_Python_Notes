from concurrent.futures import ThreadPoolExecutor
import threading
import time

def action(max):
    my_sum=0
    for i in range(max):
        print(threading.current_thread().name+' '+str(i))
        my_sum+=i
    return my_sum

pool=ThreadPoolExecutor(2)
future1=pool.submit(action,50)
future2=pool.submit(action,100)
print(future1.done())

# time.sleep(3)

print(future2.done())
print(future1.result())
print(future2.result())

# 由于阻塞了主线程，下段代码永远只能在result后执行
print('-------------------------')
pool.shutdown()
