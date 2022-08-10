import threading
import time
import Account

def draw(account,draw_amount):
    if account.balance>=draw_amount:
        print(threading.currentThread().name + \
            '取钱成功!吐出钞票:'+str(draw_amount))
        time.sleep(0.001)
        account.balance -=draw_amount
        print('\t余额为:'+str(account.balance))
    else:
        print(threading.currentThread().name + \
            '取钱失败!余额不足!')

acct=Account.Account('1234567',1000)
threading.Thread(name='甲',target=draw,args=[acct,800]).start()
threading.Thread(name='乙',target=draw,args=[acct,800]).start()