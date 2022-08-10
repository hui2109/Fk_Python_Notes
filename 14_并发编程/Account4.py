import threading,time

class Account:
    def __init__(self,account_no,balance) :
        self.account_no=account_no
        self._balance=balance
        self.lock=threading.Lock()
        self.event=threading.Event()
        self.wait_time=0.05
    def getBalance(self):
        return self._balance
    def draw(self,draw_amount):
        self.lock.acquire()
        if self.event.is_set():
            print(threading.current_thread().name \
                        +' 取钱:'+str(draw_amount))
            self._balance -= draw_amount
            print('账户余额为:'+str(self._balance))
            self.event.clear()
            self.lock.release()
            time.sleep(self.wait_time)
        else:
            self.lock.release()
            time.sleep(self.wait_time)
    def deposit(self,deposit_amount):
        self.lock.acquire()
        if not self.event.is_set():
            print(threading.current_thread().name \
                        +' 存款:'+str(deposit_amount))
            self._balance+=deposit_amount
            print('账户余额为:'+str(self._balance))
            self.event.set()
            self.lock.release()
            time.sleep(self.wait_time)
        else:
            self.lock.release()
            time.sleep(self.wait_time)