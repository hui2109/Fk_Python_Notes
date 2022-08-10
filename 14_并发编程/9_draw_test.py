import threading
import Account2

def draw(account,draw_account):
    account.draw(draw_account)
acct=Account2.Account('1234567',1000)
threading.Thread(name='甲',target=draw,args=[acct,800]).start()
threading.Thread(name='乙',target=draw,args=[acct,800]).start()