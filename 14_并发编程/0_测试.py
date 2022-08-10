# import threading,time
# def abc(max):
#     for i in range(max):
#         print(str(i))
# threading.Thread(target=abc,args=[100]).start()
# time.sleep(10)

count=0
def xyz():
    
    print(count)
count+=1
xyz()