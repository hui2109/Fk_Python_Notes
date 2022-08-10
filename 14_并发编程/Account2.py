import threading,time

class Account:
    def __init__(self,account_no,balance) -> None:
        self.account_no=account_no
        self._balance=balance
        self.lock=threading.RLock()
    def getBalance(self):
        return self._balance
    def draw(self,draw_account):
        self.lock.acquire()
        try:
            if self._balance>=draw_account:
                print(threading.current_thread().name \
                    +'取钱成功!吐出钞票:'+str(draw_account))
                time.sleep(0.001)
                self._balance-=draw_account
                print('\t余额为:'+str(self._balance))
            else:
                print(threading.current_thread().name +\
                    '取钱失败!余额不足!')
        finally:
            self.lock.release()