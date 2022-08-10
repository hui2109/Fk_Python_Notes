import threading
import Account3

def draw_many(account,draw_amount,max):
    for i in range(max):
        account.draw(draw_amount)
def deposit_many(account,deposit_amount,max):
    for i in range(max):
        account.deposit(deposit_amount)    
acct=Account3.Account('1234567',0)

threading.Thread(name='取钱者甲',target=draw_many,args=[acct,800,100]).start()
threading.Thread(name='取钱者乙',target=draw_many,args=[acct,800,100]).start()
threading.Thread(name='取钱者丙',target=draw_many,args=[acct,800,100]).start()

threading.Thread(name='存款者甲',target=deposit_many,args=[acct,800,100]).start()
threading.Thread(name='存款者乙',target=deposit_many,args=[acct,800,100]).start()
threading.Thread(name='存款者丙',target=deposit_many,args=[acct,800,100]).start()

# threading.Thread(name='取钱者乙',target=draw_many,args=[acct,800,100]).start()
# threading.Thread(name='取钱者丙',target=draw_many,args=[acct,800,100]).start()

print(threading.current_thread().name+'已经运行完成')
