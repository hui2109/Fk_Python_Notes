from concurrent.futures import ThreadPoolExecutor
import threading

mydata = threading.local()
def action (max):
    for i in range(max):
        try:
            mydata.x += i
        except:
            mydata.x = i
        print('%s mydata.x的值为: %d' % (threading.current_thread().name,mydata.x))
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(action , 10)
    pool.submit(action , 10)