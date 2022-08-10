import threading

class Account:
    def __init__(self,account_no,balance) -> None:
        self.account_no=account_no
        self._balance=balance
        self.cond=threading.Condition()
        self._flag=False
    def getBalance(self):
        return self._balance
    def draw(self,draw_amount):
        self.cond.acquire()
        try:
            if not self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name \
                        +' 取钱:'+str(draw_amount))
                self._balance -= draw_amount
                print('账户余额为:'+str(self._balance))
                self._flag=False
                self.cond.notify_all()
        finally:
            print('yes')
            self.cond.release()
    def deposit(self,deposit_amount):
        self.cond.acquire()
        try:
            if self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name \
                        +' 存款:'+str(deposit_amount))
                self._balance+=deposit_amount
                print('账户余额为:'+str(self._balance))
                self._flag=True
                self.cond.notify_all()
        finally:
            self.cond.release()