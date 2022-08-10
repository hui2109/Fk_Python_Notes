import threading

class Account:
    def __init__(self,account_no,balance) :
        self.account_no=account_no
        self._balance=balance
        self.lock=threading.Lock()
        self.event=threading.Event()
    def getBalance(self):
        return self._balance
    def draw(self,draw_amount):
        if self.event.is_set():  # 旗帜为True,则继续执行
            print(threading.current_thread().name \
                        +' 取钱:'+str(draw_amount))
            self._balance -= draw_amount
            print('账户余额为:'+str(self._balance))
            self.event.clear()
            self.event.wait()
        else:
            self.event.wait(5)
    def deposit(self,deposit_amount):
        if not self.event.is_set(): # 旗帜为False,则继续执行
            print(threading.current_thread().name \
                        +' 存款:'+str(deposit_amount))
            self._balance+=deposit_amount
            print('账户余额为:'+str(self._balance))
            self.event.set()
            print(self.event.wait(),1)
        else:
            print(self.event.wait(),2)
    