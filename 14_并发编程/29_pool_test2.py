import multiprocessing
import os
import time

def action(max):
    my_sum=0
    for i in range(max):
        print('(%s)进程正在执行:%d'%(os.getpid(),i))
        my_sum+=i
    return my_sum

if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        results=pool.map(action,[50,100,150])
        print('------------')
        for i in results:
            print(i)