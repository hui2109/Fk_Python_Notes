from concurrent.futures import ThreadPoolExecutor
import threading
import time

def action(max):
    my_sum=0
    for i in range(max):
        print(threading.current_thread().name+'  '+str(i))
        my_sum+=i
    return my_sum

if __name__ == '__main__': 
    with ThreadPoolExecutor(4) as pool:
        results=pool.map(action,[50,100,150])
        print('---------------')
        for r in results:
            # print(results)
            print(r)
# pool=ThreadPoolExecutor(3)
# results=pool.map(action,[50,100,150])
# print('---------------')
# for r in results:
#     print(results)
#     print(r)
# print([i for i in results])
# pool.shutdown()