import threading
from concurrent.futures import ThreadPoolExecutor

class Sequence:
    def __init__(self):
        self.count=0
        self.state=1
        self.cond=threading.Condition()
    def action(self,thread_num):
        try:
            self.cond.acquire()
            while self.state != thread_num:
                self.cond.wait()
            for i in range(5):
                self.count+=1
                print(threading.current_thread().name+' '+str(self.count))
            self.state=self.state%3+1
            self.cond.notify_all()
        finally:
            self.cond.release()
def take(se,thread_num):
    for i in range(5):
        se.action(thread_num)

se=Sequence()
with ThreadPoolExecutor(3) as pool:
    for i in range(3):
        pool.submit(take,se,i+1)
